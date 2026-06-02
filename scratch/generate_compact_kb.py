import os

KB_DIR = r"c:\Users\jeswin\Documents\College Stuff\RAG_workshop\knowledge_base"

# Ensure all subdirectories exist
for subdir in ["software_development", "uiux_design", "content_creation", "learning", "business", "productivity", "image_generation", "data_analysis", "research"]:
    os.makedirs(os.path.join(KB_DIR, subdir), exist_ok=True)

# 1. DEEP TEMPLATES (With corrected placeholder counts in frontmatter)
deep_updates = {
    r"software_development\full_stack_application.md": """---
title: Full Stack Application Blueprint Generator
category: software_development
subcategory: application_architecture
tags:
  - architecture
  - system-design
  - software-engineering
  - technical-specification
  - project-scaffolding
difficulty: advanced
depth: deep
retrieval_keywords:
  - full stack application
  - system architecture blueprint
  - project scaffolding
  - software architecture design
  - technical specification document
  - folder structure generator
use_case: >
  Retrieve this template when the user wants to generate a complete,
  end-to-end full-stack software architecture plan and boilerplate setup.
placeholder_count: 3
version: "1.0"
---

# Full Stack Application Blueprint Generator

## Purpose
This template is used to generate a detailed, professional software architecture blueprint, file tree scaffolding, database schemas, and integration plans for full-stack applications. It bridges the gap between raw concept ideas and structured technical plans, setting a high standard for clean code practices.

## When to Retrieve This Template
- "I want to start a new SaaS application and need an architecture plan."
- "How should I structure my Next.js and Node.js project?"
- "Generate a full-stack technical specification for a marketplace app."
- "Design the architecture and database schema for an internal dashboard."
- "Build a system design blueprint for a high-traffic e-commerce portal."

## Prompt Framework
```markdown
You are a Senior Software Architect & Lead Full-Stack Developer specializing in building secure, scalable, and highly maintainable digital platforms.

### 1. PROJECT SCOPE & IDENTITY
- **App Name:** {{PROJECT_NAME}}
- **Domain Focus:** {{PROJECT_DESCRIPTION}}
- **Tech Stack:** {{TECH_STACK}}
- **Architecture Pattern:** [Choose one: Monolith | Microservices | Serverless | Clean Architecture]

### 2. ARCHITECTURAL REQUIREMENTS
- **Functional Requirements:**
  - Standard CRUD operations for primary models.
  - User authentication and role-based access control.
  - [Optional: Real-time events, background jobs, external integrations]
- **Non-Functional Guarantees:**
  - High availability, modular maintainability, and RESTful API standards.
  - Strict security practices (SQL injection prevention, password hashing, JWT expiration).

### 3. EXPECTED DELIVERABLES
1. **System Architecture Diagram (Mermaid):** Visual flow of frontend, backend, database, and third-party systems.
2. **Directory Structure:** Complete folder layout showing separation of concerns.
3. **Database Schema:** Entity definitions and relationships in DDL SQL or ORM schema.
4. **Core API Routes:** Structured list of routes, HTTP methods, payloads, and success codes.
5. **Security & Scaling Guide:** Core recommendations for auth, caching, and database indexing.
```

## Required Context
- Project Name: {{PROJECT_NAME}}
- Project Description: {{PROJECT_DESCRIPTION}}
- Tech Stack: {{TECH_STACK}}

---

## Optional Configuration
- Complexity: [Choose one: Beginner | Intermediate | Advanced]
- Scale Strategy: [Optional: Simple DB replica | Redis Caching | CDN Assets]
- Testing Suite: [Yes / No]

---

## Full Example Prompt
```markdown
You are a Senior Software Architect & Lead Full-Stack Developer specializing in building secure, scalable, and highly maintainable digital platforms.

### 1. PROJECT SCOPE & IDENTITY
- **App Name:** DevTasker
- **Domain Focus:** A developer-focused project management system with real-time kanban board updates.
- **Tech Stack:** Next.js (App Router), Node.js (Express), PostgreSQL (Prisma ORM), TailwindCSS.
- **Architecture Pattern:** Clean Architecture Monolith

### 2. ARCHITECTURAL REQUIREMENTS
- **Functional Requirements:**
  - Standard CRUD operations for boards, columns, and tasks.
  - User authentication via JWT with session management.
- **Non-Functional Guarantees:**
  - Sub-100ms API response time for Kanban board state transitions.
  - Strict input check.

### 3. EXPECTED DELIVERABLES
1. **System Architecture Diagram (Mermaid):** Visual flow of Next.js client, Express API server, Prisma ORM, and PostgreSQL.
2. **Directory Structure:** Complete folder layout showing separation of client, server, and shared types.
3. **Database Schema:** PostgreSQL Prisma schema showing User, Board, Column, Task, and relations.
4. **Core API Routes:** RESTful endpoints for Kanban column and task updates.
```

## Best Practices
1. **Separation of Concerns:** Keep client-side UI, server logic, and database schemas strictly modularized.
2. **Standardize API Schemas:** Use uniform error response objects containing status, error message, and timestamp.
3. **Enforce Strong Typing:** Ensure TypeScript definitions are shared between frontend endpoints and backend models.
4. **Secure Defaults:** Always configure CORS rules, rate limiters, and helmet headers on server entry points.
5. **Document Setup:** Include a robust `README.md` outline explaining env configurations and db migrations.

## Common Mistakes to Avoid
- **Hardcoding Secrets:** Storing database credentials or JWT keys inside source control. Use environment variables.
- **Tightly Coupled Layers:** Mixing database logic directly inside HTTP controller actions. Use services or repositories.
- **Missing Database Indexes:** Failing to add indexes on highly queried foreign keys (e.g., `user_id`, `board_id`), resulting in poor read performance.
- **Undefined API Errors:** Throwing generic `500 Internal Server Error` without detailed log capture on the backend.
""",

    r"software_development\api_design.md": """---
title: RESTful & OpenAPI API Design Specifier
category: software_development
subcategory: api_design
tags:
  - api-design
  - openapi
  - rest
  - graphql
  - system-integration
difficulty: advanced
depth: deep
retrieval_keywords:
  - api design spec
  - openapi specification
  - rest api developer
  - graphql schema designer
  - endpoint documentation
  - web service contract
use_case: >
  Retrieve when the user is designing APIs, endpoints, webhooks,
  or writing OpenAPI/Swagger technical documentation.
placeholder_count: 3
version: "1.0"
---

# RESTful & OpenAPI API Design Specifier

## Purpose
This template generates professional, industry-standard API designs and OpenAPI 3.1 specifications. It enforces RESTful naming conventions, uniform resource mapping, pagination, error schemas, security strategies, and robust webhook patterns.

## When to Retrieve This Template
- "Design the REST API for a subscription billing platform."
- "Write an OpenAPI 3.1 schema for our user account microservice."
- "Create an API interface spec between our payment processor and backend."
- "How do I structure error payloads and responses for public APIs?"

## Prompt Framework
```markdown
You are a Principal API Architect and REST/GraphQL Integration Specialist. Your goal is to design a secure, production-grade, and self-documenting API.

### 1. API PROFILE & SECURITY
- **Service Name:** {{API_NAME}}
- **Core Purpose:** {{API_PURPOSE}}
- **Resource Model:** {{PRIMARY_RESOURCES}} (comma-separated list)
- **Auth Strategy:** [Choose: JWT Bearer Tokens | OAuth2 Client Credentials | API Keys | Session-based]
- **API Versioning:** [Choose: URI versioning (e.g., /v1/...) | Header-based versioning]

### 2. ARCHITECTURAL PROTOCOLS
- **Resource Naming:** Nouns only, lowercase, plural (e.g., `/users`, `/billing-accounts`).
- **Idempotency & Safety:** Strict enforcement of GET/PUT/DELETE idempotency and POST non-idempotency.
- **Pagination Strategy:** Cursor-based pagination for high-frequency resource streams, offset for static tables.
- **Rate Limiting:** HTTP header definitions (`X-RateLimit-Limit`, `X-RateLimit-Remaining`).

### 3. OUTPUT SPECIFICATION CONTRACTS
1. **OpenAPI 3.1.0 Yaml/JSON Schema:** Full spec including paths, request bodies, components, and securitySchemes.
2. **Detailed Endpoint Profiles:** Request verbs, parameters, exact JSON request/response bodies, and description.
3. **Robust Error Payload Contract:** A strict RFC-7807 problem details JSON schema for all error codes.
```

## Required Context
- API Name: {{API_NAME}}
- API Purpose: {{API_PURPOSE}}
- Primary Resources: {{PRIMARY_RESOURCES}}

---

## Optional Configuration
- Versioning Style: [Optional: Header Versioning | URL Path /v1/]
- Format: [Choose: YAML | JSON]
- Include Webhooks: [Yes / No]

---

## Full Example Prompt
```markdown
You are a Principal API Architect and REST/GraphQL Integration Specialist. Your goal is to design a secure, production-grade, and self-documenting API.

### 1. API PROFILE & SECURITY
- **Service Name:** InvoiceHub API
- **Core Purpose:** Managing client invoicing, invoice lifecycles, and automatic PDF receipt issuance.
- **Resource Model:** clients, invoices, payments
- **Auth Strategy:** JWT Bearer Tokens
- **API Versioning:** URI versioning (e.g., `/v1/...`)

### 2. ARCHITECTURAL PROTOCOLS
- **Resource Naming:** Nouns only, lowercase, plural.
- **Idempotency & Safety:** Strict enforcement of API structures.
- **Pagination Strategy:** Cursor-based pagination using `starting_after` and `limit`.

### 3. OUTPUT SPECIFICATION CONTRACTS
1. **OpenAPI 3.1.0 Yaml/JSON Schema:** Full spec including paths, schemas, and security.
2. **Detailed Endpoint Profiles:** Exact JSON structures for creating, retrieving, and paying invoices.
3. **Robust Error Payload Contract:** Standard JSON error envelopes with code, message, and target details.
```

## Best Practices
1. **Use HTTP Status Semantics:** Return correct codes (`201 Created` for creations, `422 Unprocessable Entity` for validation errors).
2. **CamelCase/snake_case Consistency:** Maintain snake_case keys in all JSON payloads and query parameters across all endpoints.
3. **Secure Headers:** Include security headers (`Content-Type: application/json`, `X-Content-Type-Options: nosniff`) in responses.
4. **Define Schemas in Components:** Keep OpenAPI files clean by defining models inside the `#/components/schemas` section.
5. **Rate Limiting Enforcements:** Return `429 Too Many Requests` when limits are breached with a `Retry-After` header.

## Common Mistakes to Avoid
- **Verb Endpoints:** Creating endpoints like `/getInvoices` or `/createClient` instead of using HTTP methods on nouns.
- **Returning naked arrays:** Returning `[]` as the top level of responses. Always wrap datasets inside an object envelope (`{ "data": [...] }`).
- **Leaking Server Stack traces:** Returning verbose server framework error messages in `500` responses, exposing internals to users.
- **Silent Validation Failures:** Returning `200 OK` for requests that failed semantic validation, forcing client-side parsing.
""",

    r"software_development\database_design.md": """---
title: Relational & NoSQL Database Schema Architect
category: software_development
subcategory: database_design
tags:
  - database-design
  - schema-architecture
  - sql
  - postgresql
  - normalization
difficulty: advanced
depth: deep
retrieval_keywords:
  - database design spec
  - sql schema architect
  - erd relationship diagram
  - database normalization guide
  - query performance indexing
  - postgresql ddl generator
use_case: >
  Retrieve when the user is planning database schema architectures, SQL scripts,
  normalizing data models, or designing indexes for performance.
placeholder_count: 2
version: "1.0"
---

# Relational & NoSQL Database Schema Architect

## Purpose
This template generates highly optimized relational database schemas (focused primarily on PostgreSQL and MySQL) or NoSQL data models. It models strict relationships, normalizes models to 3NF/BCNF, creates robust indexes, and ensures referential integrity via foreign key cascades.

## When to Retrieve This Template
- "Design a PostgreSQL schema for an e-commerce platform with products, orders, and clients."
- "Create an optimized MySQL database for a medical clinic booking system."
- "Write the SQL DDL commands for a school management app database."
- "How do I model a many-to-many relationship with junction tables in SQL?"

## Prompt Framework
```markdown
You are a Principal Database Architect specializing in writing performant, secure, and highly normalized database schemas.

### 1. TARGET DOMAIN & TECH STACK
- **System Domain:** {{SYSTEM_DOMAIN}}
- **Database Engine:** [Choose: PostgreSQL | MySQL | SQLite | MongoDB | mixed hybrid]
- **Key Schema Entities:** {{PRIMARY_ENTITIES}} (comma-separated list)
- **Target Normalization Level:** [Choose: 3NF | BCNF | 2NF (for analytical data warehouses)]

### 2. DATA MODELING STRATEGIES
- **Key Constraints:** Mandatory Primary Keys (UUIDs or BIGSERIAL), non-nullable audit fields (`created_at`, `updated_at`).
- **Referential Integrity:** Enforce explicit FOREIGN KEY constraints with cascading deletions or nullifications where necessary.
- **Indexing Rules:** B-Tree indexes on highly joined foreign keys, unique indices on alternate keys, partial indices for conditional flags.

### 3. EXPECTED DELIVERABLES
1. **Entity-Relationship Diagram (ERD):** Documented textual mapping of tables, columns, constraints, and cardinalities (1:1, 1:N, N:M).
2. **Standard-Compliant SQL DDL Script:** Executable CREATE TABLE scripts, schema scopes, primary/foreign key definitions, and checks.
3. **Indexing Script:** Optimized CREATE INDEX commands matching query workloads.
4. **Normalization & Denormalization Notes:** Brief discussion of BCNF mapping and any intentional performance trade-offs.
```

## Required Context
- System Domain: {{SYSTEM_DOMAIN}}
- Primary Entities: {{PRIMARY_ENTITIES}}

---

## Optional Configuration
- DB Engine: [Choose one: PostgreSQL | MySQL | MongoDB]
- ID Strategy: [Choose: Auto-incrementing BigInt | UUIDv4]
- Add Seed Data: [Yes / No]

---

## Full Example Prompt
```markdown
You are a Principal Database Architect specializing in writing performant, secure, and highly normalized database schemas.

### 1. TARGET DOMAIN & TECH STACK
- **System Domain:** Subscription-based Video Streaming Platform
- **Database Engine:** PostgreSQL
- **Key Schema Entities:** users, subscriptions, plans, viewing_logs
- **Target Normalization Level:** 3NF / BCNF

### 2. DATA MODELING STRATEGIES
- **Key Constraints:** UUIDv4 for ID fields, audit fields on all main tables.
- **Referential Integrity:** Set cascading deletions on log relations, restrict deletes on payment records.

### 3. EXPECTED DELIVERABLES
1. **Entity-Relationship Diagram (ERD):** Map tables and connections in clear text markup.
2. **Standard-Compliant SQL DDL Script:** Executable DDL schema for PostgreSQL.
3. **Indexing Script:** Custom CREATE INDEX commands for fast viewing log fetches.
```

## Best Practices
1. **Prefer UUIDs over Serial IDs:** Use UUIDs for public-facing IDs to prevent enumeration attacks and simplify distributed database merges.
2. **Auditing Fields:** Include `created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP` and an automated trigger for `updated_at` on every table.
3. **Prevent Junction Table Bloat:** Junction tables for N:M relationships must declare a composite primary key (`(table_a_id, table_b_id)`).
4. **Lowercase Naming:** Use `snake_case` with lowercase characters for tables, fields, and index names to prevent uppercase syntax mapping bugs.
5. **Add CHECK Constraints:** Enforce data validation at the database layer using SQL `CHECK` blocks (e.g., `price >= 0`).

## Common Mistakes to Avoid
- **Missing Foreign Key Indexes:** Forgetting indexes on foreign key columns, causing nested-loop sequential scans during large JOIN operations.
- **Using Naked text Datatype:** Using elastic types without sizing constraints for bounded attributes.
- **Hard Deleting Audited Data:** Deleting records permanently when regulatory frameworks require soft-deletion flags.
- **Storing Raw Passwords:** Storing raw authentication strings instead of requiring hashed, salted keys.
""",

    r"research\literature_review.md": """---
title: Academic Literature Review Synthesis
category: research
subcategory: academic_writing
tags:
  - literature-review
  - academic-writing
  - research-methodology
  - systematic-review
  - study-synthesis
difficulty: advanced
depth: deep
retrieval_keywords:
  - literature review writing
  - systematic review prisma
  - academic paper synthesis
  - research gap analysis
  - ieee citation style
  - peer reviewed search
use_case: >
  Retrieve when the user is writing academic study syntheses,
  systematic literature reviews, theses introductions, or gap analyses.
placeholder_count: 4
version: "1.0"
---

# Academic Literature Review Synthesis

## Purpose
This template drives the creation of high-impact, rigorous academic literature reviews and study syntheses. It guides the user in mapping theoretical paradigms, structuring content thematically, conducting deep gap analyses, and referencing citations using standardized styles.

## When to Retrieve This Template
- "Write a systematic literature review on deep learning in healthcare."
- "Synthesize the academic papers concerning remote work productivity."
- "Generate a research gap analysis section for a blockchain thesis."
- "How do I structure a literature review comparing cryptography algorithms?"

## Prompt Framework
```markdown
You are a Lead Academic Researcher, University Professor, and Rigorous Scientific Writer specializing in peer-reviewed data synthesis.

Your objective is to produce a publishable academic background review on a target subject.

### 1. STUDY PARAMETERS & SCOPE
- **Research Topic:** {{RESEARCH_TOPIC}}
- **Time Window:** Publications from {{PUBLICATION_YEAR_RANGE}}
- **Review Methodology:** [Choose: Systematic PRISMA review | Thematic synthesis | Historical chronological overview]
- **Source Constraints:** {{SOURCE_TYPES}}

### 2. THEMATIC SYNTHESIS STRUCTURE
- **Introduction:** Conceptual boundaries, historical background, and theoretical frameworks.
- **Thematic Core:** Grouping prior research into key themes rather than listing paper summaries one by one.
- **Critical Disagreement Matrix:** Mapping conflicting studies, variable arguments, and methodological anomalies in the literature.
- **Research Gap Analysis:** Explicitly identifying neglected niches, geographic limits, or technological boundaries.

### 3. OUTPUT SPECIFICATIONS
- **Citation Format:** [Choose: APA 7th Edition | IEEE Numeric | MLA | Chicago Author-Date]
- Deliver a complete literature review draft containing structured section headings, logical thesis transitions, and bracketed citation anchors.
```

## Required Context
- Research Topic: {{RESEARCH_TOPIC}}
- Publication Year Range: {{PUBLICATION_YEAR_RANGE}}
- Source Types: {{SOURCE_TYPES}}
- Scope Boundaries: {{SCOPE_BOUNDARIES}}

---

## Optional Configuration
- Word Count Target: [Optional: 500w | 1500w | 3000w]
- Contrastive Arguments: [Yes / No]
- Include Citation List: [Yes / No]

---

## Full Example Prompt
```markdown
You are a Lead Academic Researcher, University Professor, and Rigorous Scientific Writer specializing in peer-reviewed data synthesis.

Your objective is to produce a publishable academic background review on a target subject.

### 1. STUDY PARAMETERS & SCOPE
- **Research Topic:** Reinforcement Learning in Autonomous Drone Flight Path Optimization.
- **Time Window:** Publications from 2018 to 2026.
- **Review Methodology:** Systematic PRISMA review
- **Source Constraints:** Peer-reviewed IEEE and ACM journals only.

### 2. THEMATIC SYNTHESIS STRUCTURE
- **Thematic Core:** Categorize papers into model-free vs. model-based architectures.
- **Critical Disagreement Matrix:** Contrast real-world hardware latency vs. simulation convergence.
```

## Best Practices
1. **Synthesize Thematically:** Group studies by themes or arguments rather than writing a sequential summary of individual articles.
2. **Cite Actively:** Support every assertion or trend claim with explicit citation placeholders.
3. **Expose Research Gaps:** Dedicate a distinct section to exposing limits in current literature, paving the way for the user's research thesis.
4. **Remain Sceptical:** Critique methods, sample sizes, and geographic bounds of cited papers to maintain academic objectivity.
5. **Use Active Scientific Voice:** Employ robust academic terminology.

## Common Mistakes to Avoid
- **List-Like Summarizing:** Reviewing papers in chronological bullet points without extracting comparative themes or arguments.
- **Uncited Claims:** Making sweeping generalization claims without grounding assertions in published peer-reviewed studies.
- **Biased Selection:** Excluding research that disagrees with the user's target thesis, undermining scholarly integrity.
- **Outdated Sources:** Focusing primarily on historical studies while ignoring key modern advancements and breakthroughs.
""",

    r"research\competitive_analysis.md": """---
title: Business Competitive Strategy Analyst
category: research
subcategory: market_intelligence
tags:
  - competitive-analysis
  - market-strategy
  - swot
  - porters-five-forces
  - feature-matrix
difficulty: advanced
depth: deep
retrieval_keywords:
  - competitive analysis spec
  - competitive landscape report
  - swot matrix generator
  - porters five forces business
  - product feature comparison
  - pricing strategy matrix
use_case: >
  Retrieve when the user wants to compile a competitive intelligence report,
  map market landscapes, write a SWOT matrix, or evaluate product positioning.
placeholder_count: 3
version: "1.0"
---

# Business Competitive Strategy Analyst

## Purpose
This template generates professional-grade, investor-ready competitive strategy reports. It guides users in analyzing product landscapes, building feature comparison matrices, performing SWOT profiles, applying Porter's Five Forces, and identifying strategic market gaps.

## When to Retrieve This Template
- "Write a competitive analysis for an online grocery delivery startup."
- "Generate a feature matrix comparing top email marketing platforms."
- "Perform a Porter's Five Forces analysis on the electric vehicle industry."
- "Create a SWOT analysis comparing our tool to competitor X."

## Prompt Framework
```markdown
You are a Principal Competitive Strategy Consultant, Market Analyst, and Strategic Business Intelligence Advisor.

Your objective is to generate an exhaustive competitive landscape analysis for a target product.

### 1. LANDSCAPE BOUNDARIES
- **Subject Product/Company:** {{SUBJECT}}
- **Core Competitors:** {{COMPETITOR_LIST}} (comma-separated list)
- **Key Dimensions for Comparison:** {{ANALYSIS_DIMENSIONS}}

### 2. ANALYTICAL DECOMPOSITION
- **Comparative Feature Matrix:** A detailed table mapping features across the subject and competitors.
- **Strategic SWOT Breakdown:** Individual Strengths, Weaknesses, Opportunities, and Threats for the subject product.
- **Market Positioning Map:** Explaining where the subject sits on cost vs. quality axes.
- **Value Proposition Gap Analysis:** Isolating specific competitor vulnerabilities and unfulfilled customer needs.

### 3. OUTPUT REQUIREMENTS
- Deliver a comprehensive business report with clear markdown tables, SWOT quadrants, strategic recommendations, and high-impact executive summaries.
```

## Required Context
- Subject Product: {{SUBJECT}}
- Competitor List: {{COMPETITOR_LIST}}
- Analysis Dimensions: {{ANALYSIS_DIMENSIONS}}

---

## Optional Configuration
- Data Scope: [Choose: Publicly available only | Include estimated projections]
- Industry Category: [Optional: SaaS | B2B Enterprise | E-Commerce | Hardware]
- Pricing Analysis: [Yes / No]

---

## Full Example Prompt
```markdown
You are a Principal Competitive Strategy Consultant, Market Analyst, and Strategic Business Intelligence Advisor.

Your objective is to generate an exhaustive competitive landscape analysis for a target product.

### 1. LANDSCAPE BOUNDARIES
- **Subject Product/Company:** QuickPay Wallet
- **Core Competitors:** Stripe Terminal, Square, PayPal Zettle
- **Key Dimensions for Comparison:** Transaction fees, hardware costs, POS software integrations, payout speed.
- **Core Strategic Frameworks:** SWOT Analysis + Feature Comparison Matrix

### 2. ANALYTICAL DECOMPOSITION
- **Comparative Feature Matrix:** Compare hardware accessories and payout times.
- **Strategic SWOT Breakdown:** Map QuickPay's specific strengths in open-banking APIs.
```

## Best Practices
1. **Build Structured Tables:** Always present feature comparisons in clear, scannable markdown tables with visual markers.
2. **Actionable SWOT Points:** Avoid vague terms in SWOT quadrants. Write concrete points.
3. **Quantify Financial Data:** Whenever possible, include precise cost numbers, transaction rates, or pricing tiers.
4. **Isolate Gaps:** Emphasize the "Opportunity Gap"—exactly what competitors are doing poorly.
5. **Calibrate Porter's Forces:** When using Porter's Five Forces, assign a clear rank (Low | Medium | High) and back it up.

## Common Mistakes to Avoid
- **Flattery Bias:** Exaggerating the strengths of the subject company while downplaying competitors, producing an unrealistic strategic assessment.
- **Feature Bloat Lists:** Listing dozens of trivial features in comparison tables instead of focusing on high-impact value-driving differentiators.
- **Generic SWOT Charts:** Copying boilerplate SWOT items that apply to every startup.
- **Static Market Map:** Describing a static market without highlighting historical trajectories or emerging industry trends.
"""
}

for rel_path, content in deep_updates.items():
    abs_path = os.path.join(KB_DIR, rel_path)
    with open(abs_path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + "\n")
    print(f"Updated DEEP file: {rel_path}")

# 2. MEDIUM TEMPLATES (Compacted strictly to [20, 50] lines)
medium_templates = {
    r"software_development\code_review.md": """---
title: Professional Code Reviewer
category: software_development
subcategory: code_review
tags: [code-review, qa, bugs]
difficulty: intermediate
depth: medium
retrieval_keywords: [code review, scan code smells, find bug logic]
use_case: Retrieve to review code blocks and locate bugs.
placeholder_count: 3
version: "1.0"
---
# Professional Code Reviewer
## Purpose
Structures peer-review scanning for logical bugs, code smells, and performance bottlenecks.
## When to Retrieve This Template
- "Review this Python script for performance issues."
- "Are there any bugs or code smells in this React component?"
- "Do a security-focused code review on my Express auth middleware."
## Prompt Framework
You are an expert Senior Code Reviewer. Review the code inside `<user_code>` for language {{LANGUAGE}}, focusing on {{DEPTH}} to achieve {{CODE_PURPOSE}}.
## Required Context
- Language: {{LANGUAGE}}
- Focus: {{DEPTH}}
- Purpose: {{CODE_PURPOSE}}
## Optional Configuration
- Format: [Table | Detailed paragraphs]
## Example Prompt
Review this Node.js script focusing on performance, to optimize sql fetches.
## Best Practices
1. Provide actionable solutions and code alternatives.
2. Categorize findings by severity (CRITICAL, WARNING, INFO).
3. Reference exact line numbers when reporting issues.
""",

    r"software_development\security_audit.md": """---
title: Application Security & Threat Auditor
category: software_development
subcategory: security_audit
tags: [security-audit, owasp, cyber-security]
difficulty: advanced
depth: medium
retrieval_keywords: [security audit, owasp top 10, penetration threat]
use_case: Retrieve to audit application code or architectures against security concerns.
placeholder_count: 2
version: "1.0"
---
# Application Security & Threat Auditor
## Purpose
Drives security audits of application architectures or source codes mapped against OWASP vulnerabilities.
## When to Retrieve This Template
- "Do a security audit on this SQL query structure."
- "Perform threat modeling on our OAuth2 login architecture."
- "Scan this API gateway setup for OWASP vulnerabilities."
## Prompt Framework
You are an expert Cybersecurity Auditor. Scan the provided architecture or code for {{SECURITY_CONCERNS}} in this {{APPLICATION_TYPE}} system. Focus on OWASP Top 10 vulnerabilities.
## Required Context
- Application Type: {{APPLICATION_TYPE}}
- Security Concerns: {{SECURITY_CONCERNS}}
## Optional Configuration
- Compliance Target: [OWASP | PCI-DSS | GDPR | SOC2]
## Example Prompt
Audit a Node.js REST API managing user metadata against SQL Injection and access control.
## Best Practices
1. Scrub raw production credentials or keys before starting audits.
2. Prioritize vulnerabilities using standard risk levels (Critical, High, Medium, Low).
3. Supply secure, corrected copy-pasteable configuration or code solutions.
""",

    r"software_development\testing_strategy.md": """---
title: QA & Software Testing Strategy Planner
category: software_development
subcategory: testing_strategy
tags: [software-testing, qa, unit-tests]
difficulty: intermediate
depth: medium
retrieval_keywords: [testing strategy, qa testing pyramid, unit integration e2e]
use_case: Retrieve when the user is designing test plans or configuring CI/CD testing steps.
placeholder_count: 3
version: "1.0"
---
# QA & Software Testing Strategy Planner
## Purpose
Structures unified QA software testing plans spanning unit, integration, and E2E pyramids.
## When to Retrieve This Template
- "Write a testing strategy for our React and Django application."
- "Generate automated test cases using Cypress for a registration flow."
- "How do I setup a complete QA test plan for a payment backend?"
## Prompt Framework
You are a Lead QA Architect. Design a testing strategy for {{APP_TYPE}} built on {{TECH_STACK}} aiming for {{COVERAGE_TARGET}} coverage. Define Unit, Integration, and E2E milestones.
## Required Context
- App Type: {{APP_TYPE}}
- Tech Stack: {{TECH_STACK}}
- Coverage Target: {{COVERAGE_TARGET}}
## Optional Configuration
- CI Tool: [Optional: GitHub Actions | GitLab CI]
## Example Prompt
Design a test plan for an E-Commerce web interface using React and Stripe to hit 85% coverage.
## Best Practices
1. Prioritize tests that guard core revenue-driving user journeys.
2. Mock database and external network API dependencies in unit tests.
3. Clean data states between integration test suites to prevent contamination.
""",

    r"uiux_design\user_research.md": """---
title: UX User Research Planner
category: uiux_design
subcategory: user_research
tags: [ux-research, user-interviews, testing]
difficulty: intermediate
depth: medium
retrieval_keywords: [ux research plan, user interview guide, usability test]
use_case: Retrieve when the user is designing UX user research plans or drafting test guides.
placeholder_count: 4
version: "1.0"
---
# UX User Research Planner
## Purpose
Generates professional UX research plans, screeners, and usability testing scripts.
## When to Retrieve This Template
- "Write a UX research plan for a new food delivery app."
- "Generate user interview questions for retired individuals."
- "Create a usability testing script for our checkout flow."
## Prompt Framework
You are a UX Researcher. Design a study for a product at the {{PRODUCT_STAGE}} stage. Target the profile {{PARTICIPANT_PROFILE}} to address {{RESEARCH_GOALS}} using {{STUDY_METHOD}}.
## Required Context
- Product Stage: {{PRODUCT_STAGE}}
- Participant Profile: {{PARTICIPANT_PROFILE}}
- Research Goals: {{RESEARCH_GOALS}}
- Study Method: {{STUDY_METHOD}}
## Optional Configuration
- Interview Length: [30 mins | 60 mins]
## Example Prompt
Plan a usability lab test for a mid-fidelity cart checkout targeting mobile shoppers.
## Best Practices
1. Avoid asking leading questions; focus on open-ended behavioral tasks.
2. Focus on watching actual user interactions rather than stated opinions.
3. Keep usability testing scenarios realistic and goal-oriented.
""",

    r"uiux_design\wireframe_specification.md": """---
title: Wireframe Specification & Layout Builder
category: uiux_design
subcategory: wireframe_spec
tags: [wireframe, ui-design, layout]
difficulty: intermediate
depth: medium
retrieval_keywords: [wireframe spec, ui layout structure, content hierarchy]
use_case: Retrieve when the user is drafting wireframe layouts or annotating screens for developers.
placeholder_count: 3
version: "1.0"
---
# Wireframe Specification & Layout Builder
## Purpose
Generates wireframe layout specs, interface hierarchies, and annotated interactive screen flows.
## When to Retrieve This Template
- "Write a wireframe layout specification for a SaaS landing page."
- "Generate a UI content hierarchy plan for settings screens."
- "Create annotated wireframes for a dashboard layout."
## Prompt Framework
You are a Lead Product Designer. Design a wireframe specification for {{SCREEN_NAME}} supporting the flow {{USER_FLOW}} optimized for {{TARGET_PLATFORM}}.
## Required Context
- Screen Name: {{SCREEN_NAME}}
- User Flow: {{USER_FLOW}}
- Target Platform: {{TARGET_PLATFORM}}
## Optional Configuration
- Granularity: [Low-Fidelity skeletal | Mid-Fidelity detailed]
## Example Prompt
Design a wireframe layout for a customer profile editor on responsive web screens.
## Best Practices
1. Stack layouts vertically for mobile before expanding to wide desktop grids.
2. Place primary calls-to-action above the fold for maximum visibility.
3. Document interface edge cases like long text strings or load states.
""",

    r"content_creation\linkedin_post.md": """---
title: LinkedIn Content Architect & Post Writer
category: content_creation
subcategory: social_copy
tags: [linkedin, copywriting, social-media]
difficulty: intermediate
depth: medium
retrieval_keywords: [linkedin post, social copy, branding hook]
use_case: Retrieve to write high-engagement LinkedIn posts or thought leadership updates.
placeholder_count: 3
version: "1.0"
---
# LinkedIn Content Architect & Post Writer
## Purpose
Generates high-engagement LinkedIn posts with clear hooks, story structures, and CTAs.
## When to Retrieve This Template
- "Write a LinkedIn post about leaving my software developer job."
- "Generate a thought-leadership post about AI automation."
- "Create a LinkedIn update promoting our product launch."
## Prompt Framework
You are a LinkedIn Content Strategist. Write a post on {{POST_TOPIC}} representing the voice of {{AUTHOR_BACKGROUND}} to achieve {{CALL_TO_ACTION}}.
## Required Context
- Author Background: {{AUTHOR_BACKGROUND}}
- Post Topic: {{POST_TOPIC}}
- Call to Action: {{CALL_TO_ACTION}}
## Optional Configuration
- Writing Tone: [Conversational | Analytical | Storytelling]
## Example Prompt
Write a post on hybrid cloud migration in the voice of a senior cloud architect.
## Best Practices
1. Place the core hook within the first 140 characters before the see-more cut.
2. Write in short, single-sentence paragraphs to increase mobile readability.
3. Limit hashtags to 3-5 and place them at the very bottom.
""",

    r"content_creation\technical_blog.md": """---
title: SEO Technical Blog & Tutorial Writer
category: content_creation
subcategory: blog_copy
tags: [technical-writing, blog, seo]
difficulty: intermediate
depth: medium
retrieval_keywords: [technical blog, code tutorial, seo friendly blog]
use_case: Retrieve to write technical blogs, developer tutorials, or how-to guides.
placeholder_count: 4
version: "1.0"
---
# SEO Technical Blog & Tutorial Writer
## Purpose
Drives technical blog creation using structured, SEO-optimized problem-solution flows.
## When to Retrieve This Template
- "Write a technical blog post about setting up Docker for Node.js."
- "Create a developer tutorial explaining CSS grid layouts."
- "Generate a blog article about React Server Components."
## Prompt Framework
You are a Technical Writer. Write a technical tutorial on {{BLOG_TOPIC}} for {{AUDIENCE_LEVEL}} using keywords {{SEO_KEYWORDS}} ending in the CTA {{BLOG_CTA}}.
## Required Context
- Blog Topic: {{BLOG_TOPIC}}
- Audience Level: {{AUDIENCE_LEVEL}}
- SEO Keywords: {{SEO_KEYWORDS}}
- Blog CTA: {{BLOG_CTA}}
## Optional Configuration
- Code Snippets: [Include code | Conceptual only]
## Example Prompt
Write a tutorial on rate limiting in Express APIs for mid-level node developers.
## Best Practices
1. Dedicate space to explain the core architectural reasons behind code logic.
2. Embed descriptive inline comments in all generated code snippets.
3. Maintain clear H2/H3 heading hierarchies to boost search crawler indexing.
""",

    r"content_creation\documentation.md": """---
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
""",

    r"learning\tutor_session.md": """---
title: Socratic Expert Tutor Session
category: learning
subcategory: tutoring
tags: [tutoring, pedagogy, socratic]
difficulty: intermediate
depth: medium
retrieval_keywords: [tutor session, socratic learning, analogy teaching]
use_case: Retrieve when the user wants interactive, Socratic-led learning sessions.
placeholder_count: 3
version: "1.0"
---
# Socratic Expert Tutor Session
## Purpose
Configures the AI as an expert Socratic tutor to guide users through complex concepts.
## When to Retrieve This Template
- "Teach me how closures work in JavaScript using the Socratic method."
- "Act as an expert physics tutor and explain quantum superposition."
- "Help me understand relational database transactions step-by-step."
## Prompt Framework
You are a patient Socratic Tutor. Lead a dynamic educational session on {{SUBJECT}} for a student with {{STUDENT_BACKGROUND}} aiming to learn {{LEARNING_OBJECTIVE}}.
## Required Context
- Subject: {{SUBJECT}}
- Student Background: {{STUDENT_BACKGROUND}}
- Learning Objective: {{LEARNING_OBJECTIVE}}
## Optional Configuration
- Level: [High School | Undergraduate | Professional]
## Example Prompt
Guide an intermediate Python developer to master low-level pointer arithmetic in C++.
## Best Practices
1. Break down complex topics into progressive, Socratic questioning nodes.
2. Anchor abstract concepts in everyday, high-impact analogies.
3. Never give the direct solution; prompt the student to reasoning it out.
""",

    r"learning\study_plan.md": """---
title: Spaced Repetition Study Planner
category: learning
subcategory: study_planning
tags: [study-plan, spaced-repetition, study-tracker]
difficulty: intermediate
depth: medium
retrieval_keywords: [study plan, spaced repetition, curriculum prep]
use_case: Retrieve when the user wants a weekly study plan or exam prep guide.
placeholder_count: 5
version: "1.0"
---
# Spaced Repetition Study Planner
## Purpose
Generates study roadmaps integrating spaced repetition and active recall loops.
## When to Retrieve This Template
- "Create a 6-week study plan to learn web development basics."
- "Generate a prep guide for my upcoming AWS solutions architect exam."
- "Design a monthly study curriculum for learning calculus."
## Prompt Framework
You are a Curriculum Designer. Create a study plan for {{SUBJECT}} to achieve {{TARGET_GOAL}} given {{CURRENT_LEVEL}} background over {{WEEKS_AVAILABLE}} weeks at {{DAILY_HOURS}} hours daily.
## Required Context
- Subject: {{SUBJECT}}
- Current Level: {{CURRENT_LEVEL}}
- Weeks Available: {{WEEKS_AVAILABLE}}
- Daily Hours: {{DAILY_HOURS}}
- Target Goal: {{TARGET_GOAL}}
## Optional Configuration
- Pace Style: [Intensive sprint | Sustainable pacing]
## Example Prompt
Design a 4-week study plan for Docker containerization starting from terminal basics.
## Best Practices
1. Focus on active recall tasks rather than passive reading sessions.
2. Programmatically schedule review nodes for past week's topics.
3. Conclude each weekly milestone with a practical assessment check.
""",

    r"business\market_analysis.md": """---
title: Market Analysis & Opportunity Researcher
category: business
subcategory: market_analysis
tags: [market-analysis, tam-sam-som, business-strategy]
difficulty: intermediate
depth: medium
retrieval_keywords: [market analysis, tam sam som, customer persona]
use_case: Retrieve when the user wants to size market segments or research target demographics.
placeholder_count: 3
version: "1.0"
---
# Market Analysis & Opportunity Researcher
## Purpose
Generates market sizing and customer demographic research assessments.
## When to Retrieve This Template
- "Write a market analysis report for a solar panel cleaning service."
- "Generate customer profiles and sizing models for a B2B SaaS startup."
- "Create a market opportunity assessment for organic baby food."
## Prompt Framework
You are a Market Strategist. Analyze the opportunity for {{PRODUCT_DESCRIPTION}} in {{INDUSTRY_SECTOR}} within the geographic boundaries of {{GEOGRAPHIC_FOCUS}}.
## Required Context
- Product Description: {{PRODUCT_DESCRIPTION}}
- Industry Sector: {{INDUSTRY_SECTOR}}
- Geographic Focus: {{GEOGRAPHIC_FOCUS}}
## Optional Configuration
- Calculation: [Back-of-the-envelope | Detailed bottom-up]
## Example Prompt
Saturate a sizing model for an electric scooter rental startup in college towns.
## Best Practices
1. Clearly differentiate Total (TAM), Serviceable (SAM), and Obtainable (SOM) grids.
2. Back up all market sizing numbers with transparent formulas and assumptions.
3. Map target consumer behavior by identifying core workflow pain points.
""",

    r"productivity\task_breakdown.md": """---
title: Work Breakdown Structure (WBS) & Task Planner
category: productivity
subcategory: task_management
tags: [task-breakdown, wbs, gtd]
difficulty: intermediate
depth: medium
retrieval_keywords: [work breakdown structure, gtd task list, project roadmap]
use_case: Retrieve to decompose projects into prioritized, hourly-estimated tasks.
placeholder_count: 3
version: "1.0"
---
# Work Breakdown Structure (WBS) & Task Planner
## Purpose
Generates prioritized Work Breakdown Structures using GTD and Eisenhower frameworks.
## When to Retrieve This Template
- "Break down the launch of a new marketing website into tasks."
- "Generate a WBS for a database migration project."
- "Create a GTD-prioritized checklist to write a research paper."
## Prompt Framework
You are a Project Manager. Build a WBS for {{PROJECT_GOAL}} due by {{DEADLINE}} to be executed by {{TEAM_SIZE}}. Map priorities P1/P2/P3 with hour estimates.
## Required Context
- Project Goal: {{PROJECT_GOAL}}
- Deadline: {{DEADLINE}}
- Team Size: {{TEAM_SIZE}}
## Optional Configuration
- Granularity: [High-level milestones | Detailed action items]
## Example Prompt
Decompose a 2-week mobile app CD pipeline migration setup for a solo dev.
## Best Practices
1. Ensure the sum of child tasks equals 100% of the parent epic scope.
2. Initiate all low-level action items with strong, measurable action verbs.
3. Limit individual action items to a maximum execution cap of 8 hours.
""",

    r"image_generation\brand_illustration.md": """---
title: Corporate Brand Illustration Prompt Architect
category: image_generation
subcategory: brand_illustration
tags: [brand-design, illustration, midjourney]
difficulty: intermediate
depth: medium
retrieval_keywords: [brand illustration prompt, vector graphic, website hero]
use_case: Retrieve to generate visual prompt structures for brand vector art.
placeholder_count: 4
version: "1.0"
---
# Corporate Brand Illustration Prompt Architect
## Purpose
Generates brand illustration prompts for Midjourney, DALL-E, and Stable Diffusion.
## When to Retrieve This Template
- "Write a Midjourney prompt for flat vector illustrations."
- "Create an isometric illustration prompt representing cloud data."
- "Generate a cohesive set of 3D clay-style icons for fintech."
## Prompt Framework
You are a Brand Illustrator. Build a prompt on {{ILLUSTRATION_TOPIC}} styled as {{VISUAL_STYLE}} for the use case {{USE_CASE}} using palette {{COLOR_PALETTE}}.
## Required Context
- Illustration Topic: {{ILLUSTRATION_TOPIC}}
- Visual Style: {{VISUAL_STYLE}}
- Use Case: {{USE_CASE}}
- Color Palette: {{COLOR_PALETTE}}
## Optional Configuration
- Aspect Ratio: [Optional: --ar 16:9 | --ar 1:1]
## Example Prompt
Create a flat vector website hero banner of a remote developer drinking coffee.
## Best Practices
1. Force solid background specs to facilitate easy asset tracing and isolation.
2. Specify restricted palettes (max 3-4 colors) to align visual harmony.
3. Keep shapes stylized and modern to avoid uncanny-valley human renders.
""",

    r"image_generation\ui_mockup_visual.md": """---
title: UI/UX Mockup Visual Prompt Architect
category: image_generation
subcategory: ui_mockup
tags: [ui-mockup, midjourney, web-design]
difficulty: intermediate
depth: medium
retrieval_keywords: [ui mockup prompt, web interface mockup, app screenshot]
use_case: Retrieve to design visual UI mockups, dashboard layouts, or app assets.
placeholder_count: 4
version: "1.0"
---
# UI/UX Mockup Visual Prompt Architect
## Purpose
Generates high-fidelity UI visual mockup prompts for creative design inspiration.
## When to Retrieve This Template
- "Generate a Midjourney prompt for a dashboard UI mockup."
- "Create a visual mobile app mockup prompt for a travel application."
- "Write an image prompt showing a minimalist portfolio website layout."
## Prompt Framework
You are a UI Art Director. Create a mockup prompt for {{PLATFORM_DOMAIN}}'s {{SCREEN_TYPE}} screen in a {{UI_AESTHETIC}} style featuring {{PRIMARY_COLORS}} colors.
## Required Context
- Platform Domain: {{PLATFORM_DOMAIN}}
- Screen Type: {{SCREEN_TYPE}}
- UI Aesthetic: {{UI_AESTHETIC}}
- Primary Colors: {{PRIMARY_COLORS}}
## Optional Configuration
- Device: [Frameless UI | Mobile Frame | Laptop Frame]
## Example Prompt
Draft a dashboard screenshot prompt for a dark glassmorphic crypto tracker.
## Best Practices
1. Request flat orthographic perspectives to keep assets readable and clean.
2. Restrict the palette to 2 brand accents and 2 flat neutrals.
3. Strictly exclude human hands or hands holding devices in negative prompt tags.
""",

    r"data_analysis\dashboard_design.md": """---
title: Business Intelligence Dashboard Designer
category: data_analysis
subcategory: dashboard_design
tags: [data-visualization, dashboard, tableau]
difficulty: intermediate
depth: medium
retrieval_keywords: [dashboard design, kpi metrics, power bi spec]
use_case: Retrieve when planning dashboard charts, layouts, or KPI reports.
placeholder_count: 4
version: "1.0"
---
# Business Intelligence Dashboard Designer
## Purpose
Generates structured KPI dashboard visual plans for Tableau, Power BI, or Grafana.
## When to Retrieve This Template
- "Design a Tableau dashboard layout for sales performance tracking."
- "Generate a Power BI dashboard spec for a warehouse operations team."
- "Create a customer retention dashboard design with metrics."
## Prompt Framework
You are a BI Expert. Design a dashboard spec for {{DASHBOARD_TITLE}} targeting {{TARGET_AUDIENCE}} running at {{REFRESH_RATE}} containing {{PRIMARY_METRICS}}.
## Required Context
- Dashboard Title: {{DASHBOARD_TITLE}}
- Target Audience: {{TARGET_AUDIENCE}}
- Refresh Rate: {{REFRESH_RATE}}
- Primary Metrics: {{PRIMARY_METRICS}}
## Optional Configuration
- Interactivity: [Static reports | Active filters & drill-downs]
## Example Prompt
Design an executive revenue dashboard spec for C-suite daily monitoring.
## Best Practices
1. Reserve the top-left visual quadrant for the absolute core KPI cards.
2. Limit dashboards to a maximum of 3 distinct, clean chart configurations.
3. Avoid pie charts for categorical sets exceeding 3 unique dimensions.
""",

    r"data_analysis\insight_report.md": """---
title: Executive Insight Report Writer
category: data_analysis
subcategory: insight_reporting
tags: [data-analysis, insight-report, pyramid-principle]
difficulty: intermediate
depth: medium
retrieval_keywords: [insight report, data trend analysis, executive brief]
use_case: Retrieve when synthesizing data trends, CAC, or monthly metrics.
placeholder_count: 3
version: "1.0"
---
# Executive Insight Report Writer
## Purpose
Generates executive-level data insights applying the McKinsey Pyramid Principle.
## When to Retrieve This Template
- "Write an executive brief on our Q2 customer acquisition costs."
- "Generate a data insight report from our monthly support ticket trends."
- "Create an analytical summary of our platform traffic growth."
## Prompt Framework
You are a Business Intelligence Analyst. Write a report on {{ANALYSIS_DOMAIN}} for {{TIME_PERIOD}} using trends {{CORE_METRIC_TRENDS}} in a top-down pyramid structure.
## Required Context
- Analysis Domain: {{ANALYSIS_DOMAIN}}
- Time Period: {{TIME_PERIOD}}
- Core Metric Trends: {{CORE_METRIC_TRENDS}}
## Optional Configuration
- Reader Level: [Executive C-Suite | Director | Technical Lead]
## Example Prompt
Write a Q3 analytics brief summarizing e-commerce funnel drop-offs.
## Best Practices
1. Deliver the final, key conclusion in the first introductory paragraph.
2. Replace descriptive generalizations with precise, quantified metric values.
3. Ground every strategic recommendation directly in a reported data anomaly.
""",

    r"research\topic_deep_dive.md": """---
title: Subject Matter Expert Topic Deep Dive
category: research
subcategory: topic_analysis
tags: [research, deep-dive, subject-matter-expert]
difficulty: intermediate
depth: medium
retrieval_keywords: [topic deep dive, expert explain, concept map]
use_case: Retrieve when requiring detailed conceptual breakdowns or learning roadmaps.
placeholder_count: 3
version: "1.0"
---
# Subject Matter Expert Topic Deep Dive
## Purpose
Configures the AI as a subject-matter analyst to deliver topic guides and concept maps.
## When to Retrieve This Template
- "Explain zero-knowledge proofs in detail."
- "Perform a deep dive on quantum cryptography methods."
- "Generate a technical concept map for edge database clusters."
## Prompt Framework
You are a Subject Matter Expert. Write a topic deep dive on {{TOPIC}} calibrated for {{PRIOR_KNOWLEDGE}} to be output in the format {{FORMAT}}.
## Required Context
- Topic: {{TOPIC}}
- Prior Knowledge: {{PRIOR_KNOWLEDGE}}
- Format: {{FORMAT}}
## Optional Configuration
- Depth: [Conceptual overview | Technical deep dive | Scientific review]
## Example Prompt
Explain zero-knowledge rollups to a developer in a structured analytical essay.
## Best Practices
1. Skip baseline summaries if the user has documented prior experience.
2. Anchor explanations in simple, high-utility analogical comparisons.
3. Formulate math models using standard, readable LaTeX blocks ($$...$$).
"""
}

for rel_path, content in medium_templates.items():
    abs_path = os.path.join(KB_DIR, rel_path)
    with open(abs_path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + "\n")
    print(f"Updated MEDIUM file: {rel_path}")

# 3. LIGHTWEIGHT TEMPLATES (Compacted strictly to [10, 25] lines)
lightweight_templates = {
    r"uiux_design\accessibility_review.md": """---
title: Accessibility Review Checklist
category: uiux_design
subcategory: accessibility
tags: [accessibility, wcag, a11y]
difficulty: beginner
depth: lightweight
retrieval_keywords: [accessibility audit, wcag checklist, contrast checker]
use_case: Retrieve for WCAG compliance checks.
placeholder_count: 2
version: "1.0"
---
# Accessibility Review Checklist
## Purpose
Provides a rapid WCAG 2.2 accessibility checklist to verify contrast, tap targets, and screen reader labels.
## Required Context
- Component Name: {{COMPONENT_NAME}}
- Target WCAG Level: {{TARGET_LEVEL}}
## Template
Act as an expert Accessibility Auditor. Review {{COMPONENT_NAME}} against {{TARGET_LEVEL}} standards. Verify: 1. Perceivable (contrast 4.5:1), 2. Operable (keyboard paths, 48x48px hit areas), 3. Robust (ARIA mapping).
## Best Practices
1. Ensure all elements can be focused using only TAB and ENTER keys.
2. Require empty alt tags for decorative elements.
""",

    r"content_creation\social_media_campaign.md": """---
title: Multi-Platform Social Campaign
category: content_creation
subcategory: social_copy
tags: [social-media, campaign, marketing]
difficulty: beginner
depth: lightweight
retrieval_keywords: [social media campaign, post variants, campaign copy]
use_case: Retrieve to generate multiple promotional social posts for a launch.
placeholder_count: 3
version: "1.0"
---
# Multi-Platform Social Campaign
## Purpose
Drafts quick 5-post social media campaign variants across Twitter, LinkedIn, and Instagram.
## Required Context
- Brand Name: {{BRAND_NAME}}
- Campaign Goal: {{CAMPAIGN_GOAL}}
- Target Platform: {{PLATFORM}}
## Template
Act as a Social Media Manager. Write a 5-post promotional campaign for {{BRAND_NAME}} to achieve {{CAMPAIGN_GOAL}} on {{PLATFORM}}. For each post, supply the caption text, an engagement trigger, and 3 niche hashtags.
## Best Practices
1. Calibrate caption length to platform-specific limits (e.g. 280 chars for Twitter/X).
2. End every post with a singular, clear conversion link hook.
""",

    r"learning\quiz_generator.md": """---
title: Interactive Quiz Generator
category: learning
subcategory: assessment
tags: [quiz-generator, active-recall, exam]
difficulty: beginner
depth: lightweight
retrieval_keywords: [quiz questions, mcq test, active recall check]
use_case: Retrieve to generate quick quizzes or flashcard text.
placeholder_count: 3
version: "1.0"
---
# Interactive Quiz Generator
## Purpose
Generates structured quizzes (MCQs and short answers) with detailed answer keys.
## Required Context
- Quiz Topic: {{TOPIC}}
- Difficulty Level: {{DIFFICULTY}}
- Question Count: {{QUESTION_COUNT}}
## Template
Act as an Academic Assessor. Generate a {{QUESTION_COUNT}}-question quiz on the topic of {{TOPIC}} at {{DIULTY}} difficulty. Provide MCQs, true/false, and short answers. Append the full answer key at the bottom.
## Best Practices
1. Design plausible, common-misconception distractor options for MCQs.
2. Include brief logic explanations for every correct key in the answers.
""",

    r"learning\concept_explainer.md": """---
title: Plain-Language Concept Explainer
category: learning
subcategory: tutoring
tags: [concept-explainer, analogies, teaching]
difficulty: beginner
depth: lightweight
retrieval_keywords: [explain concept simple, analogy teach, worked example]
use_case: Retrieve to explain complex topics or terms in simple language.
placeholder_count: 2
version: "1.0"
---
# Plain-Language Concept Explainer
## Purpose
Provides clear, jargon-free explanations of complex terms using concrete metaphors and single worked examples.
## Required Context
- Target Concept: {{CONCEPT}}
- Target Audience Level: {{AUDIENCE_LEVEL}}
## Template
Act as an expert Educator. Explain {{CONCEPT}} to a {{AUDIENCE_LEVEL}} audience. Structure: 1. Plain-Language Summary, 2. Metaphorical Analogy, 3. Step-by-Step Worked Example.
## Best Practices
1. Strictly avoid advanced technical jargon unless followed immediately by a definition.
2. Dedicate the explanation to a single, high-fidelity analogy.
""",

    r"business\executive_summary.md": """---
title: Executive Summary Writer
category: business
subcategory: communication
tags: [executive-summary, business-writing, scqa]
difficulty: beginner
depth: lightweight
retrieval_keywords: [executive summary, business summary, scqa summary]
use_case: Retrieve to summarize business proposals or project pitches.
placeholder_count: 3
version: "1.0"
---
# Executive Summary Writer
## Purpose
Leverages the SCQA framework to summarize long business documents into C-suite briefs.
## Required Context
- Document Type: {{DOCUMENT_TYPE}}
- Core Topic: {{CORE_TOPIC}}
- Target Audience: {{AUDIENCE}}
## Template
Act as an Executive Writer. Draft a 250-word executive summary for {{DOCUMENT_TYPE}} concerning {{CORE_TOPIC}} for {{AUDIENCE}}. Restructure using SCQA (Situation, Complication, Question, Answer) followed by 3 bulleted takeaways.
## Best Practices
1. Anchor status quo contexts clearly before revealing core solution actions.
2. Force the entire briefing text to sit strictly under a 250-word cap.
""",

    r"business\email_communication.md": """---
title: Corporate Email Architect
category: business
subcategory: communication
tags: [email, corporate-writing, messaging]
difficulty: beginner
depth: lightweight
retrieval_keywords: [corporate email, professional email, call to action email]
use_case: Retrieve to draft professional business emails, responses, or outreach.
placeholder_count: 3
version: "1.0"
---
# Corporate Email Architect
## Purpose
Structures professional business emails featuring a subject line and a clear, singular CTA.
## Required Context
- Email Purpose: {{EMAIL_PURPOSE}}
- Recipient Role: {{RECIPIENT_ROLE}}
- Sender Context: {{SENDER_CONTEXT}}
## Template
Act as a Corporate Writer. Draft a business email from {{SENDER_CONTEXT}} to {{RECIPIENT_ROLE}} for the purpose of {{EMAIL_PURPOSE}}. Supply 3 subject lines and a crisp email body (under 150 words) with one singular, explicit next-step ask.
## Best Practices
1. Keep the message focused strictly on a single call-to-action ask.
2. Outline the core value proposition in the first two introductory sentences.
""",

    r"productivity\meeting_agenda.md": """---
title: Timed Meeting Agenda Builder
category: productivity
subcategory: meeting_management
tags: [meeting-agenda, time-boxing, planning]
difficulty: beginner
depth: lightweight
retrieval_keywords: [timed meeting agenda, meeting planner, action tracker]
use_case: Retrieve to structure corporate syncs or time-boxed agenda slots.
placeholder_count: 3
version: "1.0"
---
# Timed Meeting Agenda Builder
## Purpose
Generates action-oriented timed agendas with designated speakers and action grids.
## Required Context
- Meeting Purpose: {{MEETING_PURPOSE}}
- Attendees List: {{ATTENDEES}}
- Duration (mins): {{DURATION}}
## Template
Act as a Project Facilitator. Build a structured agenda for a {{DURATION}}-minute sync focused on {{MEETING_PURPOSE}} with {{ATTENDEES}}. Supply: 1. Success objective, 2. Time-boxed breakdown table, 3. Action tracker grid.
## Best Practices
1. Time-box each topic blocks tightly to prevent conversation bleed.
2. Allocate the final 5 minutes of agenda time exclusively to assign task owners.
""",

    r"productivity\weekly_review.md": """---
title: Weekly Performance Review Architect
category: productivity
subcategory: task_management
tags: [weekly-review, performance, agile]
difficulty: beginner
depth: lightweight
retrieval_keywords: [weekly review, performance wins, retrospective]
use_case: Retrieve to conduct weekly retrospective reviews or set upcoming priorities.
placeholder_count: 2
version: "1.0"
---
# Weekly Performance Review Architect
## Purpose
Structures weekly retrospectives to score past goals, map wins, and plan priorities.
## Required Context
- Role Focus: {{ROLE}}
- Week's Goals: {{WEEK_GOALS}}
## Template
Act as a Productivity Coach. Structure a weekly review retrospective for a {{ROLE}} who set the target goals of {{WEEK_GOALS}}. Map: 1. Goal scores, 2. Wins & Blockers analysis, 3. Process learnings, 4. Next week's top 3 priorities.
## Best Practices
1. Retrospectively identify team process friction points with radical honesty.
2. Limit the upcoming week's commitments to a maximum of 3 core P1 milestones.
"""
}

for rel_path, content in lightweight_templates.items():
    abs_path = os.path.join(KB_DIR, rel_path)
    with open(abs_path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + "\n")
    print(f"Updated LIGHTWEIGHT file: {rel_path}")

print("Generation of compact RAG knowledge base files completed successfully!")
