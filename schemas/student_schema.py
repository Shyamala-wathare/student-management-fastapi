from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional

class StudentBase(BaseModel):
    student_name: str
    email: EmailStr
    dob: Optional[date] = None

class StudentCreate(StudentBase):
    password: str  

class StudentUpdate(BaseModel):
    student_name: Optional[str] = None
    email: Optional[EmailStr] = None
    dob: Optional[date] = None

class StudentOut(StudentBase):
    student_id: int
    class Config:
        from_attributes = True
