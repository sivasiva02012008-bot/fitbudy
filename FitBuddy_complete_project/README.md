# FitBuddy – AI Fitness Plan Generator

FitBuddy is the FastAPI + Jinja2 + SQLite + Gemini application described in the supplied project document.

## Features
- Personalized 7-day workout plan
- Nutrition/recovery tip
- Feedback-based plan revision
- SQLite persistence
- Admin/demo dashboard
- FastAPI JSON/API documentation
- Health endpoint

## Project structure
```text
FitBuddy/
├─ app/
│  ├─ __init__.py
│  ├─ main.py
│  ├─ config.py
│  ├─ database.py
│  ├─ schemas.py
│  ├─ gemini_client.py
│  ├─ gemini_generator.py
│  ├─ gemini_flash_generator.py
│  ├─ updated_plan.py
│  └─ routes.py
├─ templates/
│  ├─ index.html
│  ├─ result.html
│  └─ all_users.html
├─ static/style.css
├─ requirements.txt
├─ .env.example
└─ .gitignore
```

## VS Code setup – Windows
1. Open the `FitBuddy` folder in VS Code.
2. Open Terminal → New Terminal.
3. Create environment:
   `python -m venv .venv`
4. Activate:
   `.venv\Scripts\activate`
5. Install:
   `pip install -r requirements.txt`
6. Copy `.env.example` to `.env`.
7. Put your Gemini API key in `.env`.
8. Start:
   `uvicorn app.main:app --reload`
9. Open:
   `http://127.0.0.1:8000`
10. API docs:
   `http://127.0.0.1:8000/docs`

## macOS/Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

## Testing
- Browser: submit a plan from the home page.
- Feedback: submit feedback from the result page.
- Dashboard: `/view-all-users`
- Health: `/health`
- Swagger UI: `/docs`

For an API-only test, the application exposes the FastAPI documentation at `/docs`.

## Gemini model note
The project document specifies Gemini 1.5 Pro for workout generation and Gemini Flash for nutrition. Those defaults are retained in `.env.example`. Google’s current Python SDK is `google-genai`; if your account no longer exposes those legacy model IDs, set `GEMINI_PRO_MODEL` and `GEMINI_FLASH_MODEL` to model IDs available to your API account.

## Safety
This is a general wellness demo, not medical care. AI output should be reviewed by a qualified adult/professional where appropriate.
