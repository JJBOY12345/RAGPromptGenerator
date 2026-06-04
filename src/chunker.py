import hashlib
import re

def split_by_headings(document: dict) -> list:
    """
    Splits a loaded document dict into chunks using a Hybrid Adaptive Chunking strategy:
    - Small template files (< 2,500 chars) are stored intact as single chunks to preserve identity.
    - Large reference files (>= 2,500 chars) are grouped into semantic blocks of H2 sections
      (target: 1,500 - 2,500 characters) to avoid fragmentation while keeping search granular.
    """
    chunks = []
    content = document["content"].strip()
    source_doc = document["source_document"]
    category = document["category"]
    title = document["title"]
    tags = document["tags"]
    keywords = document["keywords"]
    
    if not content:
        return chunks
        
    # Hybrid Strategy: Keep small template files completely whole
    if len(content) < 2500:
        chunk_id = hashlib.md5(f"{source_doc}_full".encode("utf-8")).hexdigest()
        chunks.append({
            "chunk_id": chunk_id,
            "source_document": source_doc,
            "category": category,
            "title": title,
            "tags": tags,
            "retrieval_keywords": keywords,
            "content": content
        })
        return chunks
        
    # Large files: Scan and group H2 sections semantically
    heading_pattern = r"(^|\n)(##\s+.*?)(?=\n##\s+|\n#\s+|$)"
    matches = list(re.finditer(heading_pattern, content, re.DOTALL))
    
    if not matches:
        # Fallback: No H2 headings in large file
        chunk_id = hashlib.md5(f"{source_doc}_full".encode("utf-8")).hexdigest()
        chunks.append({
            "chunk_id": chunk_id,
            "source_document": source_doc,
            "category": category,
            "title": title,
            "tags": tags,
            "retrieval_keywords": keywords,
            "content": content
        })
        return chunks
        
    # Group sections up to a limit of 2,500 characters
    current_chunk_parts = []
    current_chunk_len = 0
    current_titles = []
    section_index = 0
    
    for match in matches:
        chunk_text = match.group(2).strip()
        if not chunk_text:
            continue
            
        # Get heading title for stable IDs
        heading_line = chunk_text.splitlines()[0]
        heading_title = heading_line.replace("##", "").strip()
        
        # If adding this heading section exceeds 2,500 characters, emit the current block first
        if current_chunk_parts and (current_chunk_len + len(chunk_text) > 2500):
            joined_content = "\n\n".join(current_chunk_parts)
            titles_key = "_".join(current_titles)
            hash_input = f"{source_doc}_{section_index}_{titles_key}"
            chunk_id = hashlib.md5(hash_input.encode("utf-8")).hexdigest()
            
            chunks.append({
                "chunk_id": chunk_id,
                "source_document": source_doc,
                "category": category,
                "title": title,
                "tags": tags,
                "retrieval_keywords": keywords,
                "content": joined_content
            })
            
            # Reset values
            current_chunk_parts = [chunk_text]
            current_chunk_len = len(chunk_text)
            current_titles = [heading_title]
            section_index += 1
        else:
            current_chunk_parts.append(chunk_text)
            current_chunk_len += len(chunk_text) + 2 # account for double newline separator
            current_titles.append(heading_title)
            
    # Emit final remaining chunk
    if current_chunk_parts:
        joined_content = "\n\n".join(current_chunk_parts)
        titles_key = "_".join(current_titles)
        hash_input = f"{source_doc}_{section_index}_{titles_key}"
        chunk_id = hashlib.md5(hash_input.encode("utf-8")).hexdigest()
        
        chunks.append({
            "chunk_id": chunk_id,
            "source_document": source_doc,
            "category": category,
            "title": title,
            "tags": tags,
            "retrieval_keywords": keywords,
            "content": joined_content
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
