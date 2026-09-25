from app.config import GEMINI_PRO_MODEL
from app.gemini_client import generate

def update_workout_plan(original_plan, feedback):
    prompt = f"""
You are updating a FitBuddy 7-day general fitness plan.

ORIGINAL PLAN:
{original_plan}

USER FEEDBACK:
{feedback}

Return a revised 7-day plan. Preserve useful parts of the original plan,
incorporate reasonable feedback, and keep exercise guidance conservative.
Do not provide medical treatment, extreme dieting, unsafe challenges, or
instructions that encourage exercising through pain. Keep the same clear
Day 1–Day 7 structure with focus, warm-up, main workout, rest, and cooldown.
"""
    return generate(GEMINI_PRO_MODEL, prompt)
