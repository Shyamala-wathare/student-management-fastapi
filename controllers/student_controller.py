from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas.student_schema import StudentCreate, StudentUpdate, StudentOut
from service.student_service import StudentService
from controllers.auth_controller import get_current_user

router = APIRouter(prefix="/students", tags=["Students"])


# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# -----------------------------
# CREATE STUDENT (PUBLIC)
# -----------------------------
@router.post("/", response_model=StudentOut)
def create_student(data: StudentCreate, db: Session = Depends(get_db)):
    return StudentService(db).create_student(data)


# -----------------------------
# GET ALL STUDENTS (PROTECTED)
# -----------------------------
@router.get("/", response_model=list[StudentOut])
def list_students(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
   return StudentService(db).list_students(skip, limit)


# -----------------------------
# GET SINGLE STUDENT (PROTECTED)
# -----------------------------
@router.get("/{student_id}", response_model=StudentOut)
def get_student(
    student_id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    student = StudentService(db).get_student_by_id(student_id)

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


# -----------------------------
# UPDATE STUDENT (PROTECTED)
# -----------------------------
@router.put("/{student_id}", response_model=StudentOut)
def update_student(
    student_id: int,
    data: StudentUpdate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    updated = StudentService(db).update_student(student_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Student not found")
    return updated


# -----------------------------
# DELETE STUDENT (PROTECTED)
# -----------------------------
@router.delete("/{student_id}")
def delete_student(
    student_id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    deleted = StudentService(db).delete_student(student_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student deleted successfully"}
