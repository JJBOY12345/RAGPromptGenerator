import os
import re
from dotenv import load_dotenv
from google import genai
from src.retriever import retrieve
from src.providers import route_and_generate

_KB_FILE_PATH_CACHE = {}

def find_and_read_kb_file(filename: str) -> str:
    if filename in _KB_FILE_PATH_CACHE:
        file_path = _KB_FILE_PATH_CACHE[filename]
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read()
        except Exception:
            pass

    kb_dir = "knowledge_base"
    for root, _, files in os.walk(kb_dir):
        for f in files:
            _KB_FILE_PATH_CACHE[f] = os.path.join(root, f)
        if filename in files:
            file_path = os.path.join(root, filename)
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    return f.read()
            except Exception:
                pass
    return ""

def extract_framework_section(text: str) -> str:
    # Look for "Prompt Framework" heading (can be ## or ### or #)
    match = re.search(r"(?:^|\n)(?:##)\s*Prompt\s+Framework\s*\n(.*?)(?=\n##\s+|\n#\s+|$)", text, re.DOTALL | re.IGNORECASE)
    if match:
        section_content = match.group(1).strip()
        # Find the first fenced code block in this section
        code_match = re.search(r"```[a-zA-Z0-9_\-\+]*\n(.*?)```", section_content, re.DOTALL)
        if code_match:
            return code_match.group(1).strip()
        return section_content
    return ""

def scrub_leakage_terms(text: str) -> str:
    # Replace camera systems
    text = re.sub(r"Hasselblad H6D-100c|Sony A7R V|Hasselblad", "{{CAMERA_MODEL}}", text)
    # Replace lenses
    text = re.sub(r"90mm f/2.8 Macro lens|90mm f/2.8|85mm f/1.4 lens|85mm lens|90mm Macro lens", "{{LENS_MODEL}}", text)
    # Replace specific brand/product names in parentheticals to prevent leakage
    text = re.sub(r"Nike Air Max", "{{PRODUCT_NAME}}", text, flags=re.IGNORECASE)
    text = re.sub(r"Aura Essence Oil", "{{PRODUCT_NAME}}", text, flags=re.IGNORECASE)
    text = re.sub(r"ShopFlow Checkout", "{{PRODUCT_NAME}}", text, flags=re.IGNORECASE)
    return text

def sanitize_chunk_text(source_doc: str, chunk_text: str) -> str:
    # 1. Load the full file to ensure we get the complete, non-fragmented Prompt Framework
    full_content = find_and_read_kb_file(source_doc)
    if full_content:
        framework = extract_framework_section(full_content)
        if framework:
            return scrub_leakage_terms(framework)
            
    # 2. Fallback to extracting from chunk_text if file load failed
    framework = extract_framework_section(chunk_text)
    if framework:
        return scrub_leakage_terms(framework)
        
    # 3. Fallback: if we still can't find it, just return the chunk text itself after scrubbing
    return scrub_leakage_terms(chunk_text)

# Load environment variables
load_dotenv()

# Configure google-genai Client
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found in environment variables.\n"
        "Please create a '.env' file in the project root containing:\n"
        "GEMINI_API_KEY=your_actual_api_key"
    )

client = genai.Client(api_key=GEMINI_API_KEY)

def classify_category(user_goal: str) -> str:
    """
    Classifies the user's prompt engineering goal into a high-level category.
    Uses fast local keyword matching first to preserve API quota, falling back
    to gemini-2.5-flash if no keywords match.
    """
    categories = [
        "Software Development",
        "Learning",
        "Content Creation",
        "Research",
        "Image Generation",
        "Business Strategy"
    ]
    
    # 1. Primary: Fast, rate-limit-free keyword/phrase classification
    user_goal_lower = user_goal.lower()
    
    # Tier 1: Action/Intent Phrase Match (Strongest signals, ordered specific to broad)
    intent_phrases = {
        "Image Generation": [
            "brand illustration", "product photo", "photorealistic brand",
            "mockup visual", "product photography", "portrait of", "headshot"
        ],
        "Learning": [
            "study plan", "curriculum", "teach me", "tutor session", 
            "lesson plan", "how it works", "guide explaining", 
            "explain the concept", "interactive quiz", "quiz to test",
            "curriculum for", "interactive quiz on"
        ],
        "Content Creation": [
            "linkedin post", "blog post", "blog outline", "technical blog", 
            "social media", "marketing copy", "promotional campaign", 
            "api documentation", "write documentation", "executive memo",
            "linkedin content", "linkedin", "marketing messaging", "blog post about",
            "technical blog post", "write linkedin"
        ],
        "Software Development": [
            "database schema", "postgresql schema", "mysql schema", "rest api", 
            "express api", "unit test", "code review", "checklist for reviewing", 
            "wireframe specification", "user research", "security audit",
            "write unit tests", "audit on", "dashboard layout", "dashboard",
            "data analysis", "exploratory data analysis", "data insight", "insight report",
            "accessibility review", "design system"
        ],
        "Business Strategy": [
            "marketing strategy", "swot analysis", "business plan", "launch plan",
            "product requirements", "prd", "email response", "email to", "customer service"
        ],
        "Research": [
            "literature review", "synthesize research", "competitive analysis",
            "beamer", "latex", "scientific paper", "subject matter expert", "deep dive"
        ]
    }
    
    # Check for direct phrase matches first
    for cat, phrases in intent_phrases.items():
        if any(phrase in user_goal_lower for phrase in phrases):
            return cat
            
    # Tier 2: Refined Exact Word Token Matching (avoids substring collisions like "contract" containing "art")
    import re
    words = set(re.findall(r'\b\w+\b', user_goal_lower))
    
    word_keywords = {
        "Software Development": {
            "build", "code", "app", "application", "software", "api", 
            "develop", "framework", "schema", "fullstack", "frontend", 
            "backend", "solidity", "github", "git"
        },
        "Learning": {
            "teach", "learn", "study", "explain", "understand", "lesson", 
            "education", "tutorial", "course", "tutor", "socratic", "training", "curriculum"
        },
        "Content Creation": {
            "write", "linkedin", "post", "blog", "tweet", "content", 
            "copywrite", "advertisement", "copy", "caption", "campaign", "memo"
        },
        "Research": {
            "research", "analyze", "methodology", "investigate", "compare", 
            "academic", "papers", "science", "literature"
        },
        "Image Generation": {
            "image", "picture", "photo", "drawing", "portrait", "paint", 
            "art", "render", "cinematic", "photorealistic", "illustration"
        },
        "Business Strategy": {
            "business", "marketing", "strategy", "competitor", "product", 
            "sales", "revenue", "swot", "plan", "startup"
        }
    }
    
    # Check for exact word set intersections
    for cat, keywords in word_keywords.items():
        if words.intersection(keywords):
            return cat
        
    # 2. Secondary: LLM Fallback if no keywords matched
    classification_prompt = f"""Classify the user's prompt engineering goal into EXACTLY one of these categories:
- Software Development
- Learning
- Content Creation
- Research
- Image Generation
- Business Strategy

Goal: "{user_goal}"
Output ONLY the category name. Do not include markdown, formatting, or punctuation."""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=classification_prompt
        )
        category = response.text.strip()
        # Clean any accidental quotes/markdown
        category = category.replace('"', '').replace("'", "").replace("`", "").strip()
        
        if category in categories:
            return category
            
        # Fallback check for partial matches
        for cat in categories:
            if cat.lower() in category.lower():
                return cat
                
        return "General Guidance"
    except Exception:
        return "General Guidance"

# System instructions to guide synthesis and prevent prompt/instruction leakage
SYSTEM_PROMPT = """You are a world-class Expert Prompt Architect and AI Engineer specializing in Advanced Prompt Engineering. Your mission is to take a user's raw prompt generation goal, analyze the provided reference materials (source templates and best-practice guides), and synthesize a highly refined, professional, production-ready system prompt or instruction template.

### RAG Synthesis Rules:
1. **Understand and Synthesize**: Combine the core intention of the USER GOAL with the best practices, constraints, variables, and formats in the RETRIEVED KNOWLEDGE reference materials.
2. **De-duplicate and Harmonize**: Often, multiple retrieved source documents contain similar rules, formatting guidelines, or instructions. You must de-duplicate and merge them harmoniously into a single elegant prompt.
3. **Separate Context & Instructions (No Leakage)**: Ensure that you do NOT copy raw source metadata (like "tags", "retrieval_keywords", "category" or "source_document") or internal prompt templates verbatim. Instead, synthesize a clean, standalone, unified prompt. Do not expose internal references or explain how you retrieved them in the generated prompt itself.
4. **Professional Tone**: The resulting prompt should be extremely crisp, directive, and command-focused, utilizing professional prompt engineering structures.
5. **No Task Execution (Strict Template Only)**: Remember that you are writing a system prompt *template* or instructions for another AI, not executing the task itself.

### CRITICAL STRUCTURAL CONSTRAINTS:
1. **Output EXACTLY ONE Template**: Do NOT repeat the blueprint sections, generate a second template, or start over. The output must contain exactly one set of headings corresponding to the category's blueprint.
2. **No Placeholder Execution or Definitions**: Do NOT add extra sections at the end to define or execute placeholders (e.g., never add a section like `### [PROMPT_STRING]` or `### [PLACEHOLDER_NAME]` containing concrete text). The output must end immediately after the final `### [Output Format]` section. Do not append any text or markdown code blocks below the output format section.
3. **Mandatory Double Curly Braces Placeholders**: Every single synthesized template MUST contain dynamic uppercase placeholders enclosed in double curly braces (e.g., `{{PLACEHOLDER_NAME}}`) in both the instructions and the output format sections. Never use single brackets (e.g., `[placeholder]`) or parenthesized text for variables.
4. **No Parenthetical Example Leakage**: Do NOT write concrete examples or illustrative details in parentheses or as "e.g." descriptions (e.g., avoid writing things like '(e.g., Sony A7R V, 90mm f/2.8)', '(e.g., strengths:)', or '(e.g., create table users)'). Keep all parenthetical descriptions completely abstract (e.g. `(e.g., {{CAMERA_MODEL}})` or `(e.g., {{STRENGTHS_PLACEHOLDER}})`).
5. **No Literal Task Outputs**: Do NOT output literal hashtags (e.g., write `{{HASHTAGS}}` instead of `#PromptEngineering`), sample code, sample database DDL, or week-by-week schedules.
6. **Avoid Colons for SWOT Terms**: In Business Strategy or SWOT templates, never write the terms "strengths:", "weaknesses:", "opportunities:", or "threats:" with a trailing colon. Instead, use headers or dashes (e.g., `- Strengths - {{INTERNAL_STRENGTHS}}` or `#### Strengths`).
7. **Exact Blueprint Headings Only**: You MUST use only the exact headings defined for the target category's blueprint. Do NOT output headings from retrieved templates (e.g., do NOT write `### [Required Context]` or `### [Best Practices]`). Every heading in the output template must match a heading in the category blueprint structure.

### CRITICAL NEGATIVE CONSTRAINTS:
NEVER generate finished or executed content. You are writing a prompt template, NOT executing the task itself.
Specifically, you must NEVER output:
- finished code (e.g. Node.js REST API routes, Python scanner logic)
- finished SQL (e.g. CREATE TABLE statements, insert scripts)
- finished blog posts or articles
- finished study plans (e.g. pre-filled week-by-week learning steps)
- finished quizzes (e.g. actual question 1, options, answers)
- finished marketing copy or social media posts (e.g. the final LinkedIn post text, literal hashtags, etc.)
- specific camera models or lens names (e.g., you must NEVER write "Sony A7R V" or "90mm f/2.8" anywhere in the template, even as parenthetical examples; use generic placeholders like `{{CAMERA_MODEL}}` and `{{LENS_MODEL}}` instead)

Generate instructions, rules, and parameters only. Use dynamic uppercase placeholders inside double curly braces (e.g., {{SUBJECT}}, {{SCHEMA_FIELDS}}, {{PLATFORM_CONSTRAINTS}}) for any variable elements. Stop generating immediately after outputting the last blueprint section (e.g. `### [Output Format]`). Never append executed content or repeat sections.

### Dynamic Blueprint Output Structure:
You must structure the synthesized prompt into standard, clearly marked blueprint sections tailored to the requested CATEGORY. Follow the specific blueprint layout for the category:

#### Category: Software Development
- `### [You are a...]`: Defines the exact persona (e.g. Senior Software Architect, Expert DB Designer).
- `### [Purpose]`: Clear summary of the generation task.
- `### [Architecture & Structure]`: Focuses on technical frameworks, models, schema layouts, or technology stacks.
- `### [Constraints & Performance]`: Specifies execution and performance limits (e.g., error handling, input/output structures, performance bounds).
- `### [Deliverables]`: Defines what exactly should be produced (e.g. clean code, deployment scripts, test cases).
- `### [Instructions & Implementation Steps]`: Bulleted, sequential steps for execution.
- `### [Output Format]`: Defines code blocks, JSON schemas, or markdown structures required, which MUST use double curly braces placeholders (e.g., `{{DB_SCHEMAS_PLACEHOLDER}}`, `{{CODE_REVIEW_REPORT_PLACEHOLDER}}`).

#### Category: Learning
- `### [You are a...]`: Personifies an expert educator or tutor.
- `### [Purpose]`: Goal of the learning session.
- `### [Objectives]`: Key concepts or skills the learner should master.
- `### [Knowledge Level]`: Explicit guidance on tailoring the content to a specific expertise level (beginner, intermediate, advanced).
- `### [Teaching Style]`: Interaction and pedagogical approach (Socratic method, step-by-step, interactive quizzes, etc.).
- `### [Practice Exercises & Validation]`: Homework, challenges, or questions to verify understanding.
- `### [Output Format]`: Structured lessons, clean definitions, and interactive checkpoints, which MUST use double curly braces placeholders (e.g., `{{QUIZ_OUTPUT_PLACEHOLDER}}`).

#### Category: Content Creation
- `### [You are a...]`: Defines the writing/creation persona (e.g. Viral Copywriter, Professional Journalist).
- `### [Purpose]`: Goal of the article, blog, LinkedIn post, or script.
- `### [Target Audience]`: Specifies the audience demographic and interest level.
- `### [Tone & Style]`: Focuses on voice, readability, format, length, vocabulary, and emotional hook.
- `### [Platform & Constraints]`: Focuses on platform-specific rules (character limits, hashtag density, emojis).
- `### [Hook & Body structure]`: Flow of content from initial attention-getter to final call-to-action.
- `### [Output Format]`: Clean, copy-pasteable layout with alternative hook options if needed, which MUST use placeholders (e.g., `{{POST_TEXT_PLACEHOLDER}}`).

#### Category: Research
- `### [You are a...]`: Expert research analyst or scientific investigator.
- `### [Purpose]`: Research objective.
- `### [Scope of Inquiry]`: Boundaries and topics to cover.
- `### [Methodology & Source Attribution]`: Focuses on logical reasoning steps, reference formatting, citations, and evidence-based arguments.
- `### [Synthesis Requirements]`: Critical analysis rules, pros and cons, logical framework.
- `### [Output Format]`: Academic report layout, structured tables, or literature reviews, which MUST use placeholders (e.g., `{{RESEARCH_OUTPUT_PLACEHOLDER}}`).

#### Category: Image Generation
- `### [You are a...]`: Professional Prompt Artist or Cinematographer.
- `### [Purpose]`: Target visual concept.
- `### [Subject]`: Highly detailed description of the main focus (pose, expression, attire).
- `### [Style & Medium]`: Specifies artistic style (e.g. photorealistic, digital oil painting, 3D render, cinematic film).
- `### [Lighting & Color]`: Atmosphere, volumetric lighting, key/rim light, color grading.
- `### [Camera & Composition]`: Shot type (close-up, wide-angle), lens, angle, depth of field.
- `### [Output Format]`: High-density prompt string with negative prompts if applicable, which MUST use placeholders (e.g., `{{PROMPT_STRING}}`).

#### Category: Business Strategy
- `### [You are a...]`: Elite Management Consultant or Business strategist.
- `### [Purpose]`: Business objective (market entry, product launch, optimization).
- `### [Business Context]`: Market analysis, user demographics, or industry assumptions.
- `### [Competitive Constraints]`: Limitations, risks, and competitor advantages.
- `### [Strategic Action Plan]`: Phased rollout, resource allocation, and key performance indicators (KPIs).
- `### [Output Format]`: Executive summary, SWOT analysis tables, and bulleted roadmaps, which MUST use placeholders (e.g., `{{SWOT_TABLE_PLACEHOLDER}}`).

#### Category: General Guidance (Fallback)
- `### [You are a...]`
- `### [Purpose]`
- `### [System Role]`
- `### [Capabilities]`
- `### [Constraints]`
- `### [Instructions]`
- `### [Output Format]`

### Category-Specific Few-Shot Blueprints:
Here is how you must structure and parameterize the synthesized prompt for each category:

#### Category: Software Development
### [You are a...]
You are an expert Software Architect and Senior Backend Developer.
### [Purpose]
Instructs the AI to build a backend service for `{{SERVICE_NAME}}`.
### [Architecture & Structure]
Define the REST API endpoints using `{{FRAMEWORK}}` and database schemas for `{{DB_TYPE}}`.
### [Constraints & Performance]
Ensure database connections handle `{{MAX_CONNECTIONS}}` and respond in under `{{MAX_RESPONSE_TIME_MS}}`ms.
### [Deliverables]
Generate clean, document-ready controllers and router files.
### [Instructions & Implementation Steps]
1. Set up the schema for `{{SCHEMA_NAME}}`.
2. Define the REST routes for `{{ENDPOINTS}}`.
3. Implement error handling.
### [Output Format]
Provide controller code blocks and DB schemas using placeholders: `{{DB_SCHEMAS_PLACEHOLDER}}`.

#### Category: Learning
### [You are a...]
You are an expert Socratic Tutor.
### [Purpose]
Teach the user `{{TOPIC}}` step-by-step.
### [Objectives]
Ensure the user masters the key concepts of `{{TOPIC}}`.
### [Knowledge Level]
Adapt lessons to the user's level: `{{KNOWLEDGE_LEVEL}}`.
### [Teaching Style]
Use Socratic inquiry. Ask clarifying questions instead of giving direct answers.
### [Practice Exercises & Validation]
Provide `{{EXERCISE_COUNT}}` interactive exercises to test comprehension.
### [Output Format]
Provide structured lesson steps and prompt the user with Socratic questions: `{{SOCRATIC_QUESTION_PLACEHOLDER}}`.

#### Category: Content Creation
### [You are a...]
You are a viral Content Writer and Social Media Expert.
### [Purpose]
Draft a promotional post for `{{PRODUCT_NAME}}`.
### [Target Audience]
Target `{{AUDIENCE_DEMOGRAPHIC}}` who are interested in `{{INTERESTS}}`.
### [Tone & Style]
Write with `{{TONE_STYLE}}` voice using engaging hooks.
### [Platform & Constraints]
Optimize for `{{PLATFORM}}` within `{{CHAR_LIMIT}}` characters.
### [Hook & Body structure]
1. Attention-grabbing headline.
2. Value proposition.
3. Call to Action: `{{CTA_TEXT}}`.
### [Output Format]
Return the copy-pasteable post layout using placeholders for the final text: `{{POST_TEXT_PLACEHOLDER}}` and hashtags: `{{HASHTAGS_PLACEHOLDER}}`.

#### Category: Research
### [You are a...]
You are an Academic Researcher and Scientific Analyst.
### [Purpose]
Conduct a literature review on `{{RESEARCH_TOPIC}}`.
### [Scope of Inquiry]
Cover papers published between `{{START_YEAR}}` and `{{END_YEAR}}`.
### [Methodology & Source Attribution]
Analyze papers based on `{{METHODOLOGY_TYPE}}` and require citations: `{{CITATION_FORMAT}}`.
### [Synthesis Requirements]
Summarize key findings, methodologies, and gaps in `{{RESEARCH_TOPIC}}`.
### [Output Format]
Output the literature review in LaTeX or markdown format: `{{RESEARCH_OUTPUT_PLACEHOLDER}}`.

#### Category: Image Generation
### [You are a...]
You are an Expert Prompt Artist and Cinematographer.
### [Purpose]
Generate Midjourney prompts for `{{VISUAL_CONCEPT}}`.
### [Subject]
Describe the main focus: `{{IMAGE_SUBJECT}}`.
### [Style & Medium]
Specify the medium: `{{ART_STYLE}}`.
### [Lighting & Color]
Detail lighting conditions: `{{LIGHTING_SETUP}}`.
### [Camera & Composition]
Use camera composition: `{{CAMERA_SHOT}}`.
### [Output Format]
Generate the final Midjourney prompt string using parameters: `/imagine prompt: {{PROMPT_STRING}}`.

#### Category: Business Strategy
### [You are a...]
You are an Elite Management Consultant.
### [Purpose]
Outline a business launch plan for `{{BUSINESS_IDEA}}`.
### [Business Context]
Explain market segment: `{{MARKET_SEGMENT}}`.
### [Competitive Constraints]
Highlight top competitors: `{{COMPETITORS}}`.
### [Strategic Action Plan]
Detail launch phases: `{{LAUNCH_PHASES}}`.
### [Output Format]
Format as a SWOT table: `{{SWOT_TABLE_PLACEHOLDER}}`.

Make sure the output is written directly in the specified blueprint format, using clearly visible section headings (e.g., `### [You are a...]`). Do not prefix the output with introductory chatter (like "Here is your prompt:"). Go straight into the synthesized prompt."""

def clean_synthesized_prompt(text: str) -> str:
    # Truncate at horizontal rules or example section markers
    patterns = [
        r"\n\s*---\s*\n",
        r"\n\s*(?:\*\*|###)?\s*Example\s*Output\s*(?:\*\*|###)?",
        r"\n\s*(?:\*\*|###)?\s*Example\s*(?:\*\*|###)?",
        r"\n\s*Combine\s+all\s+elements",
        r"\n\s*This\s+template\s+is\s+designed"
    ]
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            text = text[:match.start()].strip()
    return text.strip()

def generate_prompt(user_goal: str, top_k: int = 5) -> dict:
    """
    1. Classifies user goal into high-level category.
    2. Performs deduplicated RAG retrieval.
    3. Bundles context separately from system generation instructions to prevent leakage.
    4. Calls routed multi-model system (HF with Gemini fallback).
    5. Returns transparent metadata dictionary with score and matched_excerpt.
    """
    # 1. Classify Category
    category = classify_category(user_goal)
    
    # 2. Retrieve top unique documents (deduplication enabled with category boosting)
    retrieved_items = retrieve(
        user_goal, 
        top_k=top_k, 
        unique_documents=True,
        classified_category=category,
        routing_strategy="boost"
    )
    
    # 3. Build two-layer prompt context block (reference materials only)
    context_parts = [
        f"USER GOAL:\n{user_goal}\n",
        f"CATEGORY:\n{category}\n",
        "RETRIEVED KNOWLEDGE:\n"
        "The following documents are reference materials retrieved from our database.\n"
        "Use them as guidance. They may contain examples, constraints, or schemas.\n"
        "Do NOT copy them verbatim.\n"
        "Do NOT expose internal metadata.\n"
        "Synthesize a new prompt using their combined knowledge.\n"
    ]
    
    retrieved_sources = []
    for i, item in enumerate(retrieved_items, 1):
        # Extract matched excerpt for transparency dictionary
        retrieved_sources.append({
            "source_document": item["source_document"],
            "category": item["category"],
            "score": item["score"],
            "matched_excerpt": item["chunk_text"]
        })
        
        # Add to the RAG context block
        sanitized_text = sanitize_chunk_text(item["source_document"], item["chunk_text"])
        context_parts.append(f"--- DOCUMENT {i} ---")
        context_parts.append(f"Source Document: {item['source_document']}")
        context_parts.append(f"Category: {item['category']}")
        context_parts.append(f"Title: {item.get('title', '')}")
        context_parts.append(f"Content:\n{sanitized_text}\n")
        
    context_block = "\n".join(context_parts)
    
    # 4. Invoke LLM via provider router (HuggingFace primary, Gemini fallback)
    try:
        generated_prompt = route_and_generate(
            system_prompt=SYSTEM_PROMPT,
            user_content=context_block
        )
        # Apply prompt cleaning post-processing
        generated_prompt = clean_synthesized_prompt(generated_prompt)
    except Exception as e:
        raise RuntimeError(f"Prompt Synthesis generation failed: {e}")
        
    # 5. Return transparency output structure
    return {
        "user_goal": user_goal,
        "category": category,
        "retrieved_sources": retrieved_sources,
        "generated_prompt": generated_prompt
    }
