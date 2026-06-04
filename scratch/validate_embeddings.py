import os
import sys

# Ensure the root directory is on the python search path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.vector_store import get_chroma_client, get_collection

def main():
    print("=" * 80)
    print(" PROMPTFORGE AI - VECTOR STORAGE INTEGRITY CHECK")
    print("=" * 80)
    
    client = get_chroma_client()
    collection = get_collection(client)
    
    # Fetch all records with embeddings included
    try:
        data = collection.get(include=["embeddings", "metadatas", "documents"])
    except Exception as e:
        print(f"[ERROR] Failed to fetch data from collection: {e}")
        sys.exit(1)
        
    ids = data.get("ids", [])
    embeddings = data.get("embeddings", [])
    metadatas = data.get("metadatas", [])
    documents = data.get("documents", [])
    
    print(f"Total Chunks Found in DB: {len(ids)}")
    
    # 1. Assert chunk count
    if len(ids) != 63:
        print(f"[FAIL] Expected exactly 63 chunks, but found {len(ids)}.")
        sys.exit(1)
    else:
        print("[PASS] Chunk count matches expected 63 chunks.")
        
    # 2. Check embedding list size matches
    if embeddings is None or len(embeddings) == 0:
        print("[FAIL] No embeddings returned from database.")
        sys.exit(1)
        
    if len(embeddings) != len(ids):
        print(f"[FAIL] Mismatch: {len(ids)} chunks but only {len(embeddings)} embeddings stored.")
        sys.exit(1)
    else:
        print("[PASS] Embeddings count matches chunk count.")
        
    # 3. Validate dimension and non-zero contents
    mismatched_dimensions = 0
    zero_vectors = 0
    null_vectors = 0
    expected_dim = 3072
    
    for idx, (chunk_id, vector) in enumerate(zip(ids, embeddings)):
        if vector is None:
            null_vectors += 1
            continue
            
        dim = len(vector)
        if dim != expected_dim:
            mismatched_dimensions += 1
            print(f"  -> Chunk {chunk_id} has dimension {dim} (Expected: {expected_dim})")
            
        # Check if vector is all zeroes
        is_all_zero = all(val == 0.0 for val in vector)
        if is_all_zero:
            zero_vectors += 1
            
    if null_vectors > 0:
        print(f"[FAIL] Found {null_vectors} NULL vectors in database.")
    else:
        print("[PASS] No NULL vectors found.")
        
    if mismatched_dimensions > 0:
        print(f"[FAIL] Found {mismatched_dimensions} vectors with wrong dimensions.")
    else:
        print(f"[PASS] All embedding vectors are exactly dimension {expected_dim}.")
        
    if zero_vectors > 0:
        print(f"[FAIL] Found {zero_vectors} zero-vectors in database.")
    else:
        print("[PASS] No zero-vectors found.")
        
    if null_vectors == 0 and mismatched_dimensions == 0 and zero_vectors == 0:
        print("\n>>> ALL VECTOR DB INTEGRITY CHECKS PASSED SUCCESSFULLY! <<<\n")
        sys.exit(0)
    else:
        print("\n>>> INTEGRITY CHECKS FAILED! <<<\n")
        sys.exit(1)

if __name__ == "__main__":
    main()
