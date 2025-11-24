from pydantic import BaseModel

class MarksBase(BaseModel):
    student_id: int
    course_id: int
    marks_obtained: int
    grade: str

class MarksCreate(MarksBase):
    pass

class MarksResponse(MarksBase):
    mark_id: int

    class Config:
        from_attributes = True
