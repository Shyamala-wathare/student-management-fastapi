from pydantic import BaseModel
from typing import Optional

class CourseCreate(BaseModel):
    course_name: str
    duration: Optional[str] = None
    fees: Optional[float] = None
    description: Optional[str] = None
    credits: Optional[int] = None

    class Config:
        from_attributes = True

class CourseUpdate(BaseModel):
    course_name: Optional[str] = None
    duration: Optional[str] = None
    fees: Optional[float] = None
    description: Optional[str] = None
    credits: Optional[int] = None

class CourseOut(CourseCreate):
    course_id: int
