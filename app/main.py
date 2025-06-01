from fastapi import FastAPI
from .api.course_generation import router as course_generation_router

app = FastAPI()

app.include_router(course_generation_router)

@app.get("/")
def hello() -> dict[str , str]:
    return {"response": "hello"}
