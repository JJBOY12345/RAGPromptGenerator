from src.embeddings import get_embedding
from src.vector_store import get_chroma_client, get_collection

def map_classifier_to_db_categories(classified_category: str) -> list:
    """
    Maps a high-level classified category to the folder categories in document metadata.
    """
    mapping = {
        "Software Development": ["software_development", "uiux_design", "data_analysis"],
        "Learning": ["learning"],
        "Content Creation": ["content_creation", "business"],
        "Research": ["research"],
        "Image Generation": ["image_generation"],
        "Business Strategy": ["business"]
    }
    return mapping.get(classified_category, [])

def retrieve(
    query: str,
    top_k: int = 5,
    unique_documents: bool = False,
    classified_category: str = None,
    routing_strategy: str = "none"
) -> list:
    """
    Accepts a user query, generates its embedding, searches ChromaDB,
    and returns the top_k most relevant knowledge documents with similarity scores.
    Supports routing_strategy = "none", "filter", or "boost" using classified_category.
    If unique_documents is True, returns only the highest-scoring chunk per source document.
    """
    client = get_chroma_client()
    collection = get_collection(client)
    
    # 1. Embed query
    query_embedding = get_embedding(query, is_query=True)
    
    # 2. Determine fetch size from Chroma
    fetch_k = max(top_k * 3, 15) if unique_documents else top_k
    
    # Define metadata filters
    where_filter = None
    db_categories = []
    allowed_categories = []
    
    if classified_category and routing_strategy != "none":
        db_categories = map_classifier_to_db_categories(classified_category)
        allowed_categories = db_categories + ["_frameworks"]
        
    if routing_strategy == "filter" and allowed_categories:
        where_filter = {"category": {"$in": allowed_categories}}
        
    # 3. Query ChromaDB
    query_args = {
        "query_embeddings": [query_embedding],
        "n_results": fetch_k
    }
    if where_filter:
        query_args["where"] = where_filter
        
    results = collection.query(**query_args)
    
    retrieved_items = []
    
    # Check if there are any results
    if not results or not results["ids"] or not results["ids"][0]:
        return retrieved_items
        
    ids = results["ids"][0]
    distances = results["distances"][0]
    metadatas = results["metadatas"][0]
    documents = results["documents"][0]
    
    raw_items = []
    
    for i in range(len(ids)):
        meta = metadatas[i]
        source_doc = meta.get("source_document", "unknown")
        
        # Convert cosine distance to cosine similarity score
        score = round(1.0 - distances[i], 4)
        
        # Apply score boost if strategy is boost
        if routing_strategy == "boost" and allowed_categories:
            if meta.get("category") in allowed_categories:
                # Add category bonus
                score = round(score + 0.10, 4)
                
        raw_items.append({
            "score": score,
            "source_document": source_doc,
            "category": meta.get("category", "unknown"),
            "chunk_text": documents[i],
            # Auxiliary fields for debugging
            "title": meta.get("title", ""),
            "tags": meta.get("tags", ""),
            "retrieval_keywords": meta.get("retrieval_keywords", "")
        })
        
    # Sort raw items by score descending (important for boost/filtering re-rankings)
    raw_items.sort(key=lambda x: x["score"], reverse=True)
    
    # Deduplicate and slice to top_k
    seen_documents = set()
    for item in raw_items:
        source_doc = item["source_document"]
        
        # Deduplication check
        if unique_documents:
            if source_doc in seen_documents:
                continue
            seen_documents.add(source_doc)
            
        retrieved_items.append(item)
        
        # Limit to top_k unique documents
        if len(retrieved_items) >= top_k:
            break
            
    return retrieved_items
