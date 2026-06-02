from src.embeddings import get_embedding
from src.vector_store import get_chroma_client, get_collection

def retrieve(query: str, top_k: int = 5, unique_documents: bool = False) -> list:
    """
    Accepts a user query, generates its embedding, searches ChromaDB,
    and returns the top_k most relevant knowledge documents with similarity scores.
    If unique_documents is True, returns only the highest-scoring chunk per source document.
    """
    client = get_chroma_client()
    collection = get_collection(client)
    
    # 1. Embed query
    query_embedding = get_embedding(query, is_query=True)
    
    # 2. Determine fetch size from Chroma
    # If deduplicating, fetch more candidates so we can return exactly top_k unique docs
    fetch_k = max(top_k * 3, 15) if unique_documents else top_k
    
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=fetch_k
    )
    
    retrieved_items = []
    
    # Check if there are any results
    if not results or not results["ids"] or not results["ids"][0]:
        return retrieved_items
        
    ids = results["ids"][0]
    distances = results["distances"][0]
    metadatas = results["metadatas"][0]
    documents = results["documents"][0]
    
    seen_documents = set()
    
    for i in range(len(ids)):
        meta = metadatas[i]
        source_doc = meta.get("source_document", "unknown")
        
        # Deduplication check
        if unique_documents:
            if source_doc in seen_documents:
                continue
            seen_documents.add(source_doc)
            
        # Convert cosine distance to cosine similarity score
        score = round(1.0 - distances[i], 4)
        
        # Build strict returned dict model as specified in requirements
        retrieved_items.append({
            "score": score,
            "source_document": source_doc,
            "category": meta.get("category", "unknown"),
            "chunk_text": documents[i],
            # Auxiliary fields for debugging
            "title": meta.get("title", ""),
            "tags": meta.get("tags", ""),
            "retrieval_keywords": meta.get("retrieval_keywords", "")
        })
        
        # Limit to top_k unique documents
        if unique_documents and len(retrieved_items) >= top_k:
            break
            
    return retrieved_items
