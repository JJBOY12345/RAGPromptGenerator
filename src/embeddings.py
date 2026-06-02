import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load environment variables from .env
load_dotenv()

# Environment validation & fail-fast key check
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found in environment variables.\n"
        "Please create a '.env' file in the project root containing:\n"
        "GEMINI_API_KEY=your_actual_api_key"
    )

# Configure google-genai Client
client = genai.Client(api_key=GEMINI_API_KEY)

# Deterministic Embedding Model - strictly no automatic switches at runtime
def get_active_embedding_model() -> str:
    return os.getenv("EMBEDDING_MODEL", "models/gemini-embedding-2")

def get_embedding(text: str, is_query: bool = False) -> list:
    """
    Generates a text embedding vector using the modernized google.genai Client.
    Employs the strictly configured EMBEDDING_MODEL with no silent runtime switches.
    """
    active_model = get_active_embedding_model()
    task_type = "RETRIEVAL_QUERY" if is_query else "RETRIEVAL_DOCUMENT"
    try:
        response = client.models.embed_content(
            model=active_model,
            contents=text,
            config=types.EmbedContentConfig(task_type=task_type)
        )
        return response.embeddings[0].values
    except Exception as e:
        raise RuntimeError(f"Gemini API Embedding generation failed using {active_model}: {e}")

def get_embeddings_batch(texts: list, is_query: bool = False) -> list:
    """
    Generates embeddings in a batch request for maximum efficiency.
    Employs the strictly configured EMBEDDING_MODEL with no silent runtime switches.
    """
    if not texts:
        return []
        
    active_model = get_active_embedding_model()
    task_type = "RETRIEVAL_QUERY" if is_query else "RETRIEVAL_DOCUMENT"
    try:
        response = client.models.embed_content(
            model=active_model,
            contents=texts,
            config=types.EmbedContentConfig(task_type=task_type)
        )
        return [emb.values for emb in response.embeddings]
    except Exception as e:
        raise RuntimeError(f"Gemini API Batch Embedding generation failed using {active_model}: {e}")
