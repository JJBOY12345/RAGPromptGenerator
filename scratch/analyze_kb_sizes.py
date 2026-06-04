import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.loader import load_documents

kb_dir = "knowledge_base"
documents = load_documents(kb_dir)

print(f"=== Knowledge Base Size Analysis ===")
print(f"Total documents: {len(documents)}")
print("-" * 50)

sizes = []
for doc in documents:
    content = doc["content"]
    char_len = len(content)
    word_count = len(content.split())
    est_tokens = char_len // 4
    # Count H2 headings
    h2_headings = [line for line in content.splitlines() if line.strip().startswith("## ")]
    sizes.append({
        "file": doc["source_document"],
        "chars": char_len,
        "words": word_count,
        "tokens": est_tokens,
        "h2_count": len(h2_headings)
    })

# Sort by character length descending
sizes.sort(key=lambda x: x["chars"], reverse=True)

for idx, s in enumerate(sizes, 1):
    print(f"{idx:2d}. {s['file']:<30} | {s['chars']:4d} chars | {s['words']:4d} words | ~{s['tokens']:3d} tokens | {s['h2_count']} H2s")

print("-" * 50)
avg_chars = sum(s["chars"] for s in sizes) / len(sizes)
print(f"Average Document Size: {avg_chars:.1f} chars (~{int(avg_chars//4)} tokens)")
print(f"Largest Document:      {sizes[0]['file']} ({sizes[0]['chars']} chars, ~{sizes[0]['tokens']} tokens)")
print(f"Smallest Document:     {sizes[-1]['file']} ({sizes[-1]['chars']} chars, ~{sizes[-1]['tokens']} tokens)")
