import os
import sys
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ["PRIMARY_GENERATION_PROVIDER"] = "ollama"
os.environ["OLLAMA_MODEL_NAME"] = "qwen2.5:7b"

import src.synthesizer as synth

print("Running single generate_prompt test...")
start_time = time.perf_counter()
try:
    res = synth.generate_prompt("Design a study plan for learning Rust programming", top_k=3)
    elapsed = (time.perf_counter() - start_time) * 1000.0
    print(f"Success! Latency: {elapsed:.2f} ms")
    print(f"Generated prompt length: {len(res['generated_prompt'])}")
    print("Generated prompt preview:")
    print(res['generated_prompt'][:500])
except Exception as e:
    print(f"Failed: {e}")
