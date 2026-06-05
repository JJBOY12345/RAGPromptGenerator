import sys
import os
import re
import time

# Ensure the root directory is on the python search path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.synthesizer import generate_prompt

# Force UTF-8 encoding on Windows to prevent UnicodeEncodeError
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# The 15 Frozen End-to-End Synthesis Queries
SYNTHESIS_QUERIES = [
    {
        "id": 1,
        "query": "Design a study plan for learning Rust programming",
        "category": "Learning",
        "expected_headings": ["You are a", "Purpose", "Objectives", "Knowledge Level", "Teaching Style", "Practice Exercises & Validation", "Output Format"],
        "forbidden_substrings": ["week 1", "week 2", "week 3", "cargo new", "borrow checker", "structs and enums"],
        "description": "Tests if Rust learning study plan executes chapters directly instead of instructions."
    },
    {
        "id": 2,
        "query": "Teach me how closures work in JavaScript using the Socratic method",
        "category": "Learning",
        "expected_headings": ["You are a", "Purpose", "Objectives", "Knowledge Level", "Teaching Style", "Practice Exercises & Validation", "Output Format"],
        "forbidden_substrings": ["closure is defined as", "closure is a function", "let closure =", "let x = 10", "function closure"],
        "description": "Tests if JS Socratic tutor executes lesson directly instead of tutoring rules."
    },
    {
        "id": 3,
        "query": "Write a LinkedIn post about how to start learning prompt engineering",
        "category": "Content Creation",
        "expected_headings": ["You are a", "Purpose", "Target Audience", "Tone & Style", "Platform & Constraints", "Hook & Body structure", "Output Format"],
        "forbidden_substrings": ["#promptengineering", "here is a linkedin post", "are you ready to", "scroll down for"],
        "description": "Tests if LinkedIn post writes actual viral content copy instead of guidelines."
    },
    {
        "id": 4,
        "query": "Draft a technical blog explaining the difference between SQL and NoSQL",
        "category": "Content Creation",
        "expected_headings": ["You are a", "Purpose", "Target Audience", "Tone & Style", "Platform & Constraints", "Hook & Body structure", "Output Format"],
        "forbidden_substrings": ["sql vs nosql", "relational databases use", "nosql databases are", "in this blog post"],
        "description": "Tests if SQL/NoSQL blog writes actual tutorial articles directly."
    },
    {
        "id": 5,
        "query": "Create a PostgreSQL schema for a user authentication database",
        "category": "Software Development",
        "expected_headings": ["You are a", "Purpose", "Architecture & Structure", "Constraints & Performance", "Deliverables", "Instructions & Implementation Steps", "Output Format"],
        "forbidden_substrings": ["create table users", "create table sessions", "password_hash varchar", "insert into users"],
        "description": "Tests if SQL DB schema pre-fills explicit DDL tables and schema definitions."
    },
    {
        "id": 6,
        "query": "Build a REST API in Node.js for a shopping cart checkout",
        "category": "Software Development",
        "expected_headings": ["You are a", "Purpose", "Architecture & Structure", "Constraints & Performance", "Deliverables", "Instructions & Implementation Steps", "Output Format"],
        "forbidden_substrings": ["const express", "app.post('/checkout'", "router.post", "res.status(200)"],
        "description": "Tests if API builder writes Node.js/Express API route code directly."
    },
    {
        "id": 7,
        "query": "Design a marketing strategy and SWOT analysis for our new database application",
        "category": "Business Strategy",
        "expected_headings": ["You are a", "Purpose", "Business Context", "Competitive Constraints", "Strategic Action Plan", "Output Format"],
        "forbidden_substrings": ["strengths:", "weaknesses:", "opportunities:", "threats:", "swot analysis table"],
        "description": "Tests if SWOT analyzer pre-fills SaaS strategic analyses."
    },
    {
        "id": 8,
        "query": "Create a marketing launch plan for a new SaaS product",
        "category": "Business Strategy",
        "expected_headings": ["You are a", "Purpose", "Business Context", "Competitive Constraints", "Strategic Action Plan", "Output Format"],
        "forbidden_substrings": ["phase 1: pre-launch", "saas launch checklist", "social media launch"],
        "description": "Tests if SaaS launcher writes specific rollout schedules."
    },
    {
        "id": 9,
        "query": "Conduct literature review on transformer models in academic papers",
        "category": "Research",
        "expected_headings": ["You are a", "Purpose", "Scope of Inquiry", "Methodology & Source Attribution", "Synthesis Requirements", "Output Format"],
        "forbidden_substrings": ["attention is all you need", "vaswani et al", "encoder-decoder architecture"],
        "description": "Tests if research engine writes academic article summaries directly."
    },
    {
        "id": 10,
        "query": "Synthesize research papers on LLM hallucination mitigation",
        "category": "Research",
        "expected_headings": ["You are a", "Purpose", "Scope of Inquiry", "Methodology & Source Attribution", "Synthesis Requirements", "Output Format"],
        "forbidden_substrings": ["hallucination in llms is mitigated by", "mitigation techniques are described below", "rlhf reduces hallucinations by"],
        "description": "Tests if literature review writes actual technical mitigations."
    },
    {
        "id": 11,
        "query": "Generate a prompt for a photorealistic brand illustration of a laptop",
        "category": "Image Generation",
        "expected_headings": ["You are a", "Purpose", "Subject", "Style & Medium", "Lighting & Color", "Camera & Composition", "Output Format"],
        "forbidden_substrings": ["/imagine prompt: a sleek", "sony a7r v", "90mm f/2.8", "diffused light and a natural"],
        "description": "Tests if visual generator outputs final Midjourney prompt string instead of prompt rules."
    },
    {
        "id": 12,
        "query": "Generate a prompt for commercial product photography of running shoes",
        "category": "Image Generation",
        "expected_headings": ["You are a", "Purpose", "Subject", "Style & Medium", "Lighting & Color", "Camera & Composition", "Output Format"],
        "forbidden_substrings": ["/imagine prompt: running shoes", "running shoes on a podium", "mesh uppers", "cinematic film shot"],
        "description": "Tests if visual generator leaks final Midjourney photography prompt."
    },
    {
        "id": 13,
        "query": "Perform a code review on this Python directory scanner script",
        "category": "Software Development",
        "expected_headings": ["You are a", "Purpose", "Architecture & Structure", "Constraints & Performance", "Deliverables", "Instructions & Implementation Steps", "Output Format"],
        "forbidden_substrings": ["review of python script", "vulnerabilities found", "line 15:", "script review:"],
        "description": "Tests if reviewer executes code audit output directly."
    },
    {
        "id": 14,
        "query": "Write api documentation for user profile endpoints",
        "category": "Content Creation",
        "expected_headings": ["You are a", "Purpose", "Target Audience", "Tone & Style", "Platform & Constraints", "Hook & Body structure", "Output Format"],
        "forbidden_substrings": ["get /api/v1/profile", "response 200 ok", "profile schema"],
        "description": "Tests if writer documents profiles directly instead of guidelines."
    },
    {
        "id": 15,
        "query": "Design an interactive quiz to test my understanding of Python decorators",
        "category": "Learning",
        "expected_headings": ["You are a", "Purpose", "Objectives", "Knowledge Level", "Teaching Style", "Practice Exercises & Validation", "Output Format"],
        "forbidden_substrings": ["question 1:", "what is a decorator", "decorators are useful because", "option a"],
        "description": "Tests if quiz generator outputs actual decorators questions."
    }
]

def check_headings_compliance(text: str, headings: list) -> tuple[int, list]:
    text_lower = text.lower()
    passed_count = 0
    missing = []
    
    for h in headings:
        h_clean = h.replace("[", "").replace("]", "").replace("...", "").lower().strip()
        # Look for the heading name in lowercase
        if h_clean in text_lower:
            passed_count += 1
        else:
            missing.append(h)
            
    return passed_count, missing

def check_placeholders(text: str) -> list:
    # Find patterns like {{SUBJECT}} or {{subject}}
    placeholders = re.findall(r"\{\{([a-zA-Z0-9_]+)\}\}", text)
    return placeholders

def check_leakage(text: str, forbidden: list) -> list:
    text_lower = text.lower()
    leaked = []
    for f in forbidden:
        if f.lower() in text_lower:
            leaked.append(f)
    return leaked

def main():
    print("=" * 80)
    print(" PROMPTFORGE AI - END-TO-END PROMPT SYNTHESIS QUALITY GATE")
    print("=" * 80 + "\n")
    
    total_cases = len(SYNTHESIS_QUERIES)
    results = []
    
    os.makedirs("logs", exist_ok=True)
    detail_log_path = os.path.join("logs", "synthesis_test_details.md")
    
    with open(detail_log_path, "w", encoding="utf-8") as df:
        df.write("# Prompt Synthesis End-to-End Test Execution Logs\n\n")
        df.write(f"Generated on: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
    print(f"Executing {total_cases} prompt synthesis test cases. Pacing calls to prevent API rate limits...")
    
    for idx, q in enumerate(SYNTHESIS_QUERIES, 1):
        print(f"[{idx}/{total_cases}] Query: \"{q['query'][:45]}...\"")
        start_time = time.perf_counter()
        
        try:
            res = generate_prompt(q["query"], top_k=3)
            elapsed = (time.perf_counter() - start_time) * 1000.0 # ms
            prompt_text = res["generated_prompt"]
            
            # 1. Structural Compliance
            passed_h, missing_h = check_headings_compliance(prompt_text, q["expected_headings"])
            headings_ok = passed_h == len(q["expected_headings"])
            
            # 2. Placeholders Check
            placeholders = check_placeholders(prompt_text)
            has_placeholders = len(placeholders) > 0
            
            # 3. Downstream Leakage check
            leaks = check_leakage(prompt_text, q["forbidden_substrings"])
            leakage_ok = len(leaks) == 0
            
            status = "PASS" if (headings_ok and has_placeholders and leakage_ok) else "FAIL"
            
            results.append({
                "id": q["id"],
                "query": q["query"],
                "category": q["category"],
                "status": status,
                "latency_ms": elapsed,
                "headings_passed": passed_h,
                "headings_total": len(q["expected_headings"]),
                "missing_headings": missing_h,
                "placeholder_count": len(placeholders),
                "placeholders_found": placeholders[:10],
                "leakage_violations": leaks,
                "error": None
            })
            
            # Append detailed output trace
            with open(detail_log_path, "a", encoding="utf-8") as df:
                df.write(f"## Test Case {q['id']}: {q['query']}\n\n")
                df.write(f"* **Category**: {q['category']}\n")
                df.write(f"* **Status**: {status}\n")
                df.write(f"* **Latency**: {elapsed:.2f} ms\n")
                df.write(f"* **Structural Headings**: {passed_h} / {len(q['expected_headings'])} passed\n")
                if missing_h:
                    df.write(f"  * *Missing Headings*: {missing_h}\n")
                df.write(f"* **Placeholders Found ({len(placeholders)})**: `{placeholders}`\n")
                df.write(f"* **Downstream Leakage Violations ({len(leaks)})**: `{leaks}`\n\n")
                df.write("### Synthesized Prompt Template Output:\n")
                df.write("```markdown\n")
                df.write(prompt_text)
                df.write("\n```\n")
                df.write("\n---\n\n")
                
        except Exception as e:
            elapsed = (time.perf_counter() - start_time) * 1000.0
            print(f"  [ERROR] Case {idx} failed: {e}")
            results.append({
                "id": q["id"],
                "query": q["query"],
                "category": q["category"],
                "status": "ERROR",
                "latency_ms": elapsed,
                "headings_passed": 0,
                "headings_total": len(q["expected_headings"]),
                "missing_headings": q["expected_headings"],
                "placeholder_count": 0,
                "placeholders_found": [],
                "leakage_violations": [],
                "error": str(e)
            })
            
            with open(detail_log_path, "a", encoding="utf-8") as df:
                df.write(f"## Test Case {q['id']}: {q['query']}\n\n")
                df.write(f"* **Status**: ERROR\n")
                df.write(f"* **Latency**: {elapsed:.2f} ms\n")
                df.write(f"* **Error Exception**: `{e}`\n\n---\n\n")
                
        # API Rate limit pacing sleep (4 seconds)
        time.sleep(4.0)
        
    # Summary Calculations
    total_passed = sum(1 for r in results if r["status"] == "PASS")
    total_failed = sum(1 for r in results if r["status"] == "FAIL")
    total_errors = sum(1 for r in results if r["status"] == "ERROR")
    
    compliance_rates = []
    placeholder_rates = []
    leakage_violations = 0
    total_latency = 0.0
    valid_latencies = 0
    
    for r in results:
        if r["status"] != "ERROR":
            compliance_rates.append(r["headings_passed"] / r["headings_total"])
            placeholder_rates.append(1 if r["placeholder_count"] > 0 else 0)
            leakage_violations += len(r["leakage_violations"])
            total_latency += r["latency_ms"]
            valid_latencies += 1
            
    avg_compliance = (sum(compliance_rates) / len(compliance_rates) * 100.0) if compliance_rates else 0.0
    avg_placeholder_rate = (sum(placeholder_rates) / len(placeholder_rates) * 100.0) if placeholder_rates else 0.0
    avg_latency = (total_latency / valid_latencies) if valid_latencies else 0.0
    
    print("\n" + "=" * 80)
    print(" SYNTHESIS QUALITY BENCHMARK MATRIX SUMMARY")
    print("=" * 80)
    print(f"Total test cases run           : {total_cases}")
    print(f"Fully Compliant Prompt Templates: {total_passed} / {total_cases} ({(total_passed/total_cases)*100.0:.1f}%)")
    print(f"Structural Heading Compliance  : {avg_compliance:.1f}%")
    print(f"Placeholder Usage Rate (has {{}}) : {avg_placeholder_rate:.1f}%")
    print(f"Total Downstream Leakage Alerts : {leakage_violations}")
    print(f"Average Generation Latency     : {avg_latency/1000.0:.2f} seconds")
    print(f"Execution errors / timeouts    : {total_errors}")
    print(f"Detailed traces written to     : {detail_log_path}")
    print("=" * 80 + "\n")
    
    # Save frozen benchmark metrics to synthesis_benchmark_summary.json in the root
    summary_path = "synthesis_benchmark_summary.json"
    import json
    summary_data = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "total_test_cases": total_cases,
        "passed_cases": total_passed,
        "failed_cases": total_failed,
        "error_cases": total_errors,
        "structural_compliance_rate": round(avg_compliance, 1),
        "placeholder_usage_rate": round(avg_placeholder_rate, 1),
        "downstream_leakage_violations": leakage_violations,
        "average_generation_latency_seconds": round(avg_latency/1000.0, 2)
    }
    with open(summary_path, "w") as sf:
        json.dump(summary_data, sf, indent=2)
        
    # Exit with code based on compliance
    if total_passed == total_cases:
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
