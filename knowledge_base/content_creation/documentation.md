---
title: Technical Documentation Specifier
category: content_creation
subcategory: documentation
tags: [documentation, technical-writing, readme]
difficulty: intermediate
depth: medium
retrieval_keywords: [documentation writer, readme spec, api manual]
use_case: Retrieve when writing README files, API manuals, or system user guides.
placeholder_count: 3
version: "1.0"
---
# Technical Documentation Specifier
## Purpose
Generates documentation briefs based on the standard Divio 4-quadrant framework.
## When to Retrieve This Template
- "Write a README.md file for our open-source utility."
- "Generate API user guide documentation for our microservice."
- "Create a technical system architecture document."
## Prompt Framework
You are a Technical Writer. Write a document of type {{DOCUMENT_GOAL}} for {{PROJECT_NAME}} targeted at {{TARGET_AUDIENCE}}. Respect Divio guidelines.
## Required Context
- Project Name: {{PROJECT_NAME}}
- Target Audience: {{TARGET_AUDIENCE}}
- Document Goal: {{DOCUMENT_GOAL}}
## Optional Configuration
- Code Blocks: [Bash syntax | Programming scripts | None]
## Example Prompt
Create a getting started README tutorial for a task scheduler targeted at juniors.
## Best Practices
1. Maintain standard, clean markdown layouts compatible with static generators.
2. Supply copy-pasteable terminal instructions for installation and setup.
3. Structure API parameters using clear table schemas mapping data types.
