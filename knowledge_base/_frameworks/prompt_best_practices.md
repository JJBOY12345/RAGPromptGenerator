---
title: Prompt Engineering Best Practices Reference Guide
category: _frameworks
tags:
  - prompt-engineering
  - best-practices
  - optimization
  - system-design
difficulty: advanced
depth: reference
version: "1.0"
---

# Prompt Engineering Best Practices

This guide documents the gold standards, mental models, and writing rules for creating optimal prompts across the PromptForge AI ecosystem. By applying these guidelines, you maximize the predictability, reasoning capability, and performance of LLMs in production.

---

## 1. Role Assignment (Explicit vs. Implicit)

Assigning a persona is the single most effective way to anchor the LLM’s vocabulary, tone, and logical baseline.
* **Implicit (Weak):** "Write a Python script to scan directories."
* **Explicit (Strong):** "You are a Senior Systems Administrator and Python Automation Architect specializing in secure, cross-platform file operations. Write a robust Python script to scan directories."

**The Golden Rule:** Always establish the agent's professional identity, depth of experience, and visual/tonal persona in the very first sentence of the prompt.

---

## 2. Constraint Specification

Large language models require boundaries to keep them from generating excessive, insecure, or off-topic content. Enforce negative constraints as strictly as positive instructions.
* **Negative Constraints:** Use absolute terms ("NEVER use external libraries," "DO NOT generate markdown titles").
* **Positive Constraints:** Specify explicit boundary limits ("Output exactly 3 bullet points," "Limit explanation to 100 words").
* **Formatting:** Group constraints under a clear, prominent section headers or bulleted list so they are not lost in long paragraphs of context.

---

## 3. Output Format Definition

Do not leave the formatting of the response to chance. Tell the LLM exactly how to shape its output.
* Provide an explicit outline or structural blueprint of the desired response.
* If a machine-readable format is required (JSON, YAML, CSV), supply an empty schema or few-shot example.
* Use delimiters like backticks for raw code blocks, and specify the exact language tag (e.g., ````python ... ````) to ensure syntax highlighting works in standard markdown parsers.

---

## 4. Context vs. Instruction Separation

Mixing background data, variable values, and instructions together in a single block of text causes "attention dilution" in self-attention heads.
* **Use XML Tags:** Delimit raw data, source text, and instructions using custom tags (e.g., `<user_data>...</user_data>`, `<source_document>...</source_document>`).
* **Why it works:** Modern models (especially Anthropic’s Claude and Gemini) are pre-trained to recognize XML structures as boundaries, reducing the risk of prompt injection and contextual confusion.

---

## 5. Placeholder Usage Rules (`{{...}}` vs. `[...]`)

PromptForge AI uses a distinct, hybrid placeholder syntax to cater to both programmatic automated engines and human configurability.
* **`{{VARIABLE_NAME}}` (Programmatic):** Used for variables that must be automatically replaced by code before prompt execution (e.g., API keys, dynamic user inputs, tech stacks). These must be all uppercase with underscores.
* **`[Optional Hint / Choice]` (Human Guidance):** Used for configuration options, choices, or instructions that a human user reads to customize the prompt before running it (e.g., `[Choose: Socratic | Direct Instruction]`).

---

## 6. Chain-of-Thought (CoT) Triggers

When asking an LLM to perform complex reasoning, mathematical steps, code reviews, or architectural designs, forcing a "thinking step" dramatically improves output accuracy.
* **Trigger Phrase:** "Analyze the requirement step-by-step before outputting the final result. Write your reasoning inside `<thinking>` tags."
* **Why it works:** Allowing the model to output intermediate tokens lets it allocate computational steps to reasoning before arriving at the conclusion.

---

## 7. Length and Specificity Calibration

Calibrate prompt length and instructions to match the target model's context window behavior:
* **Short, High-Frequency Tasks:** Keep instructions simple, direct, and under 20 lines (LIGHTWEIGHT).
* **High-Complexity Engineering Tasks:** Provide thorough contextual rules, error-handling instructions, and full template definitions (DEEP). Use explicit, exhaustive checklists rather than loose descriptions.

---

## 8. Avoiding Ambiguity

Vague words lead to high-variance, unpredictable model completions. Replace general descriptors with precise, action-oriented instructions.
* **Ambiguous (Bad):** "Make the code run fast," "Write in a professional tone," "Be helpful."
* **Precise (Good):** "Optimize the algorithm for O(N log N) time complexity," "Write in a formal, peer-reviewed academic style," "Structure the output with clear bold sub-headers and a summary block."

---

## 9. RAG-Optimized Writing (For Knowledge Base Documents)

When writing documents for a RAG knowledge base, design them specifically for search engines:
* **Rich Frontmatter:** Include descriptive meta titles, categories, tags, and semantic search keywords.
* **Trigger Queries:** Include a "When to Retrieve" list containing the exact search phrases and natural-language queries that should trigger this chunk.
* **Semantic Headers:** Use descriptive `##` section headers. Vector index splitters (like `MarkdownHeaderTextSplitter`) will chunk the document along these headers, keeping each retrieved node highly contextual and self-contained.

---

## 10. Common Anti-Patterns to Avoid

* **The Double Negative:** Saying "Don't avoid using..." confuses model negation logic. State instructions affirmatively.
* **Prompt Bloat:** Adding historical logs or irrelevant code comments to the prompt context. Keep the prompt focused strictly on the current task environment.
* **Unbounded Variables:** Leaving `{{VARIABLE}}` values empty or poorly documented, leading to the model treating the double braces as part of the task instruction.
* **Lack of Code Language Blocks:** Forgetting to wrap example outputs in standard code blocks, which breaks user-interface rendering.
