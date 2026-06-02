import os
import re
import yaml

def load_documents(kb_dir: str) -> list:
    """
    Recursively scans the kb_dir for markdown files, extracts YAML frontmatter
    and document bodies, and returns a list of document dicts.
    """
    documents = []
    
    if not os.path.exists(kb_dir):
        print(f"Warning: Directory {kb_dir} does not exist.")
        return documents

    for root, _, files in os.walk(kb_dir):
        # Determine current category from the folder name
        category_folder = os.path.basename(root)
        
        for file in files:
            if not file.endswith(".md"):
                continue
                
            file_path = os.path.join(root, file)
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
            except Exception as e:
                print(f"Error reading file {file_path}: {e}")
                continue
                
            # Parse YAML frontmatter bounded by ---
            match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
            if not match:
                print(f"Warning: Missing or invalid frontmatter in {file_path}")
                continue
                
            frontmatter_text = match.group(1)
            body_content = content[match.end():].strip()
            
            try:
                metadata = yaml.safe_load(frontmatter_text) or {}
            except Exception as e:
                print(f"Error parsing frontmatter in {file_path}: {e}")
                continue
                
            # Extract attributes from metadata
            title = metadata.get("title", os.path.splitext(file)[0].replace("_", " ").title())
            # Default category to category_folder if missing in frontmatter
            category = metadata.get("category", category_folder)
            tags = metadata.get("tags", [])
            if not isinstance(tags, list):
                tags = [tags] if tags else []
                
            keywords = metadata.get("retrieval_keywords", metadata.get("keywords", []))
            if not isinstance(keywords, list):
                keywords = [keywords] if keywords else []
                
            documents.append({
                "title": title,
                "category": category,
                "tags": tags,
                "keywords": keywords,
                "content": body_content,
                "source_document": file
            })
            
    return documents
