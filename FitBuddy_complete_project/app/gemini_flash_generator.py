from app.config import GEMINI_FLASH_MODEL
from app.gemini_client import generate

def generate_nutrition_tip_with_flash(goal):
    prompt = f"""
Give one concise, practical nutrition or recovery tip for a general wellness
user whose selected fitness goal is: {goal}.
Keep it evidence-aware, non-restrictive, and suitable for a teenager as well
as an adult. Avoid calorie targets, fasting instructions, supplements, or
medical claims. Mention hydration, balanced meals, sleep, or ordinary protein/
food sources where appropriate. Maximum 90 words.
"""
    return generate(GEMINI_FLASH_MODEL, prompt)
