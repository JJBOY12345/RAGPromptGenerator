import os
from dotenv import load_dotenv
from google import genai
from src.retriever import retrieve
from src.providers import route_and_generate

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
5. **No Task Execution (Strict Template Only)**: Remember that you are writing a system prompt *template* or instructions for another AI, not executing the task itself. For example, if the goal is to design a study plan, write a post, or build an application, do NOT write the actual study plan chapters/weeks, the actual post content, or the application code. Use dynamic placeholder variables like `{{SUBJECT}}`, `{{CURRENT_LEVEL}}`, or `{{WEEKS}}` inside the template. Stop generating immediately after outputting the last blueprint section (e.g. `### [Output Format]`). Never append executed content or repeat sections.

### Dynamic Blueprint Output Structure:
You must structure the synthesized prompt into standard, clearly marked blueprint sections tailored to the requested CATEGORY. Follow the specific blueprint layout for the category:

#### Category: Software Development
- `[You are a...]`: Defines the exact persona (e.g. Senior Software Architect, Expert DB Designer).
- `[Purpose]`: Clear summary of the generation task.
- `[Architecture & Structure]`: Focuses on technical frameworks, models, schema layouts, or technology stacks.
- `[Constraints & Performance]`: Specifies execution and performance limits (e.g., error handling, input/output structures, performance bounds).
- `[Deliverables]`: Defines what exactly should be produced (e.g. clean code, deployment scripts, test cases).
- `[Instructions & Implementation Steps]`: Bulleted, sequential steps for execution.
- `[Output Format]`: Defines code blocks, JSON schemas, or markdown structures required.

#### Category: Learning
- `[You are a...]`: Personifies an expert educator or tutor.
- `[Purpose]`: Goal of the learning session.
- `[Objectives]`: Key concepts or skills the learner should master.
- `[Knowledge Level]`: Explicit guidance on tailoring the content to a specific expertise level (beginner, intermediate, advanced).
- `[Teaching Style]`: Interaction and pedagogical approach (Socratic method, step-by-step, interactive quizzes, etc.).
- `[Practice Exercises & Validation]`: Homework, challenges, or questions to verify understanding.
- `[Output Format]`: Structured lessons, clean definitions, and interactive checkpoints.

#### Category: Content Creation
- `[You are a...]`: Defines the writing/creation persona (e.g. Viral Copywriter, Professional Journalist).
- `[Purpose]`: Goal of the article, blog, LinkedIn post, or script.
- `[Target Audience]`: Specifies the audience demographic and interest level.
- `[Tone & Style]`: Focuses on voice, readability, format, length, vocabulary, and emotional hook.
- `[Platform & Constraints]`: Focuses on platform-specific rules (character limits, hashtag density, emojis).
- `[Hook & Body structure]`: Flow of content from initial attention-getter to final call-to-action.
- `[Output Format]`: Clean, copy-pasteable layout with alternative hook options if needed.

#### Category: Research
- `[You are a...]`: Expert research analyst or scientific investigator.
- `[Purpose]`: Research objective.
- `[Scope of Inquiry]`: Boundaries and topics to cover.
- `[Methodology & Source Attribution]`: Focuses on logical reasoning steps, reference formatting, citations, and evidence-based arguments.
- `[Synthesis Requirements]`: Critical analysis rules, pros and cons, logical framework.
- `[Output Format]`: Academic report layout, structured tables, or literature reviews.

#### Category: Image Generation
- `[You are a...]`: Professional Prompt Artist or Cinematographer.
- `[Purpose]`: Target visual concept.
- `[Subject]`: Highly detailed description of the main focus (pose, expression, attire).
- `[Style & Medium]`: Specifies artistic style (e.g. photorealistic, digital oil painting, 3D render, cinematic film).
- `[Lighting & Color]`: Atmosphere, volumetric lighting, key/rim light, color grading.
- `[Camera & Composition]`: Shot type (close-up, wide-angle), lens, angle, depth of field.
- `[Output Format]`: High-density prompt string with negative prompts if applicable.

#### Category: Business Strategy
- `[You are a...]`: Elite Management Consultant or Business strategist.
- `[Purpose]`: Business objective (market entry, product launch, optimization).
- `[Business Context]`: Market analysis, user demographics, or industry assumptions.
- `[Competitive Constraints]`: Limitations, risks, and competitor advantages.
- `[Strategic Action Plan]`: Phased rollout, resource allocation, and key performance indicators (KPIs).
- `[Output Format]`: Executive summary, SWOT analysis tables, and bulleted roadmaps.

#### Category: General Guidance (Fallback)
- `[You are a...]`
- `[Purpose]`
- `[System Role]`
- `[Capabilities]`
- `[Constraints]`
- `[Instructions]`
- `[Output Format]`

Make sure the output is written directly in the specified blueprint format, using clearly visible section headings (e.g., `### [You are a...]`). Do not prefix the output with introductory chatter (like "Here is your prompt:"). Go straight into the synthesized prompt."""

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
        context_parts.append(f"--- DOCUMENT {i} ---")
        context_parts.append(f"Source Document: {item['source_document']}")
        context_parts.append(f"Category: {item['category']}")
        context_parts.append(f"Title: {item.get('title', '')}")
        context_parts.append(f"Content:\n{item['chunk_text']}\n")
        
    context_block = "\n".join(context_parts)
    
    # 4. Invoke LLM via provider router (HuggingFace primary, Gemini fallback)
    try:
        generated_prompt = route_and_generate(
            system_prompt=SYSTEM_PROMPT,
            user_content=context_block
        )
    except Exception as e:
        raise RuntimeError(f"Prompt Synthesis generation failed: {e}")
        
    # 5. Return transparency output structure
    return {
        "user_goal": user_goal,
        "category": category,
        "retrieved_sources": retrieved_sources,
        "generated_prompt": generated_prompt
    }
