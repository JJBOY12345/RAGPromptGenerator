---
title: Universal Prompt Engineering Frameworks Reference Guide
category: _frameworks
tags:
  - prompt-engineering
  - frameworks
  - prompt-design
  - meta-prompting
difficulty: advanced
depth: reference
version: "1.0"
---

# Universal Prompt Engineering Frameworks

This reference document serves as the architectural blueprint for prompt design across the PromptForge AI platform. It documents the core logical skeletons that govern how AI models are tasked, context is injected, and outputs are structured. These frameworks ensure repeatable, high-quality, and structurally consistent model responses.

---

## 1. Universal Prompt Framework (Role-Goal-Context-Constraints-Output)

### Skeleton Structure
```markdown
ROLE: [Define who the AI is acting as, its specific expertise, and its professional tone]
GOAL: [Define the primary outcome the AI is trying to achieve]
CONTEXT: [Provide the background information, relevant data, or user circumstances]
CONSTRAINTS: [List the strict boundaries, forbidden behaviors, rules, or formatting limits]
OUTPUT: [Specify the exact formatting, length, markdown elements, or schema to return]
```

### When to Use
Use this framework as a fallback or baseline for any prompt that does not fit into a specialized domain. It provides the strongest baseline task definition for generic text generation, email writing, or brainstorming. It is optimized for zero-shot and standard instruction-following models.

---

## 2. Software Development Framework

### Skeleton Structure
```markdown
[AGENT ROLE]          Senior Software Architect & Specialized Developer
[PROJECT IDENTITY]    System identifier, core domain, and architecture style
[TECH STACK]          Languages, frameworks, databases, and dependencies
[ARCHITECTURE]        System patterns (e.g., microservices, serverless, clean architecture)
[REQUIREMENTS]        Functional requirements and non-functional guarantees (e.g., latency, throughput)
[CONSTRAINTS]         Timeline, backward-compatibility limits, and safety boundaries
[DELIVERABLES]        Desired code files, schema definitions, API routes, or tests
[OUTPUT FORMAT]       Well-commented compilable code blocks and file trees
```

### When to Use
Apply this framework when generating scripts, defining architectural specs, reviews, or database schemas. It ensures that the LLM considers environment variables, safety constraints, security practices, and testing patterns rather than just spitting out naive, context-free snippets.

---

## 3. UI/UX Design Framework

### Skeleton Structure
```markdown
[AGENT ROLE]          Senior Product Designer & Design Systems Architect
[PRODUCT IDENTITY]    Name and core value proposition of the product
[BRAND TONE]          The visual and emotive personality of the brand
[TARGET USERS]        User personas, physical/cognitive abilities, and device context
[DESIGN TOKENS]       Design primitives (colors, typography scales, spacing, elevation)
[COMPONENT LIBRARY]   Atomic structure specifications (atoms, molecules, organisms)
[ACCESSIBILITY]       WCAG standards and POUR compliance guidelines
[OUTPUT]              Specification documentation, component trees, or design token JSONs
```

### When to Use
Use this framework for user interface modeling, creating component specification libraries, and drafting design system documentation. It bridges the gap between pure visual ideas and developer-friendly token structures, establishing a standardized taxonomy for design systems.

---

## 4. Learning & Pedagogy Framework

### Skeleton Structure
```markdown
[AGENT ROLE]          Expert Pedagogue & Subject Matter Expert
[STUDENT PROFILE]     Prior knowledge level, learning styles, and common misconceptions
[LEARNING GOAL]       Target learning objectives mapped to Bloom's Taxonomy
[DIFFICULTY]          Beginning, Intermediate, or Advanced baseline calibration
[TEACHING STYLE]      Socratic, Direct Instruction, or Project-based learning loops
[SESSION LENGTH]      Structure of the lesson (intro, deep-dive, checkpoints, assessment)
[EXAMPLES]            High-impact real-world analogies and concrete code/data samples
[ASSESSMENT]          Formative checks for understanding and feedback loops
```

### When to Use
Utilize this framework when designing study plans, interactive tutor prompts, curriculum materials, or exam generators. It focuses on reducing cognitive load, pacing learning intervals, leveraging spaced repetition, and reinforcing concepts using the Socratic method instead of just providing direct answers.

---

## 5. Business Communication Framework

### Skeleton Structure
```markdown
[AGENT ROLE]          Specialized Corporate Professional or Communications Advisor
[COMMUNICATION GOAL]  Target outcome (e.g., alignment, pitch, decision-making)
[RECIPIENT ROLE]      Audience persona (e.g., C-Suite executive, board, engineering team)
[SENDER CONTEXT]      Background context, current relationship, and authoritative standing
[TONE]                Formal, diplomatic, persuasive, or transparently direct
[KEY TAKEAWAY]        The core message structured using the McKinsey Pyramid Principle
[CALL TO ACTION]      The singular, explicit next step expected from the reader
[OUTPUT FORMAT]       Structured emails, memos, or slide scripts
```

### When to Use
Apply this framework to executive briefings, email drafts, pitches, and board reporting. It forces the model to structure information top-down, starting with the conclusion/answer, backed by structured supporting evidence, ending with a clear call-to-action.

---

## 6. Research & Academic Framework

### Skeleton Structure
```markdown
[AGENT ROLE]          Lead Researcher & Rigorous Academic Analyst
[RESEARCH TOPIC]      The primary thesis or problem definition
[SCOPE & LIMITS]      Methodological bounds, geographical scope, and publication dates
[DEPTH]               Standard overview, detailed review, or systematic PRISMA meta-analysis
[STRUCTURE]           Introduction, literature breakdown, gap analysis, and conclusions
[CITATION STYLE]      APA, MLA, IEEE, or Chicago standards
[SOURCE TYPES]        Peer-reviewed academic databases, industry papers, or market reports
[OUTPUT]              Formatted research report draft with bracketed citation anchors
```

### When to Use
Use this framework when compiling literature reviews, competitive reports, and synthesis reviews of technical topics. It enforces academic rigor, structural skepticism, and a focus on mapping research gaps rather than generating generic web articles or blog summaries.

---

## 7. Image Generation Prompt Framework

### Skeleton Structure
```markdown
[AGENT ROLE]         Professional Visual Director & Camera/Lighting Expert
[IDENTITY REFERENCE] Reference image description or structural layout
[SUBJECT]            Detailed description of the primary focus, clothing, and posture
[ENVIRONMENT]        Studio backdrop, landscape details, and architectural environment
[LIGHTING]           Specific lighting setup (e.g., Rembrandt, softbox, split key)
[COLOR & MOOD]       Harmonious color palettes and visual emotive tone
[COMPOSITION]        Framing (e.g., headshot, rule-of-thirds), camera lens, and depth-of-field
[CONSTRAINTS]        Negative styles to avoid (e.g., cartoon, over-sharpened, plastic skin)
[OUTPUT QUALITY]     Technical descriptors (e.g., commercial print ready, 8k resolution)
```

### When to Use
Utilize this framework for translating ideas into visual prompts for Midjourney, Stable Diffusion, or DALL-E. It translates photographic terminology (lenses, lighting setups, shot types) into structured prompts that generate high-end, commercial-grade art.

---

## 8. Data Analysis Framework

### Skeleton Structure
```markdown
[AGENT ROLE]          Principal Data Analyst & Business Intelligence Expert
[DATASET SCHEMA]      Information about rows, columns, data types, and primary fields
[BUSINESS DOMAIN]     Industry background and strategic goals
[ANALYSIS GOAL]       Exploratory targets, predictive hypotheses, or descriptive summaries
[TECHNIQUES]          Methods (e.g., correlation, clustering, regression, anomaly checks)
[VISUALIZATIONS]      Chart specifications (e.g., heatmaps, scatterplots, bar layouts)
[STATISTICAL DEPTH]   Level of evidence required (descriptive vs. inferential vs. predictive)
[OUTPUT FORMAT]       Executive dashboard spec or exploratory code blocks with annotations
```

### When to Use
Use this framework for exploratory data analysis (EDA), visual dashboard briefs, and executive reporting summaries. It ensures that the model treats data with statistical rigor, avoids visual noise, maintains high data-to-ink ratios, and generates actionable, numbers-backed business hypotheses.
