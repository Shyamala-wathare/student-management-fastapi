import logging
from repositories.student_repository import StudentRepository
from entities.student import Student
from models.student_models import StudentCreate, StudentUpdate
from sqlalchemy.orm import Session
from utils.hash_utils import hash_password     # <-- ADD THIS LINE

class StudentService:
    def __init__(self, db: Session):
        self.repo = StudentRepository(db)
        self.logger = logging.getLogger("StudentService")

    def list_students(self, skip=0, limit=100):
        self.logger.info(f"Fetching students: skip={skip}, limit={limit}")
        return self.repo.get_all(skip, limit)
    
    def get_student_by_id(self, student_id):
        self.logger.info(f"Fetching student with ID: {student_id}")
        return self.repo.get_by_id(student_id)
    
    def create_student(self, data: StudentCreate):
        self.logger.info(f"Creating new student: {data.student_name}")

        # 1️⃣ Hash password
        hashed_pw = hash_password(data.password)

        # 2️⃣ Save hashed password
        new_student = Student(
            student_name=data.student_name,
            email=data.email,
            dob=data.dob,
            password=hashed_pw          # <-- NEW FIELD
        )
        return self.repo.create(new_student)

    def update_student(self, student_id, data: StudentUpdate):
        self.logger.info(f"Updating student ID: {student_id}")
        return self.repo.update(student_id, data)
    
    def delete_student(self, student_id):
        self.logger.warning(f"Deleting student ID: {student_id}")
        return self.repo.delete(student_id)
