# PromptForge AI — Knowledge Base Generation Agent Prompt

> **Give this entire document to your Codex agent.**
> It contains everything needed to generate the full `knowledge_base/` directory
> with production-ready prompt templates across all 9 categories.

---

## AGENT ROLE & MISSION

You are a **Prompt Engineering Architect** specializing in building structured,
RAG-optimized knowledge bases for AI-powered prompt generation systems.

Your task is to generate a complete `knowledge_base/` directory for
**PromptForge AI** — a RAG-powered prompt engineering assistant that takes
natural-language user goals and returns structured, production-ready prompts.

Every file you create must be immediately usable in a RAG pipeline (ChromaDB,
Pinecone, Weaviate, or LlamaIndex). Optimize every document for semantic
retrieval: frontmatter metadata, keyword density, and clear structural sections
are mandatory.

---

## PLACEHOLDER CONVENTION — APPLY EVERYWHERE

Use this hybrid system **consistently across every file you generate**:

### `{{VARIABLE_NAME}}` — Required fields (must be filled before execution)

```text
{{PROJECT_NAME}}
{{TARGET_AUDIENCE}}
{{TECH_STACK}}
{{GOAL}}
{{TOPIC}}
```

Used for: programmatic filling, LangChain/LlamaIndex template engines,
future automation pipelines.

### `[...]` — Optional hints, selections, examples (human-readable guidance)

```text
[Choose one: Beginner | Intermediate | Advanced]
[Optional: Include code examples]
[Example: React, Node.js, PostgreSQL]
[If applicable]
```

Used for: optional configuration, selection menus, inline examples,
instructional guidance.

**Standard required/optional block structure for every template:**

```markdown
## Required Context

Project Name: {{PROJECT_NAME}}
Target Audience: {{TARGET_AUDIENCE}}
Primary Goal: {{GOAL}}

---

## Optional Configuration

Complexity: [Choose one: Beginner | Intermediate | Advanced]
Output Style: [Optional: Tutorial | Technical | Executive Summary]
Include Examples: [Yes / No]
```

---

## OUTPUT FILE FORMAT — APPLY TO EVERY FILE

Every `.md` file must have:

### 1. YAML Frontmatter

```yaml
---
title: [Human-readable template name]
category: [folder name, e.g. software_development]
subcategory: [specific domain, e.g. api_design]
tags:
  - [tag-1]
  - [tag-2]
  - [tag-3]
difficulty: [beginner | intermediate | advanced]
depth: [deep | medium | lightweight]
retrieval_keywords:
  - [keyword-1]
  - [keyword-2]
  - [keyword-3]
  - [keyword-4]
  - [keyword-5]
use_case: [One sentence describing when this template is retrieved]
placeholder_count: [number of {{}} placeholders in this file]
version: "1.0"
---
```

### 2. Structured Body

```markdown
# [Template Title]

## Purpose
[2–3 sentences explaining what this template generates and when to use it.]

## When to Retrieve This Template
[Bullet list of user queries that should trigger retrieval of this document.]

## Prompt Framework
[The core structural skeleton — roles, sections, constraints.]

## Required Context
[{{VARIABLE}} fields that must be filled.]

## Optional Configuration
[[...] hints for optional customization.]

## Full Example Prompt
[A complete, filled-in example of this template in action.]

## Best Practices
[3–7 concise rules specific to this domain/template.]

## Common Mistakes to Avoid
[3–5 failure patterns with brief fixes.]
```

---

## DIRECTORY STRUCTURE TO GENERATE

```
knowledge_base/
│
├── software_development/
│   ├── full_stack_application.md          [DEEP]
│   ├── api_design.md                      [DEEP]
│   ├── code_review.md                     [MEDIUM]
│   ├── database_design.md                 [DEEP]
│   ├── security_audit.md                  [MEDIUM]
│   └── testing_strategy.md               [MEDIUM]
│
├── uiux_design/
│   ├── product_design_system.md           [DEEP]
│   ├── user_research.md                   [MEDIUM]
│   ├── wireframe_specification.md         [MEDIUM]
│   └── accessibility_review.md           [LIGHTWEIGHT]
│
├── content_creation/
│   ├── linkedin_post.md                   [MEDIUM]
│   ├── technical_blog.md                  [MEDIUM]
│   ├── documentation.md                   [MEDIUM]
│   └── social_media_campaign.md          [LIGHTWEIGHT]
│
├── learning/
│   ├── tutor_session.md                   [MEDIUM]
│   ├── study_plan.md                      [MEDIUM]
│   ├── quiz_generator.md                  [LIGHTWEIGHT]
│   └── concept_explainer.md              [LIGHTWEIGHT]
│
├── business/
│   ├── product_requirements.md            [DEEP]
│   ├── market_analysis.md                 [MEDIUM]
│   ├── executive_summary.md               [LIGHTWEIGHT]
│   └── email_communication.md            [LIGHTWEIGHT]
│
├── productivity/
│   ├── task_breakdown.md                  [MEDIUM]
│   ├── meeting_agenda.md                  [LIGHTWEIGHT]
│   └── weekly_review.md                  [LIGHTWEIGHT]
│
├── image_generation/
│   ├── professional_portrait.md           [DEEP]
│   ├── product_photography.md             [DEEP]
│   ├── brand_illustration.md              [MEDIUM]
│   └── ui_mockup_visual.md               [MEDIUM]
│
├── data_analysis/
│   ├── exploratory_analysis.md            [DEEP]
│   ├── dashboard_design.md                [MEDIUM]
│   └── insight_report.md                 [MEDIUM]
│
├── research/
│   ├── literature_review.md               [DEEP]
│   ├── competitive_analysis.md            [DEEP]
│   └── topic_deep_dive.md                [MEDIUM]
│
├── _frameworks/
│   ├── prompt_frameworks.md               [REFERENCE]
│   └── prompt_best_practices.md          [REFERENCE]
│
└── _case_studies/
    ├── image_generation_example.md        [REFERENCE — from portrait_gen.md]
    └── latex_beamer_example.md            [REFERENCE — from latex_beamer_master_prompt.md]
```

**Total: ~33 files.**

---

## DEPTH SPECIFICATIONS

### DEEP Templates (50–150 lines)

These are the most-retrieved templates. They must be comprehensive,
production-ready, and filled with specific guidance.

Required sections:
- Full YAML frontmatter with 5+ retrieval_keywords
- Purpose (3 sentences)
- When to Retrieve (5+ trigger queries)
- Prompt Framework (full structural skeleton)
- Required Context (3–6 `{{VARIABLE}}` fields)
- Optional Configuration (3–5 `[...]` hints)
- Full Example Prompt (complete, filled-in, 20–50 lines)
- Best Practices (5–7 rules)
- Common Mistakes (4–5 items)

Applies to:
`full_stack_application.md`, `api_design.md`, `database_design.md`,
`product_design_system.md`, `product_requirements.md`,
`professional_portrait.md`, `product_photography.md`,
`exploratory_analysis.md`, `literature_review.md`,
`competitive_analysis.md`

---

### MEDIUM Templates (20–50 lines)

Solid scaffold with framework, required fields, a concise example, and
best practices.

Required sections:
- Full YAML frontmatter with 3–5 retrieval_keywords
- Purpose (2 sentences)
- When to Retrieve (3+ trigger queries)
- Prompt Framework (structural skeleton)
- Required Context (2–4 `{{VARIABLE}}` fields)
- Optional Configuration (2–3 `[...]` hints)
- Concise Example Prompt (10–20 lines)
- Best Practices (3–5 rules)

Applies to: all remaining templates not marked DEEP or LIGHTWEIGHT.

---

### LIGHTWEIGHT Templates (10–20 lines)

Fast-retrieval, fill-and-go templates for simple, high-frequency tasks.

Required sections:
- YAML frontmatter with 3 retrieval_keywords
- Purpose (1 sentence)
- Required Context (1–3 `{{VARIABLE}}` fields)
- Full Template (compact, ready-to-fill)
- Best Practices (2–3 rules)

Applies to:
`accessibility_review.md`, `social_media_campaign.md`,
`quiz_generator.md`, `concept_explainer.md`,
`executive_summary.md`, `email_communication.md`,
`meeting_agenda.md`, `weekly_review.md`

---

## CATEGORY-SPECIFIC INSTRUCTIONS

### `software_development/`

**`full_stack_application.md`** — DEEP

Framework structure:
```
[AGENT ROLE]          Senior Software Architect
[PROJECT IDENTITY]    {{PROJECT_NAME}}, {{PROJECT_DESCRIPTION}}
[TECH STACK]          {{TECH_STACK}}
[ARCHITECTURE]        [Monolith | Microservices | Serverless]
[REQUIREMENTS]        Functional + Non-functional
[CONSTRAINTS]         Timeline, Budget, Team size
[DELIVERABLES]        File structure, API contracts, DB schema, README
[OUTPUT FORMAT]       Structured technical spec
```

Include: system architecture patterns, scalability considerations,
folder structure conventions, API versioning, auth patterns.
Reference domains: SaaS apps, internal tools, marketplaces, dashboards.

---

**`api_design.md`** — DEEP

Framework structure:
```
[AGENT ROLE]          API Design Expert & REST/GraphQL Specialist
[API PURPOSE]         {{API_PURPOSE}}
[RESOURCE MODEL]      {{PRIMARY_RESOURCES}}
[AUTH STRATEGY]       [JWT | OAuth2 | API Key | Session]
[VERSIONING]          [URI versioning | Header versioning]
[STANDARDS]           RESTful conventions, HTTP status codes, pagination
[ERROR HANDLING]      Structured error responses
[OUTPUT]              OpenAPI spec + endpoint documentation
```

Include: endpoint naming conventions, idempotency, rate limiting,
response envelope patterns, HATEOAS optional guidance.

---

**`database_design.md`** — DEEP

Framework structure:
```
[AGENT ROLE]          Database Architect
[SYSTEM DOMAIN]       {{SYSTEM_DOMAIN}}
[DB TYPE]             [PostgreSQL | MySQL | MongoDB | Mixed]
[ENTITIES]            {{PRIMARY_ENTITIES}}
[RELATIONSHIPS]       One-to-many, Many-to-many patterns
[NORMALISATION]       [1NF through BCNF guidance]
[INDEXING STRATEGY]   Query-pattern based
[OUTPUT]              ERD description, DDL SQL, normalisation notes
```

---

**`code_review.md`** — MEDIUM

Framework: Reviewer role, codebase language, review depth
(security | performance | maintainability | all), specific concerns,
output as structured review with severity levels (critical / warning / info).

---

**`security_audit.md`** — MEDIUM

Framework: Security auditor role, application type, threat model,
OWASP Top 10 checklist reference, output as audit report with
risk ratings (Critical | High | Medium | Low).

---

**`testing_strategy.md`** — MEDIUM

Framework: QA Architect role, application type, test pyramid
(unit / integration / e2e), coverage targets, CI/CD integration,
output as testing plan with tool recommendations.

---

### `uiux_design/`

**`product_design_system.md`** — DEEP

Framework structure:
```
[AGENT ROLE]          Senior Product Designer & Design Systems Architect
[PRODUCT]             {{PRODUCT_NAME}}, {{PRODUCT_TYPE}}
[BRAND TONE]          {{BRAND_TONE}}
[TARGET USERS]        {{TARGET_AUDIENCE}}
[DESIGN TOKENS]       Colors, Typography, Spacing, Elevation
[COMPONENT LIBRARY]   Atoms → Molecules → Organisms
[ACCESSIBILITY]       WCAG 2.1 AA minimum
[OUTPUT]              Design system specification document
```

Include: token naming conventions, component variants, dark mode
considerations, responsive breakpoints, animation principles.

---

**`user_research.md`** — MEDIUM

Framework: UX Researcher role, product stage, research method
[Interviews | Surveys | Usability Tests | Card Sorting],
participant profile, research questions, output as research plan
with discussion guide.

---

**`wireframe_specification.md`** — MEDIUM

Framework: Product Designer role, screen/feature name, user flow,
key interactions, content hierarchy, annotations for developers,
output as structured wireframe specification.

---

**`accessibility_review.md`** — LIGHTWEIGHT

Framework: Accessibility Auditor role, component/page name, WCAG level target,
output as checklist with pass/fail and remediation steps.

---

### `content_creation/`

**`linkedin_post.md`** — MEDIUM

Framework:
```
[AGENT ROLE]     LinkedIn Content Strategist
[AUTHOR VOICE]   {{AUTHOR_BACKGROUND}}
[TOPIC]          {{POST_TOPIC}}
[GOAL]           [Thought leadership | Job search | Network building | Promotion]
[TONE]           [Professional | Conversational | Storytelling | Data-driven]
[HOOK TYPE]      [Question | Bold statement | Personal story | Statistic]
[CTA]            {{CALL_TO_ACTION}}
[LENGTH]         [Short 150w | Medium 300w | Long 600w]
```

Include: hook-body-CTA structure, hashtag strategy (3–5 max),
line break rhythm for LinkedIn formatting, engagement triggers.

---

**`technical_blog.md`** — MEDIUM

Framework: Technical Writer role, topic, target reader (junior/mid/senior dev),
outline structure (problem → solution → implementation → conclusion),
code example inclusion, SEO keyword target, output as full blog draft.

---

**`documentation.md`** — MEDIUM

Framework: Technical Documentation Writer role, doc type
[API Docs | README | User Guide | Architecture Doc], audience,
tone (formal/informal), sections required, output format
(Markdown / Docusaurus / Sphinx compatible).

---

**`social_media_campaign.md`** — LIGHTWEIGHT

Required: `{{BRAND_NAME}}`, `{{CAMPAIGN_GOAL}}`, `{{PLATFORM}}`.
Output: 5 post variants with captions, hashtags, and posting schedule.

---

### `learning/`

**`tutor_session.md`** — MEDIUM

Framework:
```
[AGENT ROLE]         Expert Tutor in {{SUBJECT}}
[STUDENT PROFILE]    {{STUDENT_BACKGROUND}}
[LEARNING GOAL]      {{LEARNING_OBJECTIVE}}
[DIFFICULTY]         [Choose: Beginner | Intermediate | Advanced]
[TEACHING STYLE]     [Socratic | Direct Instruction | Project-based]
[SESSION LENGTH]     [30 min | 60 min | Open-ended]
[EXAMPLES]           Real-world analogies preferred
[ASSESSMENT]         End-of-session comprehension check
```

---

**`study_plan.md`** — MEDIUM

Framework: Study Coach role, subject/exam, available weeks,
daily hours, prior knowledge level, learning resources available,
output as week-by-week plan with daily tasks, milestones, and review sessions.

---

**`quiz_generator.md`** — LIGHTWEIGHT

Required: `{{TOPIC}}`, `{{DIFFICULTY}}`, `{{QUESTION_COUNT}}`.
Output: MCQ / Short-answer / True-False mix with answer key.

---

**`concept_explainer.md`** — LIGHTWEIGHT

Required: `{{CONCEPT}}`, `{{AUDIENCE_LEVEL}}`.
Output: Plain-language explanation + analogy + 1 worked example.

---

### `business/`

**`product_requirements.md`** — DEEP

Framework structure:
```
[AGENT ROLE]          Senior Product Manager
[PRODUCT NAME]        {{PRODUCT_NAME}}
[PROBLEM STATEMENT]   {{PROBLEM_STATEMENT}}
[TARGET USERS]        {{TARGET_AUDIENCE}}
[SUCCESS METRICS]     {{SUCCESS_METRICS}}
[SCOPE]               In-scope features | Out-of-scope exclusions
[REQUIREMENTS]        Functional (user stories) + Non-functional (performance, security)
[DEPENDENCIES]        {{DEPENDENCIES}}
[TIMELINE]            {{TIMELINE}}
[OUTPUT FORMAT]       Full PRD document with epics and user stories
```

---

**`market_analysis.md`** — MEDIUM

Framework: Market Research Analyst role, industry/domain, geographic focus,
analysis depth [Surface | Detailed | Deep Dive], competitors to include,
output as structured report with TAM/SAM/SOM, competitive landscape,
SWOT, and opportunities.

---

**`executive_summary.md`** — LIGHTWEIGHT

Required: `{{DOCUMENT_TYPE}}`, `{{CORE_TOPIC}}`, `{{AUDIENCE}}`.
Output: 250-word max executive summary with 3 key takeaways.

---

**`email_communication.md`** — LIGHTWEIGHT

Required: `{{EMAIL_PURPOSE}}`, `{{RECIPIENT_ROLE}}`, `{{SENDER_CONTEXT}}`.
Optional: `[Tone: Formal | Semi-formal | Friendly]`.
Output: Subject line + email body with clear CTA.

---

### `productivity/`

**`task_breakdown.md`** — MEDIUM

Framework: Productivity Coach + Project Manager role, goal/project description,
deadline, team size, complexity level, output as WBS (Work Breakdown Structure)
with tasks, subtasks, time estimates, and priority tags (P1/P2/P3).

---

**`meeting_agenda.md`** — LIGHTWEIGHT

Required: `{{MEETING_PURPOSE}}`, `{{ATTENDEES}}`, `{{DURATION}}`.
Output: Timed agenda with discussion points, decision items, and action-item template.

---

**`weekly_review.md`** — LIGHTWEIGHT

Required: `{{ROLE}}`, `{{WEEK_GOALS}}`.
Output: Structured weekly review template with wins, blockers, learnings,
and next-week priorities.

---

### `image_generation/`

> **Reference file:** `_case_studies/image_generation_example.md`
> (sourced from `portrait_gen.md` — the professional portrait prompt you provided)
> Use this as the gold-standard depth and style for all image generation templates.

**`professional_portrait.md`** — DEEP

This is the reference template. Structure identically to `portrait_gen.md`
but generalize it into a reusable framework:

Framework sections to include:
```
[AGENT ROLE]         Professional Portrait & Retouching Expert
[IDENTITY REFERENCE] {{REFERENCE_IMAGE_DESCRIPTION}}
[SUBJECT]            {{PERSON_DESCRIPTION}}
[CLOTHING & STYLING] {{OUTFIT_DESCRIPTION}}
[POSE & EXPRESSION]  Confidence level, eye contact, posture
[BACKGROUND]         {{BACKGROUND_COLOR}} — solid studio backdrop
[LIGHTING]           Setup type [Studio Key | Rembrandt | Split | Flat]
[COLOR & MOOD]       {{COLOR_PALETTE_MOOD}}
[COMPOSITION]        [Headshot | Chest-up | Waist-up | Full body]
[RETOUCHING RULES]   Natural skin, no plastic look, preserve texture
[CONSTRAINTS]        No cartoon, no stylization, no cinematic grading
[OUTPUT QUALITY]     LinkedIn / portfolio / magazine ready
```

---

**`product_photography.md`** — DEEP

Framework sections:
```
[AGENT ROLE]         Commercial Product Photographer
[PRODUCT]            {{PRODUCT_NAME}}, {{PRODUCT_CATEGORY}}
[SHOT TYPE]          [Hero shot | Lifestyle | Flat lay | 360 | Detail macro]
[BACKGROUND]         {{BACKGROUND_STYLE}} [White studio | Lifestyle scene | Abstract]
[LIGHTING]           [Soft box | Rim light | Natural window | Dramatic]
[MOOD & TONE]        {{BRAND_MOOD}} [Luxury | Minimal | Playful | Technical]
[PROPS]              {{PROP_DESCRIPTION}} [None | Brand-consistent items]
[COMPOSITION]        Rule of thirds, negative space usage
[COLOR GRADE]        {{COLOR_GRADE}} [Clean neutral | Warm | Cool editorial]
[OUTPUT]             E-commerce ready / campaign ready
```

---

**`brand_illustration.md`** — MEDIUM

Framework: Illustrator/Brand Designer role, brand name and values,
illustration style [Flat | Isometric | Line art | Character],
color palette reference, use case [Website hero | Social | Print],
output as detailed illustration prompt.

---

**`ui_mockup_visual.md`** — MEDIUM

Framework: UI Designer role, app/platform type, screen to visualize,
device frame [Mobile | Desktop | Tablet], color scheme, component list,
output as visual mockup prompt for image generation tools.

---

### `data_analysis/`

**`exploratory_analysis.md`** — DEEP

Framework structure:
```
[AGENT ROLE]          Senior Data Analyst
[DATASET]             {{DATASET_DESCRIPTION}}
[DOMAIN]              {{BUSINESS_DOMAIN}}
[ANALYSIS GOAL]       {{ANALYSIS_OBJECTIVE}}
[DATA SHAPE]          {{ROW_COUNT}} rows, {{COLUMN_COUNT}} columns, key fields: {{KEY_FIELDS}}
[TECHNIQUES]          Distribution analysis, correlation, outlier detection, missing values
[VISUALIZATIONS]      Histogram, scatter, heatmap, box plot as appropriate
[STATISTICAL DEPTH]   [Descriptive only | Inferential | Predictive]
[OUTPUT FORMAT]       EDA report with findings, hypotheses, and recommended next steps
```

---

**`dashboard_design.md`** — MEDIUM

Framework: Data Visualization Expert role, dashboard purpose, target audience
(executive / operational / analytical), KPIs to display, data refresh frequency,
tool target [Tableau | Power BI | Grafana | Custom],
output as dashboard specification with chart type recommendations.

---

**`insight_report.md`** — MEDIUM

Framework: Business Intelligence Analyst role, data domain, reporting period,
key metrics, audience level [Executive | Manager | Technical],
output as narrative insight report with headline numbers,
trend analysis, and action recommendations.

---

### `research/`

**`literature_review.md`** — DEEP

Framework structure:
```
[AGENT ROLE]          Research Analyst & Academic Writing Expert
[TOPIC]               {{RESEARCH_TOPIC}}
[SCOPE]               {{SCOPE_BOUNDARIES}}
[TIME RANGE]          {{PUBLICATION_YEAR_RANGE}}
[DEPTH]               [Surface overview | Standard review | Systematic review]
[STRUCTURE]           Introduction → Thematic sections → Gaps → Conclusion
[CITATION STYLE]      [APA | IEEE | MLA | Chicago]
[SOURCE TYPES]        [Peer-reviewed only | Industry reports included | All sources]
[OUTPUT]              Full literature review draft with section headings and source placeholders
```

---

**`competitive_analysis.md`** — DEEP

Framework structure:
```
[AGENT ROLE]          Competitive Intelligence Analyst
[PRODUCT/COMPANY]     {{SUBJECT}}
[COMPETITORS]         {{COMPETITOR_LIST}}
[ANALYSIS DIMENSIONS] Features, Pricing, Market Position, UX, Growth Signals
[FRAMEWORK]           [SWOT | Porter's Five Forces | Feature Matrix | All]
[DATA SOURCES]        [Public only | Include estimates]
[OUTPUT]              Structured competitive analysis report with comparison table
```

---

**`topic_deep_dive.md`** — MEDIUM

Framework: Subject Matter Expert role, topic, prior knowledge level of requester,
depth [Conceptual | Technical | Exhaustive], output format
[Essay | Bullet summary | Q&A | Concept map description],
include sub-topics, related concepts, and recommended next-reading.

---

### `_frameworks/` — Reference Documents (No Placeholders)

**`prompt_frameworks.md`** — REFERENCE

Create a master reference document containing all universal framework
templates used across the knowledge base:

Sections to include:
1. Universal Prompt Framework (Role → Purpose → Capabilities → Constraints → Output)
2. Development Framework
3. Design Framework
4. Learning Framework
5. Business Communication Framework
6. Research Framework
7. Image Generation Framework
8. Data Analysis Framework

Each framework: skeleton structure + 3-line explanation of when to use it.

---

**`prompt_best_practices.md`** — REFERENCE

Create a comprehensive best practices reference:

Sections:
1. Role Assignment (explicit vs. implicit)
2. Constraint Specification
3. Output Format Definition
4. Context vs. Instruction Separation
5. Placeholder Usage Rules (`{{...}}` vs. `[...]`)
6. Chain-of-Thought Triggers
7. Length and Specificity Calibration
8. Avoiding Ambiguity
9. RAG-Optimized Writing (for knowledge base documents)
10. Common Anti-Patterns

---

### `_case_studies/` — Preserved Reference Examples

**`image_generation_example.md`**

Take the provided `portrait_gen.md` file exactly as-is.
Prepend it with proper YAML frontmatter:

```yaml
---
title: Professional Studio Portrait — Reference Case Study
category: image_generation
subcategory: professional_portrait
tags:
  - portrait
  - studio-photography
  - professional-branding
  - retouching
  - linkedin
difficulty: intermediate
depth: deep
retrieval_keywords:
  - professional portrait
  - studio photography
  - linkedin photo
  - corporate headshot
  - brand photography
use_case: >
  Retrieve when user wants a professional, studio-quality portrait prompt
  for branding, LinkedIn, or corporate use.
placeholder_count: 3
version: "1.0"
source: user_provided
---
```

Then append the full `portrait_gen.md` content unchanged.

---

**`latex_beamer_example.md`**

Take the provided `latex_beamer_master_prompt.md` exactly as-is.
Prepend it with YAML frontmatter:

```yaml
---
title: LaTeX Beamer Presentation — Master Prompt Reference
category: research
subcategory: academic_writing
tags:
  - latex
  - beamer
  - academic
  - presentation
  - technical-writing
difficulty: advanced
depth: deep
retrieval_keywords:
  - latex presentation
  - beamer slides
  - academic slides
  - technical presentation
  - PDF slide deck
use_case: >
  Retrieve when user wants to generate LaTeX Beamer presentation prompts
  for academic, technical, or research contexts.
placeholder_count: 12
version: "1.0"
source: user_provided
---
```

Then append the full `latex_beamer_master_prompt.md` content unchanged.

---

## GENERATION RULES — AGENT MUST FOLLOW ALL

1. **Every file gets a unique YAML frontmatter block.** No file is missing
   title, category, tags, difficulty, depth, or retrieval_keywords.

2. **retrieval_keywords must be semantically rich.** Think: what would a user
   *say* that should retrieve this file? Include synonyms, related terms,
   and action verbs. Minimum 3, target 5–7.

3. **No invented filler content.** If example content for a specific domain
   is needed, use realistic, domain-accurate placeholders. Never generate
   lorem ipsum or obviously fake data.

4. **Placeholder consistency is mandatory.** `{{VARIABLE}}` = required,
   `[hint]` = optional. Never mix them up. Never use `<angle brackets>` or
   `(parentheses)` for template variables.

5. **Every DEEP template must include a fully-filled example prompt.**
   The example must demonstrate the template being used for a specific,
   realistic scenario (not a generic placeholder scenario).

6. **Depth markers must be respected.** DEEP files must be 50–150 lines.
   MEDIUM files 20–50 lines. LIGHTWEIGHT files 10–20 lines.
   Do not compress DEEP files or pad LIGHTWEIGHT files.

7. **Section headers must be consistent** across all files of the same depth tier:
   - DEEP: Purpose / When to Retrieve / Prompt Framework / Required Context /
     Optional Configuration / Full Example Prompt / Best Practices /
     Common Mistakes
   - MEDIUM: Purpose / When to Retrieve / Prompt Framework / Required Context /
     Optional Configuration / Example Prompt / Best Practices
   - LIGHTWEIGHT: Purpose / Required Context / Template / Best Practices

8. **File naming:** All lowercase, underscores for spaces, `.md` extension.
   Match the directory structure exactly as specified above.

9. **`_case_studies/` files:** Do not modify the original prompt content.
   Only prepend the YAML frontmatter block.

10. **`_frameworks/` files:** No `{{VARIABLE}}` placeholders. These are
    reference documents, not templates. Write in clear, instructional prose.

---

## GENERATION ORDER (Recommended)

Generate files in this order to build context incrementally:

```
Pass 1 — Foundations
  _frameworks/prompt_frameworks.md
  _frameworks/prompt_best_practices.md

Pass 2 — Case Studies (preserve originals + add frontmatter)
  _case_studies/image_generation_example.md
  _case_studies/latex_beamer_example.md

Pass 3 — Deep Templates (highest value, do these carefully)
  software_development/full_stack_application.md
  software_development/api_design.md
  software_development/database_design.md
  uiux_design/product_design_system.md
  business/product_requirements.md
  image_generation/professional_portrait.md
  image_generation/product_photography.md
  data_analysis/exploratory_analysis.md
  research/literature_review.md
  research/competitive_analysis.md

Pass 4 — Medium Templates
  (all remaining medium-depth files)

Pass 5 — Lightweight Templates
  (all remaining lightweight files)
```

---

## FINAL DELIVERABLE

A complete `knowledge_base/` directory containing exactly **33 `.md` files**
organized into the folder structure above, where:

- Every file is RAG-ready (frontmatter metadata + semantic body)
- Every template uses the `{{VARIABLE}}` / `[hint]` placeholder convention
- Deep templates are production-ready and immediately usable
- Case study files preserve the original prompts with added frontmatter
- The `_frameworks/` files serve as reference documentation for the
  retrieval system

This knowledge base should be ready to chunk, embed, and load into a
vector database without any post-processing.
