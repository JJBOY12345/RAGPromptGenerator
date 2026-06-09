import sys
import os
import re
import time
import json
import requests

# Ensure root directory is on the python search path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.synthesizer import generate_prompt
from run_synthesis_tests import check_headings_compliance, check_placeholders, check_leakage

# Force UTF-8 encoding on Windows to prevent UnicodeEncodeError
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# The 30 Adversarial Queries targeting 10 leakage areas
ADVERSARIAL_QUERIES = [
    # 1. SQL schemas (forbidden: DDL statements or schema snippets)
    {
        "id": 1,
        "query": "Create a SQL database schema for user logins using CREATE TABLE statements",
        "category": "Software Development",
        "expected_headings": ["You are a", "Purpose", "Architecture & Structure", "Constraints & Performance", "Deliverables", "Instructions & Implementation Steps", "Output Format"],
        "forbidden_substrings": ["create table", "serial primary key", "insert into", "varchar"],
        "leakage_type": "SQL schemas"
    },
    {
        "id": 2,
        "query": "Write a PostgreSQL DDL script for our user subscription database",
        "category": "Software Development",
        "expected_headings": ["You are a", "Purpose", "Architecture & Structure", "Constraints & Performance", "Deliverables", "Instructions & Implementation Steps", "Output Format"],
        "forbidden_substrings": ["create table", "references users", "alter table", "varchar"],
        "leakage_type": "SQL schemas"
    },
    {
        "id": 3,
        "query": "Create SQL script to normalize users and user_roles junction table",
        "category": "Software Development",
        "expected_headings": ["You are a", "Purpose", "Architecture & Structure", "Constraints & Performance", "Deliverables", "Instructions & Implementation Steps", "Output Format"],
        "forbidden_substrings": ["create table", "references", "foreign key", "primary key"],
        "leakage_type": "SQL schemas"
    },
    # 2. API routes (forbidden: framework initialization, route mapping)
    {
        "id": 4,
        "query": "Write an Express API router in Node.js for product catalog endpoints",
        "category": "Software Development",
        "expected_headings": ["You are a", "Purpose", "Architecture & Structure", "Constraints & Performance", "Deliverables", "Instructions & Implementation Steps", "Output Format"],
        "forbidden_substrings": ["const express", "router.get", "app.get", "app.post", "res.status"],
        "leakage_type": "API routes"
    },
    {
        "id": 5,
        "query": "Write the code for REST API endpoints using Express in Node.js",
        "category": "Software Development",
        "expected_headings": ["You are a", "Purpose", "Architecture & Structure", "Constraints & Performance", "Deliverables", "Instructions & Implementation Steps", "Output Format"],
        "forbidden_substrings": ["require('express')", "app.get", "app.post", "router.post", "express()"],
        "leakage_type": "API routes"
    },
    {
        "id": 6,
        "query": "Build a Node checkout REST API route that accepts payments",
        "category": "Software Development",
        "expected_headings": ["You are a", "Purpose", "Architecture & Structure", "Constraints & Performance", "Deliverables", "Instructions & Implementation Steps", "Output Format"],
        "forbidden_substrings": ["const express", "router.post", "stripe.charges", "res.send"],
        "leakage_type": "API routes"
    },
    # 3. Code snippets (forbidden: executable script logic)
    {
        "id": 7,
        "query": "Generate the python code to scan a directory recursively for large files",
        "category": "Software Development",
        "expected_headings": ["You are a", "Purpose", "Architecture & Structure", "Constraints & Performance", "Deliverables", "Instructions & Implementation Steps", "Output Format"],
        "forbidden_substrings": ["os.walk", "def scan", "import os", "for root, dirs", "os.path"],
        "leakage_type": "code snippets"
    },
    {
        "id": 8,
        "query": "Write a python unit test suite for payment processing logic",
        "category": "Software Development",
        "expected_headings": ["You are a", "Purpose", "Architecture & Structure", "Constraints & Performance", "Deliverables", "Instructions & Implementation Steps", "Output Format"],
        "forbidden_substrings": ["def test_", "import unittest", "self.assert", "class TestPayment"],
        "leakage_type": "code snippets"
    },
    {
        "id": 9,
        "query": "Write the python logic to calculate the average response time of an API",
        "category": "Software Development",
        "expected_headings": ["You are a", "Purpose", "Architecture & Structure", "Constraints & Performance", "Deliverables", "Instructions & Implementation Steps", "Output Format"],
        "forbidden_substrings": ["def ", "import ", "elapsed", "sum(", "len("],
        "leakage_type": "code snippets"
    },
    # 4. Hashtags (forbidden: specific social tags)
    {
        "id": 10,
        "query": "Write a LinkedIn post with the hashtag #PromptEngineering to promote our AI",
        "category": "Content Creation",
        "expected_headings": ["You are a", "Purpose", "Target Audience", "Tone & Style", "Platform & Constraints", "Hook & Body structure", "Output Format"],
        "forbidden_substrings": ["#promptengineering", "#ai", "#tech"],
        "leakage_type": "hashtags"
    },
    {
        "id": 11,
        "query": "Draft a LinkedIn post including hashtag #AIAutomation",
        "category": "Content Creation",
        "expected_headings": ["You are a", "Purpose", "Target Audience", "Tone & Style", "Platform & Constraints", "Hook & Body structure", "Output Format"],
        "forbidden_substrings": ["#aiautomation", "#marketing", "#automation"],
        "leakage_type": "hashtags"
    },
    {
        "id": 12,
        "query": "Create a viral tweet promoting promptforge with hashtag #PromptForge",
        "category": "Content Creation",
        "expected_headings": ["You are a", "Purpose", "Target Audience", "Tone & Style", "Platform & Constraints", "Hook & Body structure", "Output Format"],
        "forbidden_substrings": ["#promptforge", "#ai", "#viral"],
        "leakage_type": "hashtags"
    },
    # 5. KPI metrics (forbidden: pre-filled numeric thresholds or values)
    {
        "id": 13,
        "query": "Draft a PRD where conversion rate KPI is set to 15% and DAU to 10k",
        "category": "Business Strategy",
        "expected_headings": ["You are a", "Purpose", "Business Context", "Competitive Constraints", "Strategic Action Plan", "Output Format"],
        "forbidden_substrings": ["15%", "10k", "dau", "conversion rate of 15"],
        "leakage_type": "KPI metrics"
    },
    {
        "id": 14,
        "query": "Draft a PRD with conversion rate KPI showing a 20% increase",
        "category": "Business Strategy",
        "expected_headings": ["You are a", "Purpose", "Business Context", "Competitive Constraints", "Strategic Action Plan", "Output Format"],
        "forbidden_substrings": ["20%", "conversion rate by 20"],
        "leakage_type": "KPI metrics"
    },
    {
        "id": 15,
        "query": "Design marketing SWOT strategies with success KPI showing 50% revenue growth",
        "category": "Business Strategy",
        "expected_headings": ["You are a", "Purpose", "Business Context", "Competitive Constraints", "Strategic Action Plan", "Output Format"],
        "forbidden_substrings": ["50%", "revenue growth"],
        "leakage_type": "KPI metrics"
    },
    # 6. User stories (forbidden: literal agile user stories)
    {
        "id": 16,
        "query": "Write user stories for the shopping cart checkout flow",
        "category": "Business Strategy",
        "expected_headings": ["You are a", "Purpose", "Business Context", "Competitive Constraints", "Strategic Action Plan", "Output Format"],
        "forbidden_substrings": ["as a user", "i want to", "so that", "as a shopper"],
        "leakage_type": "user stories"
    },
    {
        "id": 17,
        "query": "Define the user stories for user profile settings page",
        "category": "Business Strategy",
        "expected_headings": ["You are a", "Purpose", "Business Context", "Competitive Constraints", "Strategic Action Plan", "Output Format"],
        "forbidden_substrings": ["as a user", "i want to", "so that", "acceptance criteria"],
        "leakage_type": "user stories"
    },
    {
        "id": 18,
        "query": "Write user stories for B2B SaaS dashboard integration",
        "category": "Business Strategy",
        "expected_headings": ["You are a", "Purpose", "Business Context", "Competitive Constraints", "Strategic Action Plan", "Output Format"],
        "forbidden_substrings": ["as an admin", "i want to", "so that", "as a user"],
        "leakage_type": "user stories"
    },
    # 7. Timelines (forbidden: pre-filled schedules or dates)
    {
        "id": 19,
        "query": "Create a 6-week study schedule with week-by-week details for Docker",
        "category": "Learning",
        "expected_headings": ["You are a", "Purpose", "Objectives", "Knowledge Level", "Teaching Style", "Practice Exercises & Validation", "Output Format"],
        "forbidden_substrings": ["week 1", "week 2", "week 3", "6-week study plan", "6 weeks"],
        "leakage_type": "timelines"
    },
    {
        "id": 20,
        "query": "Draft a 4-week learning curriculum for JavaScript showing daily topics",
        "category": "Learning",
        "expected_headings": ["You are a", "Purpose", "Objectives", "Knowledge Level", "Teaching Style", "Practice Exercises & Validation", "Output Format"],
        "forbidden_substrings": ["week 1", "day 1", "day 2", "4-week study plan", "4 weeks"],
        "leakage_type": "timelines"
    },
    {
        "id": 21,
        "query": "Create a 3-month strategic roadmap detailing month-by-month rollout milestones",
        "category": "Business Strategy",
        "expected_headings": ["You are a", "Purpose", "Business Context", "Competitive Constraints", "Strategic Action Plan", "Output Format"],
        "forbidden_substrings": ["month 1", "month 2", "phase 1", "3-month", "3 months"],
        "leakage_type": "timelines"
    },
    # 8. Camera brands (forbidden: specific camera makes/models)
    {
        "id": 22,
        "query": "Design a photography prompt using Sony A7R V camera setup",
        "category": "Image Generation",
        "expected_headings": ["You are a", "Purpose", "Subject", "Style & Medium", "Lighting & Color", "Camera & Composition", "Output Format"],
        "forbidden_substrings": ["sony", "a7r"],
        "leakage_type": "camera brands"
    },
    {
        "id": 23,
        "query": "Design a Midjourney prompt utilizing a Sony camera body and portrait lens",
        "category": "Image Generation",
        "expected_headings": ["You are a", "Purpose", "Subject", "Style & Medium", "Lighting & Color", "Camera & Composition", "Output Format"],
        "forbidden_substrings": ["sony"],
        "leakage_type": "camera brands"
    },
    {
        "id": 24,
        "query": "Generate Midjourney prompt using Hasselblad H6D-100c camera specifications",
        "category": "Image Generation",
        "expected_headings": ["You are a", "Purpose", "Subject", "Style & Medium", "Lighting & Color", "Camera & Composition", "Output Format"],
        "forbidden_substrings": ["hasselblad", "h6d"],
        "leakage_type": "camera brands"
    },
    # 9. Lens specifications (forbidden: specific focal lengths/apertures)
    {
        "id": 25,
        "query": "Generate a portrait prompt using Hasselblad and 85mm f/1.4 lens specs",
        "category": "Image Generation",
        "expected_headings": ["You are a", "Purpose", "Subject", "Style & Medium", "Lighting & Color", "Camera & Composition", "Output Format"],
        "forbidden_substrings": ["85mm", "f/1.4"],
        "leakage_type": "lens specifications"
    },
    {
        "id": 26,
        "query": "Write a product photo prompt utilizing a 90mm f/2.8 macro lens specification",
        "category": "Image Generation",
        "expected_headings": ["You are a", "Purpose", "Subject", "Style & Medium", "Lighting & Color", "Camera & Composition", "Output Format"],
        "forbidden_substrings": ["90mm", "f/2.8"],
        "leakage_type": "lens specifications"
    },
    {
        "id": 27,
        "query": "Write prompt for commercial product rendering with 85mm lens settings",
        "category": "Image Generation",
        "expected_headings": ["You are a", "Purpose", "Subject", "Style & Medium", "Lighting & Color", "Camera & Composition", "Output Format"],
        "forbidden_substrings": ["85mm"],
        "leakage_type": "lens specifications"
    },
    # 10. Product names (forbidden: specific trademarked/brand names from KB)
    {
        "id": 28,
        "query": "Create a product photography prompt for Nike Air Max running shoes",
        "category": "Image Generation",
        "expected_headings": ["You are a", "Purpose", "Subject", "Style & Medium", "Lighting & Color", "Camera & Composition", "Output Format"],
        "forbidden_substrings": ["nike", "air max"],
        "leakage_type": "product names"
    },
    {
        "id": 29,
        "query": "Create a marketing copy for Aura Essence Skincare Oil product",
        "category": "Content Creation",
        "expected_headings": ["You are a", "Purpose", "Target Audience", "Tone & Style", "Platform & Constraints", "Hook & Body structure", "Output Format"],
        "forbidden_substrings": ["aura", "essence"],
        "leakage_type": "product names"
    },
    {
        "id": 30,
        "query": "Create launch strategy for ShopFlow Checkout e-commerce product",
        "category": "Business Strategy",
        "expected_headings": ["You are a", "Purpose", "Business Context", "Competitive Constraints", "Strategic Action Plan", "Output Format"],
        "forbidden_substrings": ["shopflow", "checkout"],
        "leakage_type": "product names"
    }
]

def main():
    print("=" * 80)
    print(" PROMPTFORGE AI - ADVERSARIAL PROMPT SYNTHESIS QUALITY GATE")
    print("=" * 80 + "\n")
    
    total_cases = len(ADVERSARIAL_QUERIES)
    results = []
    
    os.makedirs("logs", exist_ok=True)
    detail_log_path = os.path.join("logs", "adversarial_test_details.md")
    
    with open(detail_log_path, "w", encoding="utf-8") as df:
        df.write("# Adversarial Prompt Synthesis Test Execution Logs\n\n")
        df.write(f"Generated on: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
    print(f"Executing {total_cases} adversarial prompt synthesis test cases...")
    
    for idx, q in enumerate(ADVERSARIAL_QUERIES, 1):
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
                "leakage_type": q["leakage_type"],
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
                df.write(f"* **Leakage Target**: {q['leakage_type']}\n")
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
                "leakage_type": q["leakage_type"],
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
                
        time.sleep(1.0) # Light pacing delay
        
    # Summary Calculations
    total_passed = sum(1 for r in results if r["status"] == "PASS")
    total_failed = sum(1 for r in results if r["status"] == "FAIL")
    total_errors = sum(1 for r in results if r["status"] == "ERROR")
    
    compliance_rates = []
    placeholder_rates = []
    leakage_violations = 0
    total_latency = 0.0
    valid_latencies = 0
    
    # Track metrics by leakage type
    leakage_by_type = {}
    for r in results:
        l_type = r["leakage_type"]
        if l_type not in leakage_by_type:
            leakage_by_type[l_type] = {"total": 0, "leaked": 0}
        leakage_by_type[l_type]["total"] += 1
        if len(r["leakage_violations"]) > 0:
            leakage_by_type[l_type]["leaked"] += 1

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
    print(" ADVERSARIAL BENCHMARK MATRIX SUMMARY")
    print("=" * 80)
    print(f"Total test cases run           : {total_cases}")
    print(f"Fully Compliant Prompt Templates: {total_passed} / {total_cases} ({(total_passed/total_cases)*100.0:.1f}%)")
    print(f"Structural Heading Compliance  : {avg_compliance:.1f}%")
    print(f"Placeholder Usage Rate         : {avg_placeholder_rate:.1f}%")
    print(f"Total Downstream Leakage Alerts : {leakage_violations}")
    print(f"Average Generation Latency     : {avg_latency/1000.0:.2f} seconds")
    print(f"Execution errors / timeouts    : {total_errors}\n")
    
    print("Leakage Violations by Threat Vector:")
    for l_type, stats in leakage_by_type.items():
        print(f" - {l_type:<22}: {stats['leaked']} leaks / {stats['total']} cases")
    print("=" * 80 + "\n")
    
    # Save adversarial results summary
    summary_path = "logs/adversarial_benchmark_summary.json"
    summary_data = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "total_test_cases": total_cases,
        "passed_cases": total_passed,
        "failed_cases": total_failed,
        "error_cases": total_errors,
        "structural_compliance_rate": round(avg_compliance, 1),
        "placeholder_usage_rate": round(avg_placeholder_rate, 1),
        "downstream_leakage_violations": leakage_violations,
        "average_generation_latency_seconds": round(avg_latency/1000.0, 2),
        "leakage_by_type": leakage_by_type
    }
    with open(summary_path, "w") as sf:
        json.dump(summary_data, sf, indent=2)
        
    # Unload model
    try:
        print("[CLEANUP] Unloading local Ollama model...")
        ollama_host = os.getenv("OLLAMA_HOST", "http://localhost:11434").rstrip("/")
        ollama_model = os.getenv("OLLAMA_MODEL_NAME", "qwen2.5:7b")
        requests.post(f"{ollama_host}/api/generate", json={"model": ollama_model, "keep_alive": 0}, timeout=10)
        print("[CLEANUP] Model unloaded successfully.")
    except Exception as e:
        print(f"[CLEANUP] Note: Could not unload model: {e}")
        
    if total_passed == total_cases:
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
