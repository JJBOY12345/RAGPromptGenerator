# PromptForge RAG-Driven Prompt Synthesis Engine

PromptForge is a Retrieve-and-Synthesize Prompt Engineering pipeline designed to automatically generate high-quality, expert-grade system prompts based on user queries. It retrieves domain-specific formatting techniques and contextual resources from a local Chroma DB knowledge base, then synthesizes them with a LLM (Hugging Face Qwen / Google Gemini fallback).

## Features

- **Semantic Chunk Retrieval**: Queries a local vector database to find relevant prompt templates, guidelines, and context.
- **Dynamic Prompt Synthesis**: Merges retrieved instructions and templates to generate target-oriented prompts.
- **Fail-Safe Fallbacks**: Integrates Gemini API for fallback generation in case local resources or Hugging Face endpoints fail.
- **Verification Tests**: Built-in test suite for validating retrieval accuracy, synthesis flow, and system infrastructure.

## Getting Started

1. Set up your environment variables:
   Create a `.env` file in the root directory:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

2. Run the demonstration script:
   ```bash
   python run_promptforge_demo.py
   ```

3. Run the verification test suite:
   ```bash
   python run_retrieval_tests.py
   ```
