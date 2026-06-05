import os
import json
import requests
import time
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load environment variables
load_dotenv()

METRICS_FILE = os.path.join("logs", "provider_metrics.json")

def log_metric(provider: str, success: bool, latency_ms: float, is_timeout: bool = False):
    """
    Appends execution metrics and computes a rolling latency average in logs/provider_metrics.json.
    """
    try:
        os.makedirs("logs", exist_ok=True)
        metrics = {
            "hf_success": 0,
            "hf_failure": 0,
            "hf_timeout": 0,
            "gemini_success": 0,
            "avg_latency_ms": 0.0,
            "total_generations": 0
        }
        
        if os.path.exists(METRICS_FILE):
            with open(METRICS_FILE, "r") as f:
                content = f.read().strip()
                if content:
                    metrics = json.loads(content)
                    
        # Update metrics
        if provider == "huggingface":
            if success:
                metrics["hf_success"] += 1
            else:
                if is_timeout:
                    metrics["hf_timeout"] += 1
                else:
                    metrics["hf_failure"] += 1
        elif provider == "gemini":
            if success:
                metrics["gemini_success"] += 1
                
        total = metrics.get("total_generations", 0)
        curr_avg = metrics.get("avg_latency_ms", 0.0)
        
        # Calculate rolling average latency
        new_avg = ((curr_avg * total) + latency_ms) / (total + 1)
        metrics["avg_latency_ms"] = round(new_avg, 2)
        metrics["total_generations"] = total + 1
        
        with open(METRICS_FILE, "w") as f:
            json.dump(metrics, f, indent=2)
    except Exception as e:
        print(f"Warning: Failed to log provider metrics: {e}")

class BaseProvider:
    def generate(self, system_prompt: str, user_content: str) -> str:
        raise NotImplementedError("Providers must implement generate()")

class GeminiProvider(BaseProvider):
    def __init__(self, api_key: str = None, model_name: str = None):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not found in environment.")
        self.model_name = model_name or os.getenv("GEMINI_MODEL_NAME", "gemini-2.5-flash")
        self.client = genai.Client(api_key=self.api_key)

    def generate(self, system_prompt: str, user_content: str) -> str:
        # Standard retry loop with exponential backoff to handle transient 503 / 429 errors from Free Tier
        last_error = None
        for attempt in range(3):
            try:
                response = self.client.models.generate_content(
                    model=self.model_name,
                    contents=user_content,
                    config=types.GenerateContentConfig(
                        system_instruction=system_prompt,
                        temperature=0.3
                    )
                )
                if not response.text:
                    raise ValueError("Gemini returned empty text response.")
                return response.text.strip()
            except Exception as e:
                last_error = e
                if attempt < 2:
                    # Smart handle for 429 rate limit: sleep longer (45s) to let quota reset
                    err_str = str(e)
                    sleep_time = 45 if ("429" in err_str or "RESOURCE_EXHAUSTED" in err_str) else (2 ** attempt)
                    print(f"[ROUTING] Gemini attempt {attempt + 1} failed: {e}. Retrying in {sleep_time}s...")
                    time.sleep(sleep_time)
        raise RuntimeError(f"Gemini generation failed after 3 attempts: {last_error}")

class HuggingFaceProvider(BaseProvider):
    def __init__(self, api_key: str = None, model_name: str = None):
        # Support both HF_API_KEY and hugging_face from env/dot-env
        self.api_key = api_key or os.getenv("HF_API_KEY") or os.getenv("hugging_face")
        if not self.api_key:
            raise ValueError("Hugging Face API key not configured in environment.")
        self.model_name = model_name or os.getenv("HF_MODEL_NAME", "Qwen/Qwen2.5-72B-Instruct")
        
        # Use InferenceClient as preferred and verified in your environment
        from huggingface_hub import InferenceClient
        self.client = InferenceClient(token=self.api_key, timeout=60)

    def generate(self, system_prompt: str, user_content: str) -> str:
        try:
            # Set a 12-second timeout configured on the client constructor above
            response = self.client.chat_completion(
                model=self.model_name,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_content}
                ],
                max_tokens=2048,
                temperature=0.3
            )
            
            text = response.choices[0].message.content
            if not text:
                raise ValueError("Hugging Face model returned empty choices content.")
            return text.strip()
        except Exception as e:
            # Check if this is a timeout exception
            err_str = str(e)
            if "timeout" in err_str.lower() or "timed out" in err_str.lower():
                raise requests.exceptions.Timeout(f"Hugging Face API request timed out (60s threshold): {e}")
            raise RuntimeError(f"Hugging Face generation failed: {e}")

def route_and_generate(system_prompt: str, user_content: str) -> str:
    primary = os.getenv("PRIMARY_GENERATION_PROVIDER", "huggingface").lower()
    fallback = os.getenv("FALLBACK_GENERATION_PROVIDER", "gemini").lower()
    
    # Check if HF key exists when HF is primary
    hf_key = os.getenv("HF_API_KEY") or os.getenv("hugging_face")
    
    if primary == "huggingface" and not hf_key:
        print("[ROUTING] WARNING: Primary provider 'huggingface' key not configured. Falling back to Gemini.")
        primary = "gemini"
        
    if primary == "huggingface":
        print("[ROUTING] Attempting primary provider: 'huggingface'")
        start_time = time.perf_counter()
        try:
            provider = HuggingFaceProvider()
            result = provider.generate(system_prompt, user_content)
            latency = (time.perf_counter() - start_time) * 1000.0
            log_metric("huggingface", success=True, latency_ms=latency)
            return result
        except requests.exceptions.Timeout as te:
            latency = (time.perf_counter() - start_time) * 1000.0
            log_metric("huggingface", success=False, latency_ms=latency, is_timeout=True)
            print(f"[ROUTING] WARNING: Primary provider 'huggingface' timed out: {te}")
            print(f"[ROUTING] Triggering automatic fallback to: '{fallback}' (gemini-2.5-flash)")
            
            # Call fallback
            return _call_fallback(fallback, system_prompt, user_content)
        except Exception as e:
            latency = (time.perf_counter() - start_time) * 1000.0
            log_metric("huggingface", success=False, latency_ms=latency, is_timeout=False)
            print(f"[ROUTING] WARNING: Primary provider 'huggingface' failed: {e}")
            print(f"[ROUTING] Triggering automatic fallback to: '{fallback}' (gemini-2.5-flash)")
            
            # Call fallback
            return _call_fallback(fallback, system_prompt, user_content)
    else:
        # Primary is gemini
        print("[ROUTING] Attempting primary provider: 'gemini'")
        start_time = time.perf_counter()
        try:
            provider = GeminiProvider()
            result = provider.generate(system_prompt, user_content)
            latency = (time.perf_counter() - start_time) * 1000.0
            log_metric("gemini", success=True, latency_ms=latency)
            return result
        except Exception as e:
            latency = (time.perf_counter() - start_time) * 1000.0
            log_metric("gemini", success=False, latency_ms=latency)
            raise RuntimeError(f"Primary provider 'gemini' failed: {e}")

def _call_fallback(provider_name: str, system_prompt: str, user_content: str) -> str:
    start_time = time.perf_counter()
    try:
        if provider_name == "gemini":
            provider = GeminiProvider()
            result = provider.generate(system_prompt, user_content)
            latency = (time.perf_counter() - start_time) * 1000.0
            log_metric("gemini", success=True, latency_ms=latency)
            print("[ROUTING] Success! Synthesis completed using fallback provider: 'gemini'")
            return result
        else:
            provider = HuggingFaceProvider()
            result = provider.generate(system_prompt, user_content)
            latency = (time.perf_counter() - start_time) * 1000.0
            log_metric("huggingface", success=True, latency_ms=latency)
            print("[ROUTING] Success! Synthesis completed using fallback provider: 'huggingface'")
            return result
    except Exception as e:
        raise RuntimeError(f"Fallback provider '{provider_name}' failed: {e}")