import sys
import os

# Ensure the root directory is on the python search path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.retriever import retrieve

# Force UTF-8 encoding on Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

failures = [
    {
        "idx": 12,
        "query": "Build a REST API in Node.js for a shopping cart checkout",
        "expected": "api_design.md"
    },
    {
        "idx": 14,
        "query": "Conduct a security audit on a Solidity smart contract",
        "expected": "security_audit.md"
    },
    {
        "idx": 18,
        "query": "Teach me Kubernetes deployment step-by-step",
        "expected": "tutor_session.md"
    },
    {
        "idx": 19,
        "query": "Create a LinkedIn post about cybersecurity security auditing",
        "expected": "linkedin_post.md"
    },
    {
        "idx": 21,
        "query": "Design a marketing strategy and SWOT analysis for our new database application",
        "expected": "market_analysis.md"
    },
    {
        "idx": 24,
        "query": "Create a checklist for reviewing code security vulnerabilities",
        "expected": "code_review.md"
    }
]

print("=== DEEP RETRIEVAL FAILURE ANALYSIS ===")
for f in failures:
    print("\n" + "=" * 80)
    print(f"CASE {f['idx']}: Query: '{f['query']}'")
    print(f"Expected File: {f['expected']}")
    print("=" * 80)
    
    try:
        results = retrieve(f["query"], top_k=5, unique_documents=True)
        for rank, match in enumerate(results, 1):
            is_expected = "[EXPECTED]" if match["source_document"] == f["expected"] else ""
            print(f"  Rank {rank} {is_expected}")
            print(f"    File       : {match['source_document']}")
            print(f"    Score      : {match['score']}")
            print(f"    Category   : {match['category']}")
            print(f"    Title      : {match.get('title', 'N/A')}")
            # Get first three lines of text content
            excerpt_lines = match['chunk_text'].strip().splitlines()
            clean_lines = [line.strip() for line in excerpt_lines if line.strip()][:3]
            print(f"    Excerpt    :")
            for line in clean_lines:
                print(f"      > {line}")
            print("    " + "-" * 50)
    except Exception as e:
        print(f"  [ERROR] {e}")
