import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.embeddings import get_embeddings_batch

texts = [
    "This is document 1",
    "This is document 2",
    "This is document 3"
]

print("Calling get_embeddings_batch...")
try:
    embs = get_embeddings_batch(texts)
    print(f"Type of embs: {type(embs)}")
    print(f"Length of embs: {len(embs)}")
    if len(embs) > 0:
        print(f"Type of first element: {type(embs[0])}")
        print(f"Length of first element: {len(embs[0])}")
except Exception as e:
    print(f"Error: {e}")
