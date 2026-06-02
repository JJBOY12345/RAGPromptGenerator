import sys
import os

# Ensure the root directory is on the python search path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.loader import load_documents
from src.chunker import chunk_documents
from src.vector_store import build_vector_store
from src.retriever import retrieve

KB_DIR = "knowledge_base"

def initialize_database():
    """
    Scans the knowledge base, chunks the templates, and writes to ChromaDB.
    """
    print("=" * 60)
    print("[INIT] PROMPTFORGE AI - RAG RETRIEVAL TESTING INITIALIZATION")
    print("=" * 60)
    
    print("1. Scanning local knowledge base...")
    documents = load_documents(KB_DIR)
    print(f"   Found {len(documents)} markdown files.")
    
    print("2. Segmenting documents into semantic sections...")
    chunks = chunk_documents(documents)
    print(f"   Generated {len(chunks)} heading-aware chunks.")
    
    print("3. Indexing chunks inside persistent ChromaDB...")
    total_count = build_vector_store(chunks)
    print(f"   Database populated successfully. Total chunks: {total_count}")
    print("=" * 60 + "\n")

def run_test_scenario(scenario_name: str, query: str):
    """
    Runs a RAG retrieval test scenario and prints visually clean cards.
    """
    print("-" * 60)
    print(f"[SCENARIO] {scenario_name}")
    print(f"   User Query: '{query}'")
    print("-" * 60)
    
    try:
        results = retrieve(query, top_k=3, unique_documents=True)
    except Exception as e:
        print(f"[ERROR] Error during retrieval: {e}")
        return
        
    if not results:
        print("[WARNING] No relevant matches returned.")
        return
        
    for index, match in enumerate(results, 1):
        print(f"\n{index}. [DOC] {match['source_document']}")
        print(f"   Category: {match['category']}")
        print(f"   Score:    {match['score']}")
        print("   --- Snippet ---")
        # Format and truncate chunk text to prevent terminal flooding
        snippet_lines = match['chunk_text'].splitlines()[:5]
        snippet_text = "\n      ".join(snippet_lines)
        print(f"      {snippet_text}")
        if len(match['chunk_text'].splitlines()) > 5:
            print("      ...")
            
    print("\n" + "-" * 60 + "\n")

def main():
    # Verify environment variables exist before running any operations
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if not GEMINI_API_KEY:
        print("[ERROR] CRITICAL CONFIGURATION ERROR:")
        print("   GEMINI_API_KEY not found in environment variables.")
        print("   Please create a '.env' file in this directory containing:")
        print("   GEMINI_API_KEY=your_actual_api_key_here")
        sys.exit(1)
        
    # 1. Initialize and populate database
    try:
        initialize_database()
    except Exception as e:
        print(f"[ERROR] Initialization failed: {e}")
        sys.exit(1)
        
    # 2. Execute Validation Scenarios
    run_test_scenario(
        "Scenario A (Software Development)", 
        "I want to build a hotel booking application"
    )
    
    run_test_scenario(
        "Scenario B (Learning / Tutoring)", 
        "Teach me Linux networking"
    )
    
    run_test_scenario(
        "Scenario C (Content / Copywriting)", 
        "Write a LinkedIn post about RAG"
    )

if __name__ == "__main__":
    main()
