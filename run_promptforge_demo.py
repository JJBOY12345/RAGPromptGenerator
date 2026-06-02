import sys
import os
import time

# Ensure the root directory is on the python search path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.synthesizer import generate_prompt

def run_scenario(index: int, query: str):
    print("=" * 80)
    print(f" SCENARIO {index}: '{query}'")
    print("=" * 80)
    
    try:
        result = generate_prompt(query)
    except Exception as e:
        print(f"[ERROR] Synthesis failed: {e}")
        print("=" * 80 + "\n")
        return
        
    print(f"[*] Detected Category: {result['category']}")
    print("\n[*] Retrieved Sources & Explanations:")
    
    for idx, src in enumerate(result['retrieved_sources'], 1):
        print(f"  {idx}. [DOC] {src['source_document']}")
        print(f"     Category: {src['category']}")
        print(f"     Score:    {src['score']}")
        # Extract a clean, brief snippet of matched_excerpt for visual presentation
        excerpt_lines = src['matched_excerpt'].strip().splitlines()
        excerpt_preview = " ".join([line.strip() for line in excerpt_lines if line.strip()][:2])
        if len(excerpt_preview) > 150:
            excerpt_preview = excerpt_preview[:147] + "..."
        print(f"     Reason (Snippet): \"{excerpt_preview}\"")
        print("     " + "-" * 50)
        
    print("\n" + "=" * 80)
    print(" SYNTHESIZED EXPERT PROMPT")
    print("=" * 80)
    print(result['generated_prompt'])
    print("=" * 80 + "\n\n")

def main():
    # Force UTF-8 encoding on Windows to prevent UnicodeEncodeError
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
        
    # 1. Fail-fast Environment Validation
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if not GEMINI_API_KEY:
        print("[ERROR] CRITICAL CONFIGURATION ERROR:")
        print("   GEMINI_API_KEY not found in environment variables.")
        print("   Please create a '.env' file in this directory containing:")
        print("   GEMINI_API_KEY=your_actual_api_key_here")
        sys.exit(1)
        
    # 2. Check if custom user argument is provided
    if len(sys.argv) > 1:
        custom_query = " ".join(sys.argv[1:])
        print(f"[INFO] Running custom synthesis for query: '{custom_query}'")
        run_scenario(1, custom_query)
        return

    # 3. Default: Execute sequence of 5 target validation queries
    print("=" * 80)
    print(" PROMPTFORGE AI - PHASE 2B PROMPT SYNTHESIS ENGINE DEMONSTRATION")
    print("=" * 80 + "\n")
    
    validation_queries = [
        "I want to build a hotel booking application",
        "Teach me Linux networking",
        "Write a LinkedIn post about RAG",
        "Create a luxury product advertisement",
        "Design a study plan for learning cybersecurity"
    ]
    
    for idx, query in enumerate(validation_queries, 1):
        run_scenario(idx, query)
        if idx < len(validation_queries):
            print(f"[INFO] Sleeping 15 seconds to respect Gemini API rate limits...")
            time.sleep(15)
        
if __name__ == "__main__":
    main()
