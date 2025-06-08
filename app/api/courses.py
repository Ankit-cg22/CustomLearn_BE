from fastapi import APIRouter, HTTPException, status
from typing import List
from app.models import CourseCreate, CourseUpdate, CourseInDB
from app.db import courses_collection
from bson import ObjectId

router = APIRouter()

# Helper to convert MongoDB document to dict with string id
def course_helper(course) -> dict:
    course["_id"] = str(course["_id"])
    return course

@router.post("/courses", response_model=CourseInDB, status_code=status.HTTP_201_CREATED)
async def create_course(course: CourseCreate):
    course_dict = course.model_dump()
    result = await courses_collection.insert_one(course_dict)
    course_dict["_id"] = str(result.inserted_id)
    return course_dict

@router.get("/courses/{email}", response_model=List[CourseInDB])
async def get_courses(email: str):
    courses = await courses_collection.find({"email": email}).to_list(100)
    return [course_helper(c) for c in courses]

@router.post("/courses/add", response_model=CourseInDB, status_code=status.HTTP_201_CREATED)
async def add_course(course: CourseCreate):
    course_dict = course.model_dump()
    result = await courses_collection.insert_one(course_dict)
    course_dict["_id"] = str(result.inserted_id)
    return course_dict

@router.put("/courses/update/{course_id}", response_model=CourseInDB)
async def update_course(course_id: str, course: CourseUpdate):
    update_data = {k: v for k, v in course.model_dump(exclude_unset=True).items()}
    if not update_data:
        raise HTTPException(status_code=400, detail="No data to update")
    result = await courses_collection.find_one_and_update(
        {"_id": ObjectId(course_id)},
        {"$set": update_data},
        return_document=True
    )
    if not result:
        raise HTTPException(status_code=404, detail="Course not found")
    return course_helper(result)

@router.delete("/courses/{course_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_course(course_id: str):
    result = await courses_collection.delete_one({"_id": ObjectId(course_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Course not found")
    return None
