from fastapi import APIRouter, HTTPException
from fastapi import Request
from app.chains import Chains

router = APIRouter()

@router.post("/generate")
async def generate_course(request: Request):
    data = await request.json()
    skill = data.get("skill")
    current_knowledge = data.get("currentKnowledge")
    hours_per_week = data.get("hoursPerWeek")
    no_of_weeks = data.get("noOfWeeks")
    learning_style = data.get("learningStyle")
    learning_goal = data.get("learningGoal")

    # Convert learningStyle array to comma-separated string
    if isinstance(learning_style, list):
        learning_style = ", ".join(learning_style)

    chains = Chains()
    res = chains.get_course_plan(
        skill=skill,
        current_knowledge=current_knowledge,
        hours_per_week=hours_per_week,
        no_of_weeks=no_of_weeks,
        learning_style=learning_style,
        learning_goal=learning_goal
    )
    return {"response": res}
