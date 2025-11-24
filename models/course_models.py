from typing import Optional
from pydantic import BaseModel

class CourseCreate(BaseModel):
    course_name: str
    duration: Optional[str] = None
    fees: Optional[float] = None
    description: Optional[str] = None
    credits: Optional[int] = None

    class Config:
        from_attributes = True  # replaces orm_mode in Pydantic v2


class CourseOut(CourseCreate):
    course_id: int
