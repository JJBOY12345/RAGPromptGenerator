# PromptForge AI — Reference Resources Appendix

> **Append this section to the bottom of `promptforge_kb_agent_prompt.md`.**
> These are the authoritative, publicly accessible URLs the agent must consult
> before generating templates in each category. They are grouped by what they
> inform — not by category folder — because many resources cross categories.

---

## HOW THE AGENT SHOULD USE THESE LINKS

For each template you generate, identify which resource tier applies and:

1. **Fetch the URL** before writing the template.
2. **Extract the structural conventions** — section names, field names,
   output formats, standard terminology — from that source.
3. **Reflect those conventions** in the Prompt Framework section of the template.
4. **Do not invent domain terminology.** If the standard uses a specific term
   (e.g., OpenAPI uses "paths", "components", "schemas" — not "routes" or
   "models"), the template must use that term.

---

## TIER 1 — PROMPT ENGINEERING FOUNDATIONS
*(Read before generating ANY template)*

These are the methodological foundations. The agent must internalize these
before writing a single template — they define what a well-structured
prompt looks like across all domains.

| Resource | URL | What to extract |
|---|---|---|
| **Anthropic Prompt Engineering Docs** | `https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview` | Role assignment, XML structure, chain-of-thought triggers, output format specification, Claude-specific best practices |
| **Anthropic Prompt Library** | `https://docs.anthropic.com/en/prompt-library/library` | Ready-made template patterns, task-specific prompt structures, tone calibration across domains |
| **OpenAI Prompt Engineering Guide** | `https://platform.openai.com/docs/guides/prompt-engineering` | Instruction authority levels, few-shot prompting, system vs user message design, production prompt patterns |
| **DAIR.AI Prompt Engineering Guide** | `https://www.promptingguide.ai/` | Zero-shot, few-shot, CoT, ReAct, meta-prompting techniques; academic research grounding |
| **DAIR.AI GitHub Repository** | `https://github.com/dair-ai/Prompt-Engineering-Guide` | Raw technique guides, papers, notebooks for advanced prompting methods |
| **Learn Prompting** | `https://learnprompting.org/docs/intro` | Structured curriculum covering role prompting, output formatting, personas, chaining |

---

## TIER 2 — RAG & KNOWLEDGE BASE FORMATTING
*(Read before generating ANY template — affects document structure)*

These define how knowledge base documents should be structured for
optimal retrieval. The agent's frontmatter and section design should
reflect these principles.

| Resource | URL | What to extract |
|---|---|---|
| **LlamaIndex RAG Guide** | `https://docs.llamaindex.ai/en/stable/getting_started/concepts/` | Node/chunk design, metadata filtering, document structure for retrieval, index types |
| **LlamaIndex Advanced RAG Cheat Sheet** | `https://www.llamaindex.ai/blog/a-cheat-sheet-and-some-recipes-for-building-advanced-rag-803a9d94c41b` | Chunk size optimization, retrieval strategies, query-document alignment |
| **Weaviate Chunking Strategies Guide** | `https://weaviate.io/blog/chunking-strategies-for-rag` | Markdown-aware chunking, structural splitting, when to use semantic vs recursive chunking |
| **LangChain Text Splitters Docs** | `https://python.langchain.com/docs/concepts/text_splitters/` | MarkdownHeaderTextSplitter behavior — directly affects how agent-generated `.md` files will be chunked |
| **Firecrawl Chunking Best Practices** | `https://www.firecrawl.dev/blog/best-chunking-strategies-rag` | 2025/2026 benchmarked strategies; practical defaults (256–512 tokens, 10–20% overlap) |

**Key principle extracted from these sources:**
> Use semantic section headers (H2/H3) as natural chunk boundaries.
> Each section in a knowledge base document should be independently
> retrievable and self-contained. The YAML frontmatter functions as
> document-level metadata for pre-retrieval filtering.

---

## TIER 3 — DOMAIN STANDARDS BY CATEGORY
*(Read the relevant links before generating templates in that category)*

### `software_development/`

| Resource | URL | Applies to |
|---|---|---|
| **OpenAPI Specification (OAS 3.1)** | `https://spec.openapis.org/oas/v3.1.0` | `api_design.md` — use OAS field names: paths, components, schemas, parameters, responses |
| **OpenAPI GitHub Repository** | `https://github.com/OAI/OpenAPI-Specification` | `api_design.md` — canonical spec source |
| **Google API Design Guide** | `https://cloud.google.com/apis/design` | `api_design.md` — REST resource naming, HTTP method semantics, error model |
| **REST API Design Best Practices** | `https://restfulapi.net/` | `api_design.md` — URI structure, idempotency, pagination conventions |
| **The Twelve-Factor App** | `https://12factor.net/` | `full_stack_application.md` — configuration, backing services, build/release/run separation |
| **OWASP Top 10 (2021)** | `https://owasp.org/www-project-top-ten/` | `security_audit.md` — use OWASP categories as the audit checklist scaffold |
| **OWASP Testing Guide** | `https://owasp.org/www-project-web-security-testing-guide/` | `security_audit.md` — structured testing methodology |
| **Google Testing Blog** | `https://testing.googleblog.com/` | `testing_strategy.md` — test pyramid, flakiness patterns, CI integration |
| **PostgreSQL Documentation** | `https://www.postgresql.org/docs/current/` | `database_design.md` — DDL syntax, index types, normalization terminology |

---

### `uiux_design/`

| Resource | URL | Applies to |
|---|---|---|
| **Nielsen Norman Group Articles** | `https://www.nngroup.com/articles/` | `user_research.md`, `wireframe_specification.md` — UX heuristics, research methodology, usability testing standards |
| **WCAG 2.2 Official Standard** | `https://www.w3.org/TR/WCAG22/` | `accessibility_review.md`, `product_design_system.md` — use WCAG success criteria (A/AA/AAA) as the audit framework |
| **W3C WAI Accessibility Overview** | `https://www.w3.org/WAI/standards-guidelines/` | `accessibility_review.md` — POUR principles (Perceivable, Operable, Understandable, Robust) |
| **Material Design 3 Guidelines** | `https://m3.material.io/` | `product_design_system.md` — design token naming conventions, component anatomy, spacing systems |
| **Apple Human Interface Guidelines** | `https://developer.apple.com/design/human-interface-guidelines/` | `product_design_system.md` — platform-specific design principles, accessibility integration |
| **Figma Design Systems Guide** | `https://www.figma.com/best-practices/team-file-organization/` | `product_design_system.md` — file organization, component library structure |

---

### `content_creation/`

| Resource | URL | Applies to |
|---|---|---|
| **LinkedIn Creator Guide** | `https://www.linkedin.com/help/linkedin/answer/a524076` | `linkedin_post.md` — native formatting, algorithm-friendly structure, character limits |
| **Google Search Central (SEO Docs)** | `https://developers.google.com/search/docs/fundamentals/creating-helpful-content` | `technical_blog.md` — helpful content principles, E-E-A-T signals, structured content |
| **Write the Docs Style Guide Resources** | `https://www.writethedocs.org/guide/` | `documentation.md` — docs-as-code philosophy, information architecture, style guides |
| **Divio Documentation System** | `https://documentation.divio.com/` | `documentation.md` — the 4-quadrant model: tutorials / how-tos / reference / explanation |

---

### `learning/`

| Resource | URL | Applies to |
|---|---|---|
| **Bloom's Taxonomy (Vanderbilt CFT)** | `https://cft.vanderbilt.edu/guides-sub-pages/blooms-taxonomy/` | `tutor_session.md`, `study_plan.md` — use Bloom's levels (Remember → Create) to calibrate learning objectives |
| **Spaced Repetition Research (Gwern)** | `https://gwern.net/spaced-repetition` | `study_plan.md` — evidence-based review intervals, forgetting curve |
| **Cognitive Load Theory (overview)** | `https://www.instructionaldesign.org/theories/cognitive-load/` | `tutor_session.md`, `concept_explainer.md` — chunking information, worked examples, reducing extraneous load |

---

### `business/`

| Resource | URL | Applies to |
|---|---|---|
| **Shape Up (Basecamp PRD methodology)** | `https://basecamp.com/shapeup` | `product_requirements.md` — appetite, betting, pitch structure; alternative to traditional PRD |
| **Silicon Valley PRD Template (Shreyas Doshi)** | `https://twitter.com/shreyas/status/1287180837526052864` | `product_requirements.md` — modern PM perspective on what PRDs should contain |
| **Y Combinator Startup School Resources** | `https://www.startupschool.org/library` | `market_analysis.md`, `executive_summary.md` — investor-grade framing of market size and opportunity |
| **McKinsey Pyramid Principle** | `https://www.myconsultingoffer.org/case-study-interview-prep/pyramid-principle/` | `executive_summary.md` — SCQA (Situation, Complication, Question, Answer) structure |
| **Paul Graham Essays on Startups** | `https://paulgraham.com/articles.html` | `product_requirements.md`, `market_analysis.md` — first-principles thinking on product and markets |

---

### `productivity/`

| Resource | URL | Applies to |
|---|---|---|
| **Getting Things Done (GTD) Summary** | `https://gettingthingsdone.com/what-is-gtd/` | `task_breakdown.md`, `weekly_review.md` — capture → clarify → organize → review → engage |
| **Work Breakdown Structure Guide (PMI)** | `https://www.pmi.org/learning/library/applying-work-breakdown-structure-project-lifecycle-6161` | `task_breakdown.md` — WBS decomposition rules, 100% rule, work packages |
| **Eisenhower Matrix (Asana)** | `https://asana.com/resources/eisenhower-matrix` | `task_breakdown.md` — priority classification (urgent/important quadrants) |

---

### `image_generation/`

| Resource | URL | Applies to |
|---|---|---|
| **Midjourney Prompt Guide (Official Docs)** | `https://docs.midjourney.com/hc/en-us/articles/32952963362963-Prompting` | All image gen templates — parameter structure, style descriptors, technical quality terms |
| **Stable Diffusion Prompt Guide (Civitai)** | `https://civitai.com/articles/2056` | All image gen templates — negative prompt conventions, quality tags, LoRA references |
| **OpenAI DALL-E Prompt Guide** | `https://platform.openai.com/docs/guides/images/prompting` | All image gen templates — composition language, style descriptors compatible with GPT image models |
| **Adobe Stock Photography Guidelines** | `https://helpx.adobe.com/stock/contributor/help/photography-guidelines.html` | `professional_portrait.md`, `product_photography.md` — commercial photography standards |
| **Your Reference: portrait_gen.md** | *(user-provided — see `_case_studies/`)* | `professional_portrait.md` — gold standard depth and structure for this project |

---

### `data_analysis/`

| Resource | URL | Applies to |
|---|---|---|
| **Towards Data Science EDA Guide** | `https://towardsdatascience.com/exploratory-data-analysis-8fc1cb20fd15` | `exploratory_analysis.md` — standard EDA workflow: shape, dtypes, missing values, distributions, correlations |
| **Storytelling with Data (book summary)** | `https://www.storytellingwithdata.com/chart-guide` | `dashboard_design.md`, `insight_report.md` — chart selection guide, data-ink ratio, annotation |
| **Tableau Visual Analytics Best Practices** | `https://www.tableau.com/learn/articles/best-practices-for-dashboard-design` | `dashboard_design.md` — KPI layout, hierarchy of information, filter placement |
| **Google Data Analytics Certificate Glossary** | `https://www.coursera.org/professional-certificates/google-data-analytics` | `exploratory_analysis.md` — standardized data analysis terminology |

---

### `research/`

| Resource | URL | Applies to |
|---|---|---|
| **PRISMA Guidelines (Systematic Reviews)** | `https://www.prisma-statement.org/` | `literature_review.md` — gold standard for systematic literature review methodology |
| **Purdue OWL Research Writing Guide** | `https://owl.purdue.edu/owl/research_and_citation/` | `literature_review.md` — citation formats (APA, MLA, Chicago, IEEE), literature review structure |
| **Harvard Business Review on Competitive Analysis** | `https://hbr.org/topic/subject/competitive-strategy` | `competitive_analysis.md` — Porter's Five Forces, competitive positioning frameworks |
| **MindTools SWOT Analysis Guide** | `https://www.mindtools.com/amtbj63/swot-analysis` | `competitive_analysis.md` — SWOT structure and usage in competitive context |
| **arXiv (for AI/ML research templates)** | `https://arxiv.org/` | `literature_review.md` in research contexts — preprint structure, abstract conventions |

---

## TIER 4 — META REFERENCES
*(For `_frameworks/` documents only)*

| Resource | URL | What to extract |
|---|---|---|
| **LangChain Prompt Templates Docs** | `https://python.langchain.com/docs/concepts/prompt_templates/` | How prompts are programmatically structured, variable injection patterns |
| **LlamaIndex Prompt Engineering Guide** | `https://docs.llamaindex.ai/en/stable/optimizing/custom_prompts/` | Prompt customization in RAG pipelines, template variable conventions |
| **PromptHub Blog** | `https://www.prompthub.us/blog` | Real-world prompt patterns, production prompt engineering case studies |
| **Anthropic Claude Prompt Examples** | `https://docs.anthropic.com/en/prompt-library/library` | Reference examples for what production-ready Claude prompts look like |

---

## QUICK REFERENCE: WHICH LINKS PER TEMPLATE

| Template File | Must Fetch Before Writing |
|---|---|
| `full_stack_application.md` | Anthropic Prompt Docs + 12factor.net |
| `api_design.md` | OpenAPI spec + Google API Design Guide |
| `database_design.md` | PostgreSQL docs + Anthropic Prompt Docs |
| `security_audit.md` | OWASP Top 10 + OWASP Testing Guide |
| `testing_strategy.md` | Google Testing Blog |
| `product_design_system.md` | Material Design 3 + WCAG 2.2 + Nielsen Norman |
| `user_research.md` | Nielsen Norman + NNG Articles |
| `wireframe_specification.md` | Nielsen Norman Articles |
| `accessibility_review.md` | WCAG 2.2 + W3C WAI |
| `linkedin_post.md` | LinkedIn Creator Guide |
| `technical_blog.md` | Google Search Central |
| `documentation.md` | Divio System + Write the Docs |
| `tutor_session.md` | Bloom's Taxonomy + Cognitive Load Theory |
| `study_plan.md` | Bloom's Taxonomy + Spaced Repetition |
| `product_requirements.md` | Shape Up + Shreyas Doshi PRD |
| `market_analysis.md` | YC Startup School + Paul Graham Essays |
| `executive_summary.md` | McKinsey Pyramid Principle |
| `task_breakdown.md` | PMI WBS Guide + GTD + Eisenhower Matrix |
| `professional_portrait.md` | Midjourney Docs + portrait_gen.md case study |
| `product_photography.md` | Midjourney Docs + Adobe Stock Guidelines |
| `brand_illustration.md` | Midjourney Docs + DALL-E Guide |
| `ui_mockup_visual.md` | DALL-E Guide + Material Design 3 |
| `exploratory_analysis.md` | TDS EDA Guide |
| `dashboard_design.md` | Tableau Best Practices + Storytelling with Data |
| `insight_report.md` | Storytelling with Data + McKinsey Pyramid |
| `literature_review.md` | PRISMA + Purdue OWL |
| `competitive_analysis.md` | HBR Competitive Strategy + MindTools SWOT |
| `topic_deep_dive.md` | Bloom's Taxonomy + Cognitive Load |
| `_frameworks/prompt_frameworks.md` | Anthropic Docs + DAIR.AI + LangChain Templates |
| `_frameworks/prompt_best_practices.md` | Anthropic Docs + OpenAI PE Guide + DAIR.AI |

---

*End of Resource Appendix — append above to the main agent prompt.*
