from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from app.schemas import UserInput, FeedbackRequest
from app.database import (
    save_user, save_plan, get_user, get_latest_plan, update_plan,
    get_all_users, delete_user
)
from app.gemini_generator import generate_workout_gemini
from app.gemini_flash_generator import generate_nutrition_tip_with_flash
from app.updated_plan import update_workout_plan

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.post("/generate-workout", response_class=HTMLResponse)
def generate_workout(
    request: Request,
    name: str = Form(...),
    user_id: str = Form(...),
    age: int = Form(...),
    weight: str = Form(...),
    goal: str = Form(...),
    intensity: str = Form(...)
):
    try:
        data = UserInput(user_id=user_id, name=name, age=age, weight=weight,
                         goal=goal, intensity=intensity)
        user = save_user(data)
        plan = generate_workout_gemini(data.name, data.age, data.weight, data.goal, data.intensity)
        tip = generate_nutrition_tip_with_flash(data.goal)
        saved = save_plan(user.id, plan, tip)
        return templates.TemplateResponse("result.html", {
            "request": request, "user": user, "plan": saved,
            "error": None
        })
    except Exception as exc:
        return templates.TemplateResponse("index.html", {
            "request": request,
            "error": str(exc)
        }, status_code=500)

@router.post("/submit-feedback", response_class=HTMLResponse)
def submit_feedback(
    request: Request,
    user_id: str = Form(...),
    feedback: str = Form(...)
):
    try:
        req = FeedbackRequest(user_id=user_id, feedback=feedback)
        user = get_user(req.user_id)
        plan = get_latest_plan(req.user_id)
        if not user or not plan:
            return templates.TemplateResponse("result.html", {
                "request": request, "user": user, "plan": plan,
                "error": "User or workout plan not found."
            }, status_code=404)

        revised = update_workout_plan(plan.original_plan, req.feedback)
        saved = update_plan(plan.id, revised, req.feedback)
        return templates.TemplateResponse("result.html", {
            "request": request, "user": user, "plan": saved,
            "message": "Your plan was updated successfully.",
            "error": None
        })
    except Exception as exc:
        return templates.TemplateResponse("result.html", {
            "request": request, "user": get_user(user_id),
            "plan": get_latest_plan(user_id), "error": str(exc)
        }, status_code=500)

@router.get("/view-all-users", response_class=HTMLResponse)
def view_all_users(request: Request):
    return templates.TemplateResponse("all_users.html", {
        "request": request, "users": get_all_users()
    })

@router.post("/delete-user")
def remove_user(user_id: str = Form(...)):
    delete_user(user_id)
    return RedirectResponse("/view-all-users", status_code=303)

@router.get("/health")
def health():
    return {"status": "ok"}
