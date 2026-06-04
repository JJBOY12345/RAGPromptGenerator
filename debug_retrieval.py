import sys
import os

# Ensure the root directory is on the python search path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.retriever import retrieve
from src.synthesizer import classify_category

# Force UTF-8 encoding on Windows to prevent UnicodeEncodeError
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def main():
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
    else:
        query = input("Enter query to debug: ").strip()
        
    if not query:
        print("[ERROR] Query cannot be empty.")
        sys.exit(1)
        
    print("\n" + "=" * 80)
    print(f" DEBUG RETRIEVAL & CLASSIFICATION")
    print("=" * 80)
    print(f"Input Query: '{query}'")
    
    # 1. Classification
    category = classify_category(query)
    print(f"Classified Category: {category}")
    print("-" * 80)
    
    # 2. Retrieval
    print("Retrieved Document Chunks (Top-5 unique documents):")
    try:
        results = retrieve(query, top_k=5, unique_documents=True)
        if not results:
            print("   [WARNING] No matches returned from ChromaDB.")
        else:
            for idx, item in enumerate(results, 1):
                print(f"\n  {idx}. [DOC] {item['source_document']}")
                print(f"     Similarity Score: {item['score']}")
                print(f"     Folder Category : {item['category']}")
                print(f"     Title           : {item.get('title', 'N/A')}")
                
                # Show first two lines of excerpt
                excerpt_lines = item['chunk_text'].strip().splitlines()
                clean_lines = [line.strip() for line in excerpt_lines if line.strip()]
                excerpt_preview = " | ".join(clean_lines[:2])
                if len(excerpt_preview) > 120:
                    excerpt_preview = excerpt_preview[:117] + "..."
                print(f"     Excerpt Excerpt : \"{excerpt_preview}\"")
                print("     " + "-" * 50)
    except Exception as e:
        print(f"   [ERROR] Retrieval failed with exception: {e}")
        
    print("\n" + "=" * 80 + "\n")

if __name__ == "__main__":
    main()
