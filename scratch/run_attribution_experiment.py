import sys
import os
import re
import json
import time

# Ensure root directory is in python search path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set local environment variables for the experiment
os.environ["PRIMARY_GENERATION_PROVIDER"] = "ollama"
os.environ["OLLAMA_MODEL_NAME"] = "qwen2.5:7b"

# Import synthesizer and retriever
import src.synthesizer as synth
from run_synthesis_tests import (
    SYNTHESIS_QUERIES,
    check_headings_compliance,
    check_placeholders,
    check_leakage
)

# Preserve original retrieve
original_retrieve = synth.retrieve

def find_and_read_kb_file(filename: str) -> str:
    kb_dir = "knowledge_base"
    for root, _, files in os.walk(kb_dir):
        if filename in files:
            file_path = os.path.join(root, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read()
    return ""

def extract_framework_section(text: str) -> str:
    # Look for "Prompt Framework" heading (can be ## or ### or #)
    match = re.search(r"(?:^|\n)(?:##)\s*Prompt\s+Framework\s*\n(.*?)(?=\n##\s+|\n#\s+|$)", text, re.DOTALL | re.IGNORECASE)
    if match:
        section_content = match.group(1).strip()
        # Find the first fenced code block in this section
        code_match = re.search(r"```[a-zA-Z0-9_\-\+]*\n(.*?)```", section_content, re.DOTALL)
        if code_match:
            return code_match.group(1).strip()
        return section_content
    return ""

def get_prompt_framework(source_doc: str, chunk_text: str) -> str:
    # 1. Try to extract from the chunk text first
    framework = extract_framework_section(chunk_text)
    if framework:
        return framework
        
    # 2. If not found in the chunk, load the full file
    full_content = find_and_read_kb_file(source_doc)
    if full_content:
        framework = extract_framework_section(full_content)
        if framework:
            return framework
            
    # 3. Fallback: if we still can't find it, just return the chunk text itself
    return chunk_text

# Define Mock Retrievers
def mock_retrieve_no_rag(*args, **kwargs):
    return []

def mock_retrieve_clean_rag(*args, **kwargs):
    items = original_retrieve(*args, **kwargs)
    cleaned_items = []
    for item in items:
        new_item = dict(item)
        new_item["chunk_text"] = get_prompt_framework(item["source_document"], item["chunk_text"])
        cleaned_items.append(new_item)
    return cleaned_items

def run_configuration_benchmark(config_name: str, retrieve_func):
    # Patch retrieve function
    synth.retrieve = retrieve_func
    
    print(f"\nRunning Benchmark for Configuration: {config_name}...")
    
    results = []
    total_cases = len(SYNTHESIS_QUERIES)
    
    for idx, q in enumerate(SYNTHESIS_QUERIES, 1):
        print(f"  [{idx}/{total_cases}] Query: \"{q['query'][:35]}...\"")
        start_time = time.perf_counter()
        
        try:
            res = synth.generate_prompt(q["query"], top_k=3)
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
                "leakage_violations": leaks,
                "generated_prompt": prompt_text,
                "retrieved_sources": res.get("retrieved_sources", []),
                "error": None
            })
            
        except Exception as e:
            elapsed = (time.perf_counter() - start_time) * 1000.0
            print(f"    [ERROR] Case {idx} failed: {e}")
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
                "leakage_violations": [],
                "generated_prompt": "",
                "retrieved_sources": [],
                "error": str(e)
            })
            
        # Pacing sleep is bypassed or set very small for local Ollama to run faster
        time.sleep(0.1)
        
    return results

def compute_metrics(results):
    total_cases = len(results)
    passed_cases = sum(1 for r in results if r["status"] == "PASS")
    
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
    
    return {
        "pass_rate": round((passed_cases / total_cases) * 100.0, 1),
        "passed_count": passed_cases,
        "total_count": total_cases,
        "placeholder_compliance": round(avg_placeholder_rate, 1),
        "heading_compliance": round(avg_compliance, 1),
        "leakage_alerts": leakage_violations,
        "avg_latency_seconds": round(avg_latency / 1000.0, 2)
    }

def main():
    print("=" * 80)
    # 1. Run Configuration 1 (Current RAG)
    config1_results = run_configuration_benchmark("1. Current RAG", original_retrieve)
    config1_metrics = compute_metrics(config1_results)
    
    # 2. Run Configuration 2 (No RAG)
    config2_results = run_configuration_benchmark("2. No RAG", mock_retrieve_no_rag)
    config2_metrics = compute_metrics(config2_results)
    
    # 3. Run Configuration 3 (Clean RAG)
    config3_results = run_configuration_benchmark("3. Clean RAG", mock_retrieve_clean_rag)
    config3_metrics = compute_metrics(config3_results)
    
    print("\n" + "=" * 80)
    print(" ATTRIBUTION EXPERIMENT SUMMARY")
    print("=" * 80)
    
    summary_markdown = f"""
| Configuration | Pass Rate | Placeholder Compliance | Heading Compliance | Leakage Alerts | Avg Latency |
| --- | :---: | :---: | :---: | :---: | :---: |
| **1. Current RAG** | {config1_metrics['pass_rate']}% ({config1_metrics['passed_count']}/{config1_metrics['total_count']}) | {config1_metrics['placeholder_compliance']}% | {config1_metrics['heading_compliance']}% | {config1_metrics['leakage_alerts']} | {config1_metrics['avg_latency_seconds']}s |
| **2. No RAG** | {config2_metrics['pass_rate']}% ({config2_metrics['passed_count']}/{config2_metrics['total_count']}) | {config2_metrics['placeholder_compliance']}% | {config2_metrics['heading_compliance']}% | {config2_metrics['leakage_alerts']} | {config2_metrics['avg_latency_seconds']}s |
| **3. Clean RAG** | {config3_metrics['pass_rate']}% ({config3_metrics['passed_count']}/{config3_metrics['total_count']}) | {config3_metrics['placeholder_compliance']}% | {config3_metrics['heading_compliance']}% | {config3_metrics['leakage_alerts']} | {config3_metrics['avg_latency_seconds']}s |
"""
    print(summary_markdown)
    
    # Save results to disk
    experiment_results = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "metrics": {
            "current_rag": config1_metrics,
            "no_rag": config2_metrics,
            "clean_rag": config3_metrics
        },
        "details": {
            "current_rag": [{"id": r["id"], "query": r["query"], "status": r["status"], "leakage": r["leakage_violations"], "missing_headings": r["missing_headings"]} for r in config1_results],
            "no_rag": [{"id": r["id"], "query": r["query"], "status": r["status"], "leakage": r["leakage_violations"], "missing_headings": r["missing_headings"]} for r in config2_results],
            "clean_rag": [{"id": r["id"], "query": r["query"], "status": r["status"], "leakage": r["leakage_violations"], "missing_headings": r["missing_headings"]} for r in config3_results]
        }
    }
    
    with open("logs/attribution_experiment_results.json", "w", encoding="utf-8") as f:
        json.dump(experiment_results, f, indent=2)
        
    # Generate chunk audit for failing baseline cases
    failing_cases = [r for r in config1_results if r["status"] != "PASS"]
    
    with open("logs/attribution_experiment_report.md", "w", encoding="utf-8") as rf:
        rf.write("# Synthesis Attribution Experiment & Chunk Audit Report\n\n")
        rf.write(f"Generated on: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        rf.write("## 1. Controlled Benchmark Summary\n")
        rf.write(summary_markdown + "\n")
        
        rf.write("## 2. Chunk Audit for Failing Baseline Cases\n")
        rf.write("Below are the details of the top retrieved chunks for every case that failed under the **Current RAG** baseline configuration. This helps locate the exact documents and chunks responsible for synthesis errors.\n\n")
        
        for fc in failing_cases:
            rf.write(f"### Case {fc['id']}: \"{fc['query']}\"\n")
            rf.write(f"- **Category**: {fc['category']}\n")
            rf.write(f"- **Baseline Status**: {fc['status']}\n")
            rf.write(f"- **Leakage Violations**: `{fc['leakage_violations']}`\n")
            rf.write(f"- **Missing Headings**: `{fc['missing_headings']}`\n")
            rf.write("- **Retrieved Chunks**:\n")
            for i, src in enumerate(fc["retrieved_sources"], 1):
                rf.write(f"  {i}. **Doc**: [{src['source_document']}](file:///knowledge_base/{src['source_document']}) (Score: {src['score']})\n")
                # Clean snippet for readability
                snippet_preview = src['matched_excerpt'].strip().replace("\n", " ").replace("\r", "")[:200]
                rf.write(f"     - *Snippet*: `{snippet_preview}...`\n")
            rf.write("\n---\n\n")
            
    print("Detailed report written to logs/attribution_experiment_report.md")
    
    # Clean up model after run
    try:
        import requests
        print("[CLEANUP] Unloading local Ollama model to free system resources...")
        requests.post("http://localhost:11434/api/generate", json={"model": "qwen2.5:7b", "keep_alive": 0}, timeout=10)
        print("[CLEANUP] Model unloaded successfully.")
    except Exception as e:
        print(f"[CLEANUP] Note: Could not unload model: {e}")

if __name__ == "__main__":
    main()
