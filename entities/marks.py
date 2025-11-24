from sqlalchemy import Column, Integer, ForeignKey, String
from database import Base

class Marks(Base):
    __tablename__ = "marks"

    mark_id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.student_id"))
    course_id = Column(Integer, ForeignKey("courses.course_id"))
    marks_obtained = Column(Integer)
    grade = Column(String(2))
