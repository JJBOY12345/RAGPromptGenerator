import os
import time
import chromadb
from src.embeddings import get_embeddings_batch, get_active_embedding_model

CHROMA_PATH = "chroma_db"

def get_chroma_client():
    """
    Returns a persistent ChromaDB client.
    """
    return chromadb.PersistentClient(path=CHROMA_PATH)

def get_collection(client):
    """
    Returns (or creates) the promptforge_kb collection with cosine similarity configuration.
    Performs a dynamic fail-fast check comparing the configured EMBEDDING_MODEL in .env
    against the index metadata to prevent embedding space mismatch corruption.
    """
    collection = client.get_or_create_collection(
        name="promptforge_kb",
        metadata={"hnsw:space": "cosine"}
    )
    
    # Dynamic fail-fast check
    active_model = get_active_embedding_model()
    metadata = collection.metadata or {}
    stored_model = metadata.get("embedding_model")
    
    if not stored_model:
        # Save it to the collection metadata
        # Only modify the embedding_model key to avoid changing 'hnsw:space' or other read-only keys
        new_metadata = dict(metadata)
        new_metadata["embedding_model"] = active_model
        try:
            collection.modify(metadata={"embedding_model": active_model})
        except Exception as e:
            print(f"Warning: Failed to modify collection metadata: {e}")
    elif stored_model != active_model:
        raise ValueError(
            f"\n[CRITICAL ERROR] EMBEDDING MODEL MISMATCH DETECTED!\n"
            f"--------------------------------------------------\n"
            f"The persistent vector database ('chroma_db') was built using model:\n"
            f"  --> '{stored_model}'\n"
            f"However, your current environment is configured to use:\n"
            f"  --> '{active_model}'\n\n"
            f"Reason: Mixing different embedding models corrupts vector space relationships and invalidates similarity search scores.\n"
            f"Resolution: To use '{active_model}', you must manually delete the persistent database folder ('chroma_db/') and trigger a full reindex."
        )
        
    return collection

def build_vector_store(chunks: list):
    """
    Populates ChromaDB with chunks. 
    Verifies existing chunk IDs to prevent duplicate embedding runs and unnecessary API calls.
    Respects Gemini Free Tier API rate limits (max 100 requests per minute) using paced batching.
    """
    client = get_chroma_client()
    collection = get_collection(client)
    
    # 1. Fetch existing IDs in the collection for deduplication
    try:
        existing_data = collection.get()
        existing_ids = set(existing_data["ids"]) if existing_data else set()
    except Exception as e:
        print(f"Warning: Failed to fetch existing collection data: {e}")
        existing_ids = set()
        
    # 2. Filter out already indexed chunks
    new_chunks = [c for c in chunks if c["chunk_id"] not in existing_ids]
    
    if not new_chunks:
        print("Vector database is up-to-date. No new embeddings generated.")
        return len(existing_ids)
        
    print(f"Generating embeddings for {len(new_chunks)} new chunks...")
    
    # 3. Process new chunks in paced batches of 80 to stay under the 100 requests/minute limit
    batch_size = 80
    total_new = len(new_chunks)
    
    for i in range(0, total_new, batch_size):
        end_idx = min(i + batch_size, total_new)
        batch = new_chunks[i:end_idx]
        
        print(f"   -> Processing batch {i // batch_size + 1}/{(total_new + batch_size - 1) // batch_size} (chunks {i + 1} to {end_idx})...")
        
        # Extract documents and generate batch embeddings
        documents = [c["content"] for c in batch]
        embeddings = get_embeddings_batch(documents)
        
        ids = [c["chunk_id"] for c in batch]
        
        # Convert lists to comma-separated strings to maintain Chroma compatibility
        metadatas = []
        for c in batch:
            metadatas.append({
                "source_document": c["source_document"],
                "category": c["category"],
                "title": c["title"],
                "tags": ", ".join(c["tags"]),
                "retrieval_keywords": ", ".join(c["retrieval_keywords"])
            })
            
        # Add batch to Chroma DB
        collection.add(
            ids=ids,
            embeddings=embeddings,
            metadatas=metadatas,
            documents=documents
        )
        
        # If there are more batches remaining, sleep 65 seconds to clear the per-minute API limit
        if end_idx < total_new:
            print("   -> Rate-limit cooldown: Sleeping for 65 seconds to reset the per-minute API quota...")
            time.sleep(65)
            
    total_count = len(existing_ids) + total_new
    print(f"Success! Vector database now contains {total_count} chunks.")
    return total_count
