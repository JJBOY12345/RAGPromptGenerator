import sys
import os

# Ensure the root directory is on the python search path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.synthesizer import classify_category

# Force UTF-8 encoding on Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

unseen_test_cases = [
    {"query": "Create a curriculum for Kubernetes containerization", "expected": "Learning"},
    {"query": "Help me become proficient in Rust development", "expected": "Learning"},
    {"query": "Design a training outline for junior database developers", "expected": "Learning"},
    {"query": "Write an email template announcing a database security patch", "expected": "Content Creation"},
    {"query": "Write a blog post about our team's database migration strategy", "expected": "Content Creation"},
    {"query": "Develop an automated script to scan smart contracts for security vulnerabilities", "expected": "Software Development"},
    {"query": "Create a checklist of UI accessibility reviews for a payment system", "expected": "Software Development"},
    {"query": "Conduct research into smart contract security standards", "expected": "Research"}
]

print("=== EVALUATING CLASSIFIER ON UNSEEN QUERIES ===")
passes = 0
for idx, tc in enumerate(unseen_test_cases, 1):
    classified = classify_category(tc["query"])
    result = "PASS" if classified == tc["expected"] else "FAIL"
    if result == "PASS":
        passes += 1
    print(f"{idx}. Query: '{tc['query']}'")
    print(f"   Expected: {tc['expected']:<20} | Classified: {classified:<20} | [{result}]")
    print("-" * 70)

print(f"Unseen Query Accuracy: {passes} / {len(unseen_test_cases)} ({ (passes / len(unseen_test_cases)) * 100.0 }%)")
