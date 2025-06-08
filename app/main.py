from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.course_generation import router as course_generation_router
from .api.courses import router as courses_router

app = FastAPI()

# Allow CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(course_generation_router)
app.include_router(courses_router)

@app.get("/")
def hello() -> dict[str , str]:
    return {"response": "hello"}
