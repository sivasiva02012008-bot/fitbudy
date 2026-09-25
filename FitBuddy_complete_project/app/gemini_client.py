from google import genai
from app.config import GEMINI_API_KEY

_client = genai.Client(api_key=GEMINI_API_KEY) if GEMINI_API_KEY else None

def generate(model: str, prompt: str) -> str:
    if not _client:
        raise RuntimeError("GEMINI_API_KEY is not configured. Add it to your .env file.")
    response = _client.models.generate_content(
        model=model,
        contents=prompt,
    )
    text = getattr(response, "text", None)
    if not text:
        raise RuntimeError("Gemini returned an empty response.")
    return text.strip()
