import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = "FitBuddy"
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./fitbuddy.db")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")

# The supplied documentation specifies Gemini 1.5 Pro/Flash.
# These can be overridden in .env if your Gemini account exposes different models.
GEMINI_PRO_MODEL = os.getenv("GEMINI_PRO_MODEL", "gemini-1.5-pro")
GEMINI_FLASH_MODEL = os.getenv("GEMINI_FLASH_MODEL", "gemini-1.5-flash")
