import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import src.synthesizer as synth
from run_synthesis_tests import SYNTHESIS_QUERIES

print("# Knowledge Utilization Mapping\n")
for idx, q in enumerate(SYNTHESIS_QUERIES, 1):
    category = synth.classify_category(q["query"])
    retrieved_items = synth.retrieve(
        q["query"], 
        top_k=3, 
        unique_documents=True,
        classified_category=category,
        routing_strategy="boost"
    )
    print(f"### Query {idx}: {q['query']}")
    print(f"* **Classified Category**: {category}")
    print("* **Retrieved Documents**:")
    for item in retrieved_items:
        print(f"  - `{item['source_document']}` (Score: {item['score']})")
    print()
