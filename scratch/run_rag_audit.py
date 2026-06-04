import os
import sys
import time
import json
import statistics

# Ensure the root directory is on the python search path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv
load_dotenv()

# Force PRIMARY_GENERATION_PROVIDER=huggingface to test real Hugging Face pipeline
os.environ["PRIMARY_GENERATION_PROVIDER"] = "huggingface"

# Import system modules
from src.loader import load_documents
from src.chunker import chunk_documents
from src.synthesizer import generate_prompt, SYSTEM_PROMPT, classify_category
from src.retriever import retrieve

# Force UTF-8 encoding on Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def run_chunk_audit():
    print("[1/5] Running Chunking Audit...")
    kb_dir = "knowledge_base"
    documents = load_documents(kb_dir)
    chunks = chunk_documents(documents)
    
    num_chunks = len(chunks)
    chunk_lengths = [len(c["content"]) for c in chunks]
    chunk_word_counts = [len(c["content"].split()) for c in chunks]
    
    avg_chunk_size = sum(chunk_lengths) / num_chunks if num_chunks else 0
    max_chunk = max(chunk_lengths) if num_chunks else 0
    min_chunk = min(chunk_lengths) if num_chunks else 0
    
    # Identify largest and smallest chunks
    largest_chunk_info = {}
    smallest_chunk_info = {}
    
    for c in chunks:
        if len(c["content"]) == max_chunk:
            largest_chunk_info = {
                "source": c["source_document"],
                "size_char": len(c["content"]),
                "content_preview": c["content"][:200]
            }
        if len(c["content"]) == min_chunk:
            smallest_chunk_info = {
                "source": c["source_document"],
                "size_char": len(c["content"]),
                "content_preview": c["content"][:200]
            }
            
    # Distribution by source file
    dist = {}
    for c in chunks:
        src = c["source_document"]
        dist[src] = dist.get(src, 0) + 1
        
    return {
        "num_chunks": num_chunks,
        "avg_chunk_size_char": round(avg_chunk_size, 2),
        "max_chunk_size_char": max_chunk,
        "min_chunk_size_char": min_chunk,
        "largest_chunk": largest_chunk_info,
        "smallest_chunk": smallest_chunk_info,
        "distribution_by_source": dist
    }

def run_e2e_queries():
    print("[2/5] Running 10 Representative RAG Queries...")
    
    test_queries = [
        {"goal": "Create a schema for a user authentication database", "domain": "Software Development"},
        {"goal": "Build a REST API in Node.js for a shopping cart", "domain": "Software Development"},
        {"goal": "Teach me how TCP/IP handshake works", "domain": "Learning"},
        {"goal": "Design a study plan for learning rust programming", "domain": "Learning"},
        {"goal": "Write a LinkedIn post about prompt engineering", "domain": "Content Creation"},
        {"goal": "Create a technical blog outline about vector databases", "domain": "Content Creation"},
        {"goal": "Analyze the security vulnerabilities in smart contracts", "domain": "Research"},
        {"goal": "Synthesize research papers on LLM hallucination mitigation", "domain": "Research"},
        {"goal": "Generate a prompt for a photorealistic product photo of a watch", "domain": "Image Generation"},
        {"goal": "Create a marketing launch plan for a new SaaS product", "domain": "Business Strategy"}
    ]
    
    audit_results = []
    
    for idx, q in enumerate(test_queries, 1):
        print(f"   -> Processing query {idx}/10: '{q['goal']}'")
        
        # Timing Retrieval
        start_retrieval = time.perf_counter()
        retrieved_items = retrieve(q["goal"], top_k=5, unique_documents=True)
        t_retrieval = (time.perf_counter() - start_retrieval) * 1000.0
        
        # Timing Context Assembly
        start_assembly = time.perf_counter()
        category = classify_category(q["goal"])
        
        # Build context block like in synthesizer.py
        context_parts = [
            f"USER GOAL:\n{q['goal']}\n",
            f"CATEGORY:\n{category}\n",
            "RETRIEVED KNOWLEDGE:\n"
        ]
        for i, item in enumerate(retrieved_items, 1):
            context_parts.append(f"--- DOCUMENT {i} ---")
            context_parts.append(f"Source Document: {item['source_document']}")
            context_parts.append(f"Category: {item['category']}")
            context_parts.append(f"Content:\n{item['chunk_text']}\n")
        context_block = "\n".join(context_parts)
        t_assembly = (time.perf_counter() - start_assembly) * 1000.0
        
        # Timing Generation
        start_generation = time.perf_counter()
        
        # Use our standard synthesize function
        # This will call HuggingFace since we set PRIMARY_GENERATION_PROVIDER=huggingface
        # If it times out or fails, we catch it
        generation_status = "SUCCESS"
        err_msg = ""
        generated_prompt = ""
        
        try:
            res = generate_prompt(q["goal"])
            generated_prompt = res["generated_prompt"]
        except Exception as e:
            generation_status = "FAILED"
            err_msg = str(e)
            
        t_generation = (time.perf_counter() - start_generation) * 1000.0
        
        audit_results.append({
            "goal": q["goal"],
            "target_domain": q["domain"],
            "classified_category": category,
            "latency_retrieval_ms": round(t_retrieval, 2),
            "latency_assembly_ms": round(t_assembly, 2),
            "latency_generation_ms": round(t_generation, 2),
            "generation_status": generation_status,
            "error": err_msg,
            "retrieved_sources": [
                {
                    "source": item["source_document"],
                    "score": item["score"],
                    "category": item["category"]
                }
                for item in retrieved_items
            ],
            "context_char_length": len(context_block),
            "context_est_tokens": len(context_block) // 4, # 1 token ~= 4 chars rule of thumb
            "num_chunks_retrieved": len(retrieved_items),
            "generated_prompt": generated_prompt
        })
        
        # Small delay between API calls to avoid triggering secondary rate-limiting on HF/Gemini
        time.sleep(3)
        
    return audit_results

def main():
    print("=" * 80)
    print("PROMPTFORGE AI - COMPREHENSIVE RAG PIPELINE AUDIT")
    print("=" * 80 + "\n")
    
    # 1. Chunking Audit
    chunk_stats = run_chunk_audit()
    
    # 2. End-to-End Queries Audit
    audit_results = run_e2e_queries()
    
    # Compile Audit Database
    report = {
        "chunk_stats": chunk_stats,
        "query_audits": audit_results
    }
    
    # Save raw audit output to scratch directory
    output_file = os.path.join("scratch", "raw_rag_audit_results.json")
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)
        
    print(f"\nAudit complete! Raw results written to {output_file}")
    
    # Quick statistics prints
    avg_gen_time = statistics.mean([q["latency_generation_ms"] for q in audit_results if q["generation_status"] == "SUCCESS"])
    failed_queries = sum(1 for q in audit_results if q["generation_status"] == "FAILED")
    
    print(f"Average HF Generation Latency: {avg_gen_time:.2f} ms")
    print(f"Number of failed generations: {failed_queries} / 10")

if __name__ == "__main__":
    main()
