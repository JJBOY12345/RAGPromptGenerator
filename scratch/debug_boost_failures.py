import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from run_retrieval_tests import GOLDEN_QUERIES
from src.retriever import retrieve
from src.synthesizer import classify_category

def main():
    failures = []
    for idx, q in enumerate(GOLDEN_QUERIES, 1):
        query_text = q["query"]
        classified = classify_category(query_text)
        results = retrieve(
            query_text, 
            top_k=3, 
            unique_documents=True, 
            classified_category=classified, 
            routing_strategy="boost"
        )
        retrieved_files = [item["source_document"] for item in results]
        
        case_rank = 4
        if q["expected_document"] in retrieved_files:
            case_rank = retrieved_files.index(q["expected_document"]) + 1
            
        if case_rank != 1:
            failures.append((idx, query_text, q["expected_document"], case_rank, retrieved_files))

    print(f"Total Boost failures: {len(failures)}")
    for idx, query, expected, rank, retrieved in failures:
        print(f"{idx}. Query: \"{query}\"")
        print(f"   Expected: {expected}")
        print(f"   Rank: {rank}")
        print(f"   Retrieved List: {retrieved}")
        print("-" * 50)

if __name__ == "__main__":
    main()
