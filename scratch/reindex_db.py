import os
import sys
import shutil

# Ensure the root directory is on the python search path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.loader import load_documents
from src.chunker import chunk_documents
from src.vector_store import build_vector_store

KB_DIR = "knowledge_base"
CHROMA_DIR = "chroma_db"

def main():
    print("=" * 80)
    print(" PROMPTFORGE AI - REINDEXING VECTOR STORAGE")
    print("=" * 80)
    
    # 1. Clear old Chroma DB directory to remove stale fragmented chunks
    if os.path.exists(CHROMA_DIR):
        print(f"Removing old vector database at '{CHROMA_DIR}'...")
        shutil.rmtree(CHROMA_DIR)
        print("Old database cleared successfully.")
    else:
        print("No existing vector database folder found. Starting fresh.")
        
    # 2. Load documents
    print("Loading documents from knowledge base...")
    documents = load_documents(KB_DIR)
    print(f"Loaded {len(documents)} source files.")
    
    # 3. Chunk documents using new Hybrid Adaptive Chunker
    print("Chunking documents (Hybrid Adaptive)...")
    chunks = chunk_documents(documents)
    print(f"Generated {len(chunks)} chunks.")
    
    # 4. Rebuild vector store
    print("Building vector database...")
    total_chunks = build_vector_store(chunks)
    print(f"Success! Vector database successfully rebuilt with {total_chunks} chunks.")
    print("=" * 80 + "\n")

if __name__ == "__main__":
    main()
