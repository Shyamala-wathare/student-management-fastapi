from sqlalchemy.orm import Session
from entities.student import Student


class StudentRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self, skip: int = 0, limit: int = 100):
        return self.db.query(Student).offset(skip).limit(limit).all()
    
    def get_by_id(self, student_id: int):
        return self.db.query(Student).filter(Student.student_id == student_id).first()
    
    def create(self, student: Student):
        self.db.add(student)
        self.db.commit()
        self.db.refresh(student)
        return student
    
    
    def update(self, student_id: int, data):
        student = self.get_by_id(student_id)
        if student:
            student.student_name = data.student_name
            student.email = data.email
            student.dob = data.dob
            self.db.commit()
            self.db.refresh(student)
        return student
    
    def delete(self, student_id: int):
        student = self.get_by_id(student_id)
        if student:
            self.db.delete(student)
            self.db.commit()
        return student