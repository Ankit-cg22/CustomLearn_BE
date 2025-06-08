from pydantic import BaseModel, Field
from typing import List, Optional

class CourseItem(BaseModel):
    title: str
    type: str
    link: str
    expected_duration: str
    checked: Optional[bool] = None

class RoadmapWeek(BaseModel):
    week: int
    items: List[CourseItem]
    milestone: Optional[str] = None

class CourseCreate(BaseModel):
    email: str
    course_name: str
    roadmap: List[RoadmapWeek]

class CourseUpdate(BaseModel):
    course_name: Optional[str] = None
    roadmap: Optional[List[RoadmapWeek]] = None

class CourseInDB(CourseCreate):
    id: str = Field(validation_alias="_id", serialization_alias="_id")
