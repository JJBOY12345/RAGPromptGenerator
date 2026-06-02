import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

try:
    print("Listing all available models:")
    for m in genai.list_models():
        if "embedContent" in m.supported_generation_methods:
            print(f" - {m.name} (supports embedContent)")
        else:
            print(f" - {m.name}")
except Exception as e:
    print(f"Failed to list models: {e}")
