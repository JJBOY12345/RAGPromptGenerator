import hashlib
import re

def split_by_headings(document: dict) -> list:
    """
    Splits a loaded document dict into chunks based on H2 ('## ') headers.
    Keeps headings at the beginning of each chunk to maintain semantic context.
    Adds tags and keywords as requested.
    """
    chunks = []
    content = document["content"]
    source_doc = document["source_document"]
    category = document["category"]
    title = document["title"]
    tags = document["tags"]
    keywords = document["keywords"]
    
    # Split content by heading lines (starting with '## ')
    # Using a regex to find all H2 headings and split by them, keeping headings
    heading_pattern = r"(^|\n)(##\s+.*?)(?=\n##\s+|\n#\s+|$)"
    matches = re.finditer(heading_pattern, content, re.DOTALL)
    
    section_index = 0
    for match in matches:
        chunk_text = match.group(2).strip()
        if not chunk_text:
            continue
            
        # Extract the heading title for hashing and metadata
        heading_line = chunk_text.splitlines()[0]
        heading_title = heading_line.replace("##", "").strip()
        
        # Generate unique stable chunk ID using MD5 hash of source and heading index
        hash_input = f"{source_doc}_{section_index}_{heading_title}"
        chunk_id = hashlib.md5(hash_input.encode("utf-8")).hexdigest()
        
        chunks.append({
            "chunk_id": chunk_id,
            "source_document": source_doc,
            "category": category,
            "title": title,
            "tags": tags,
            "retrieval_keywords": keywords,
            "content": chunk_text
        })
        section_index += 1
        
    # Fallback: if no H2 headings are found, treat the entire document as a single chunk
    if not chunks and content.strip():
        chunk_id = hashlib.md5(f"{source_doc}_full".encode("utf-8")).hexdigest()
        chunks.append({
            "chunk_id": chunk_id,
            "source_document": source_doc,
            "category": category,
            "title": title,
            "tags": tags,
            "retrieval_keywords": keywords,
            "content": content.strip()
        })
        
    return chunks

def chunk_documents(documents: list) -> list:
    """
    Iterates over a list of documents and returns all generated chunks.
    """
    all_chunks = []
    for doc in documents:
        chunks = split_by_headings(doc)
        all_chunks.extend(chunks)
    return all_chunks
