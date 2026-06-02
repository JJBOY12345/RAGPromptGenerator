import os
import sys

# Ensure the root directory is on the python search path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv
load_dotenv()

# Force PRIMARY_GENERATION_PROVIDER=huggingface
os.environ["PRIMARY_GENERATION_PROVIDER"] = "huggingface"

from src.synthesizer import generate_prompt

# Ensure output is UTF-8 encoded
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

query = "Design a study plan for learning cybersecurity"
print("=" * 80)
print(f"Executing generate_prompt for: '{query}'")
print(f"Primary Provider: {os.environ.get('PRIMARY_GENERATION_PROVIDER')}")
print("=" * 80)

try:
    result = generate_prompt(query)

    print("\n" + "=" * 80)
    print("AUDIT RESULTS")
    print("=" * 80)
    print(f"Category: {result['category']}")
    print("\nRetrieved Sources:")
    for idx, src in enumerate(result['retrieved_sources'], 1):
        print(f"  {idx}. {src['source_document']} (Score: {src['score']})")

    print("\nGenerated Prompt:")
    print(result['generated_prompt'])
    print("=" * 80)
except Exception as e:
    print(f"\n[ERROR] Synthesis failed: {e}")
    import traceback
    traceback.print_exc()
