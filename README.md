# PromptForge AI — RAG-Optimized Prompt Synthesis Engine

PromptForge AI is a production-grade Retrieval-Augmented Generation (RAG) system designed to synthesize highly optimized, parameterized AI system prompts and instructions from a repository of best-practice templates.

The core pipeline routes user goals to specific blueprint blueprints, retrieves relevant template guides, and generates clean instruction cards with dynamic variables.

---

## 🛠️ Project Architecture

```
                                [ User Goal ]
                                      │
                                      ▼
                        ┌───────────────────────────┐
                        │   Intent Classifier       │ (100% Acc)
                        └─────────────┬─────────────┘
                                      │ (Assigned Category)
                                      ▼
                        ┌───────────────────────────┐
                        │  Chroma Vector Search     │ (Category Score Boosting)
                        └─────────────┬─────────────┘
                                      │
                                      ▼
                        ┌───────────────────────────┐
                        │  Context Builder & RAG    │ (Hybrid Adaptive Chunks)
                        └─────────────┬─────────────┘
                                      │
                                      ▼
                        ┌───────────────────────────┐
                        │   Synthesizer (Flash/Qwen)│ (Synthesized Blueprint)
                        └───────────────────────────┘
```

* **Category Classifier (`src/synthesizer.py`)**: Local deterministic parser matching user goals to blueprint domains (Learning, Software Development, Content Creation, etc.) with 100% accuracy.
* **Hybrid Adaptive Chunker (`src/chunker.py`)**: Size-aware splitter keeping files under 2.5KB whole to preserve format identity while sectioning larger templates into H2 semantic blocks.
* **Vector Store (`src/vector_store.py` & `src/retriever.py`)**: persistent ChromaDB engine executing category-aware retrieval. Implements **Category Score Boosting** to eliminate cross-category noise.
* **Batch Embedding Wrapper (`src/embeddings.py`)**: Optimized Gemini SDK integration generating batches of `models/gemini-embedding-2` vectors.

---

## 🚀 Setup & Installation

1. **Clone and Navigate**:
   ```bash
   git clone <repo-url>
   cd RAG_workshop
   ```

2. **Environment Variables**:
   Create a `.env` file in the root directory:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   EMBEDDING_MODEL=models/gemini-embedding-2
   ```

3. **Rebuild the Vector Database**:
   Clear old databases and generate new hybrid adaptive chunks and embeddings:
   ```bash
   python scratch/reindex_db.py
   ```

4. **Verify Embedding Database Integrity**:
   Check vector count, shapes, dimensions, and values:
   ```bash
   python scratch/validate_embeddings.py
   ```

---

## 📊 Evaluation & Benchmarking

The workspace is equipped with a rigorous quality gate comprising 50 golden queries testing classification accuracy, Rank-1 and Rank-3 retrieval containment, mean rank, and cross-category errors.

To run the side-by-side benchmark comparing vanilla retrieval against category score boosting and hard category filtering:

```bash
python run_retrieval_tests.py
```

### Retrieval Optimization Comparison Matrix:

| Strategy | Classification Acc | Top-1 Accuracy | Top-3 Accuracy | Mean Rank | Cross-Cat Errors | Avg Latency |
|---|---|---|---|---|---|---|
| **Vanilla RAG** | 100.0% | 80.0% | 100.0% | 1.24 | 7 | ~400 ms |
| **Category Boost** (Active) | **100.0%** | **94.0%** | **100.0%** | **1.08** | **0** | **~430 ms** |
| **Category Filter** | 100.0% | 94.0% | 100.0% | 1.08 | 0 | ~460 ms |

---

## 🔍 Debugging Tools

Use the real-time CLI tool to inspect the classification and retrieved database outputs for any query:

```bash
python debug_retrieval.py "Help me write a security audit for a payment gateway"
```
