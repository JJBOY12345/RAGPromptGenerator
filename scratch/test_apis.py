import os
import requests
import sys
from dotenv import load_dotenv

# Ensure stdout uses UTF-8 on Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

load_dotenv()

def test_gemini():
    print("[TEST] Checking Gemini API Connection...")
    key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if not key:
        print("[FAIL] GEMINI_API_KEY is not configured in .env.")
        return False
    try:
        from google import genai
        client = genai.Client(api_key=key)
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents="Respond with the word: WORKING"
        )
        output = response.text.strip()
        print(f"[SUCCESS] Gemini API is working! Response: '{output}'")
        return True
    except Exception as e:
        print(f"[FAIL] Gemini API check failed: {e}")
        return False

def test_hf():
    print("[TEST] Checking Hugging Face API Connection...")
    key = os.getenv("hugging_face") or os.getenv("HF_API_KEY") or os.getenv("HUGGINGFACE_API_KEY")
    if not key:
        print("[SKIP] HF key is not configured in .env.")
        print("       Please add your Hugging Face API key to the .env file like this:")
        print("       hugging_face=your_hugging_face_token_here")
        return False
        
    model = os.getenv("HF_MODEL_NAME", "Qwen/Qwen2.5-72B-Instruct")
    print(f"[*] Targeting Hugging Face model: '{model}'")
    
    url = "https://api-inference.huggingface.co/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "messages": [
            {"role": "user", "content": "Respond with the word: WORKING"}
        ],
        "max_tokens": 10
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=20)
        if response.status_code == 200:
            data = response.json()
            output = data["choices"][0]["message"]["content"].strip()
            print(f"[SUCCESS] Hugging Face API is working! Response: '{output}'")
            return True
        else:
            print(f"[FAIL] Hugging Face API returned status {response.status_code}: {response.text}")
            return False
    except Exception as e:
        print(f"[FAIL] Hugging Face API check failed: {e}")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print(" PROMPTFORGE AI - API CONNECTION DIAGNOSTICS")
    print("=" * 60)
    test_gemini()
    print("-" * 60)
    test_hf()
    print("=" * 60)
