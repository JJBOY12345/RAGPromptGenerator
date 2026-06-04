import sys
import os
import time

# Ensure the root directory is on the python search path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.retriever import retrieve
from src.synthesizer import classify_category

# Force UTF-8 encoding on Windows to prevent UnicodeEncodeError
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# The 50 Golden Validation Queries
GOLDEN_QUERIES = [
    # --- Learning Queries (5) ---
    {
        "query": "Teach me how closures work in JavaScript using the Socratic method",
        "target_category": "Learning",
        "expected_document": "tutor_session.md"
    },
    {
        "query": "Help me understand relational database transactions step-by-step",
        "target_category": "Learning",
        "expected_document": "tutor_session.md"
    },
    {
        "query": "Explain the concept of quantum superposition with a Metaphorical Analogy",
        "target_category": "Learning",
        "expected_document": "concept_explainer.md"
    },
    {
        "query": "Create an interactive quiz to test my understanding of Python decorators",
        "target_category": "Learning",
        "expected_document": "quiz_generator.md"
    },
    {
        "query": "Design a 6-week curriculum for learning machine learning basics",
        "target_category": "Learning",
        "expected_document": "study_plan.md"
    },
    
    # --- Content Creation Queries (5) ---
    {
        "query": "Write a LinkedIn post about how to start learning prompt engineering",
        "target_category": "Content Creation",
        "expected_document": "linkedin_post.md"
    },
    {
        "query": "Draft a technical blog explaining the difference between SQL and NoSQL",
        "target_category": "Content Creation",
        "expected_document": "technical_blog.md"
    },
    {
        "query": "Write an executive memo explaining our Q3 engineering goals",
        "target_category": "Content Creation",
        "expected_document": "executive_summary.md"
    },
    {
        "query": "Generate a 5-post promotional campaign for launching our developer portal",
        "target_category": "Content Creation",
        "expected_document": "social_media_campaign.md"
    },
    {
        "query": "Write api documentation for user profile endpoints",
        "target_category": "Content Creation",
        "expected_document": "documentation.md"
    },
    
    # --- Software Development Queries (5) ---
    {
        "query": "Create a PostgreSQL schema for a user authentication database",
        "target_category": "Software Development",
        "expected_document": "database_design.md"
    },
    {
        "query": "Build a REST API in Node.js for a shopping cart checkout",
        "target_category": "Software Development",
        "expected_document": "api_design.md"
    },
    {
        "query": "Write unit tests for a Python payment service",
        "target_category": "Software Development",
        "expected_document": "testing_strategy.md"
    },
    {
        "query": "Conduct a security audit on a Solidity smart contract",
        "target_category": "Software Development",
        "expected_document": "security_audit.md"
    },
    {
        "query": "Perform a code review on this Python directory scanner script",
        "target_category": "Software Development",
        "expected_document": "code_review.md"
    },
    
    # --- Mixed / Ambiguous Intent Queries (11) ---
    {
        "query": "Design a study plan for learning Rust programming",
        "target_category": "Learning",
        "expected_document": "study_plan.md"
    },
    {
        "query": "Create a technical blog outline about vector databases",
        "target_category": "Content Creation",
        "expected_document": "technical_blog.md"
    },
    {
        "query": "Teach me Kubernetes deployment step-by-step",
        "target_category": "Learning",
        "expected_document": "tutor_session.md"
    },
    {
        "query": "Create a LinkedIn post about cybersecurity security auditing",
        "target_category": "Content Creation",
        "expected_document": "linkedin_post.md"
    },
    {
        "query": "Write a guide explaining neural networks to beginners with analogies",
        "target_category": "Learning",
        "expected_document": "concept_explainer.md"
    },
    {
        "query": "Design a marketing strategy and SWOT analysis for our new database application",
        "target_category": "Business Strategy",
        "expected_document": "market_analysis.md"
    },
    {
        "query": "Conduct literature review on transformer models in academic papers",
        "target_category": "Research",
        "expected_document": "literature_review.md"
    },
    {
        "query": "Generate a prompt for a photorealistic brand illustration of a laptop",
        "target_category": "Image Generation",
        "expected_document": "brand_illustration.md"
    },
    {
        "query": "Create a checklist for reviewing code security vulnerabilities",
        "target_category": "Software Development",
        "expected_document": "code_review.md"
    },
    {
        "query": "Design a wireframe specification for a tutoring application",
        "target_category": "Software Development",
        "expected_document": "wireframe_specification.md"
    },
    {
        "query": "Generate user research interview questions for shopping app checkout experience",
        "target_category": "Software Development",
        "expected_document": "user_research.md"
    },

    # --- New Target-Topic Challenge Queries (24) ---
    {
        "query": "Create a blog post about Kubernetes security",
        "target_category": "Content Creation",
        "expected_document": "technical_blog.md"
    },
    {
        "query": "Write LinkedIn content explaining API versioning",
        "target_category": "Content Creation",
        "expected_document": "linkedin_post.md"
    },
    {
        "query": "Teach me PostgreSQL indexing",
        "target_category": "Learning",
        "expected_document": "tutor_session.md"
    },
    {
        "query": "Design a learning curriculum for Docker",
        "target_category": "Learning",
        "expected_document": "study_plan.md"
    },
    {
        "query": "Create marketing messaging for an AI platform",
        "target_category": "Content Creation",
        "expected_document": "social_media_campaign.md"
    },
    {
        "query": "Draft a product requirements document (PRD) for our new mobile app",
        "target_category": "Business Strategy",
        "expected_document": "product_requirements.md"
    },
    {
        "query": "Draft an email response to handle a customer service escalation",
        "target_category": "Business Strategy",
        "expected_document": "email_communication.md"
    },
    {
        "query": "Perform a competitive analysis of top cloud hosting providers",
        "target_category": "Research",
        "expected_document": "competitive_analysis.md"
    },
    {
        "query": "Design a dashboard layout for tracking e-commerce sales metrics",
        "target_category": "Software Development",
        "expected_document": "dashboard_design.md"
    },
    {
        "query": "Create a plan for exploratory data analysis on user signup datasets",
        "target_category": "Software Development",
        "expected_document": "exploratory_analysis.md"
    },
    {
        "query": "Write a data insight report summarizing website traffic drops",
        "target_category": "Software Development",
        "expected_document": "insight_report.md"
    },
    {
        "query": "Conduct an accessibility review of our web portal login form",
        "target_category": "Software Development",
        "expected_document": "accessibility_review.md"
    },
    {
        "query": "Create a design system specification for buttons and typography",
        "target_category": "Software Development",
        "expected_document": "product_design_system.md"
    },
    {
        "query": "Generate a prompt for commercial product photography of running shoes",
        "target_category": "Image Generation",
        "expected_document": "product_photography.md"
    },
    {
        "query": "Create a prompt for a professional headshot portrait of a CEO",
        "target_category": "Image Generation",
        "expected_document": "professional_portrait.md"
    },
    {
        "query": "Create a prompt for a modern mobile app dashboard UI mockup visual",
        "target_category": "Image Generation",
        "expected_document": "ui_mockup_visual.md"
    },
    {
        "query": "Generate a LaTeX Beamer presentation template for a scientific paper",
        "target_category": "Research",
        "expected_document": "latex_beamer_example.md"
    },
    {
        "query": "Conduct a subject matter expert deep dive into zero-knowledge proofs",
        "target_category": "Research",
        "expected_document": "topic_deep_dive.md"
    },
    {
        "query": "Design an interactive quiz on basic biology for middle schoolers",
        "target_category": "Learning",
        "expected_document": "quiz_generator.md"
    },
    {
        "query": "Write a technical blog post explaining zero-knowledge proofs",
        "target_category": "Content Creation",
        "expected_document": "technical_blog.md"
    },
    {
        "query": "Design a study plan for zero-knowledge proofs",
        "target_category": "Learning",
        "expected_document": "study_plan.md"
    },
    {
        "query": "Conduct a security audit of zero-knowledge proof code",
        "target_category": "Software Development",
        "expected_document": "security_audit.md"
    },
    {
        "query": "Write a LinkedIn post about zero-knowledge proofs",
        "target_category": "Content Creation",
        "expected_document": "linkedin_post.md"
    },
    {
        "query": "Write a guide explaining database design to beginners with analogies",
        "target_category": "Learning",
        "expected_document": "concept_explainer.md"
    }
]

def is_category_match(classified_cat: str, doc_cat: str) -> bool:
    """
    Checks if doc_cat matches/is allowed for classified_cat
    """
    mapping = {
        "Software Development": ["software_development", "uiux_design", "data_analysis"],
        "Learning": ["learning"],
        "Content Creation": ["content_creation", "business"],
        "Research": ["research"],
        "Image Generation": ["image_generation"],
        "Business Strategy": ["business"]
    }
    allowed = mapping.get(classified_cat, [])
    return doc_cat in allowed or doc_cat == "_frameworks"

def main():
    print("=" * 80)
    print(" PROMPTFORGE AI - CATEGORY-AWARE RETRIEVAL COMPARATIVE TEST SUITE")
    print("=" * 80 + "\n")
    
    strategies = ["none", "boost", "filter"]
    strategy_results = {}
    
    for idx_s, strategy in enumerate(strategies):
        if idx_s > 0:
            print("Pacing delay: Sleeping for 65 seconds to reset embedding API quota...")
            time.sleep(65)
        print(f"Evaluating strategy: '{strategy.upper()}' ...")
        total_cases = len(GOLDEN_QUERIES)
        class_correct = 0
        retrieval_correct = 0
        retrieval_top1_correct = 0
        ranks = []
        latencies = []
        cross_category_errors = 0
        
        for idx, q in enumerate(GOLDEN_QUERIES, 1):
            query_text = q["query"]
            
            # 1. Evaluate Category Classification
            classified = classify_category(query_text)
            class_pass = classified == q["target_category"]
            if class_pass:
                class_correct += 1
                
            # 2. Evaluate Top-3 Retrieval
            try:
                start_time = time.perf_counter()
                results = retrieve(
                    query_text, 
                    top_k=3, 
                    unique_documents=True,
                    classified_category=classified,
                    routing_strategy=strategy
                )
                elapsed = (time.perf_counter() - start_time) * 1000.0 # ms
                latencies.append(elapsed)
                
                retrieved_files = [item["source_document"] for item in results]
                case_rank = 4
                if q["expected_document"] in retrieved_files:
                    retrieval_correct += 1
                    case_rank = retrieved_files.index(q["expected_document"]) + 1
                    
                if case_rank == 1:
                    retrieval_top1_correct += 1
                    
                # Check for cross-category errors at Rank-1
                if results:
                    rank_1_doc_cat = results[0]["category"]
                    if not is_category_match(q["target_category"], rank_1_doc_cat):
                        cross_category_errors += 1
                        
                ranks.append(case_rank)
            except Exception as e:
                print(f"  [ERROR] Query {idx} failed: {e}")
                ranks.append(4)
                
        class_acc = (class_correct / total_cases) * 100.0
        retrieval_acc = (retrieval_correct / total_cases) * 100.0
        retrieval_top1_acc = (retrieval_top1_correct / total_cases) * 100.0
        mean_rank = sum(ranks) / total_cases
        avg_latency = sum(latencies) / len(latencies) if latencies else 0.0
        
        strategy_results[strategy] = {
            "class_acc": class_acc,
            "retrieval_top1_acc": retrieval_top1_acc,
            "retrieval_top3_acc": retrieval_acc,
            "mean_rank": mean_rank,
            "cross_category_errors": cross_category_errors,
            "avg_latency": avg_latency,
            "total_cases": total_cases,
            "class_correct": class_correct,
            "retrieval_top1_correct": retrieval_top1_correct,
            "retrieval_top3_correct": retrieval_correct
        }
        
    print("\n" + "=" * 80)
    print(" COMPARATIVE EVALUATION MATRIX SUMMARY")
    print("=" * 80)
    print(f"Total Test Cases evaluated: {total_cases}\n")
    print(f"| {'Strategy':<15} | {'Class Acc':<15} | {'Top-1 Acc':<15} | {'Top-3 Acc':<15} | {'Mean Rank':<10} | {'Cross-Cat Errors':<16} | {'Avg Latency':<12} |")
    print(f"|{'-'*17}|{'-'*17}|{'-'*17}|{'-'*17}|{'-'*12}|{'-'*18}|{'-'*14}|")
    
    for strategy in strategies:
        res = strategy_results[strategy]
        strategy_name = "None (Baseline)" if strategy == "none" else strategy.capitalize()
        class_str = f"{res['class_acc']:.1f}% ({res['class_correct']}/{res['total_cases']})"
        top1_str = f"{res['retrieval_top1_acc']:.1f}% ({res['retrieval_top1_correct']}/{res['total_cases']})"
        top3_str = f"{res['retrieval_top3_acc']:.1f}% ({res['retrieval_top3_correct']}/{res['total_cases']})"
        print(f"| {strategy_name:<15} | {class_str:<15} | {top1_str:<15} | {top3_str:<15} | {res['mean_rank']:.2f} | {res['cross_category_errors']:<16} | {res['avg_latency']:.2f} ms |")
        
    print("=" * 80 + "\n")
    
    # Exit with code matching success targets for boost
    boost_res = strategy_results["boost"]
    if boost_res["retrieval_top1_acc"] >= 85.0 and boost_res["cross_category_errors"] <= 2:
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
