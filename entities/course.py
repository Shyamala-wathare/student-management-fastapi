from sqlalchemy import Column, Integer, String, Text
from database import Base

class Course(Base):
    __tablename__ = "courses"

    course_id = Column(Integer, primary_key=True, index=True)
    course_name = Column(String(100), nullable=False)
    duration = Column(String(50), nullable=True)
    fees = Column(Integer, nullable=True)
    description = Column(Text, nullable=True)
    credits = Column(Integer, nullable=True)
