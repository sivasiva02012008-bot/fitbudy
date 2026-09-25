from app.config import GEMINI_PRO_MODEL
from app.gemini_client import generate

def generate_workout_gemini(name, age, weight, goal, intensity):
    prompt = f"""
You are FitBuddy, a careful fitness-planning assistant.
Create a practical 7-day beginner-friendly workout plan.

User:
Name: {name}
Age: {age}
Weight: {weight}
Goal: {goal}
Intensity: {intensity}

For each Day 1 through Day 7 include:
- Focus
- Warm-up (5–10 minutes)
- Main workout with exercise names and sets/reps or duration
- Rest guidance
- Cool-down/recovery

Keep the plan structured and easy to read. Do not prescribe medical treatment.
Use conservative, general wellness guidance. Tell the user to stop if they
experience pain, dizziness, or other concerning symptoms and seek appropriate
adult/professional help. Do not make promises about weight loss or muscle gain.
"""
    return generate(GEMINI_PRO_MODEL, prompt)
