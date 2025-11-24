from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from utils.db_session import get_db
from service.course_service import CourseService
from models.course_models import CourseCreate, CourseOut

router = APIRouter(prefix="/courses", tags=["Courses"])
service = None

@router.on_event("startup")
def init_service():
    global service
    service = CourseService(next(get_db()))

@router.get("/courses/", response_model=list[CourseOut])
def list_courses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return service.list_courses(skip, limit)

@router.get("/courses/{course_id}", response_model=CourseOut)
def get_course(course_id: int, db: Session = Depends(get_db)):
    return service.get_course(course_id)

@router.post("/courses/", response_model=CourseOut)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    return service.create_course(course)

@router.put("/courses/{course_id}", response_model=CourseOut)
def update_course(course_id: int, course: CourseCreate, db: Session = Depends(get_db)):
    return service.update_course(course_id, course)

@router.delete("/courses/{course_id}")
def delete_course(course_id: int, db: Session = Depends(get_db)):
    deleted = service.delete_course(course_id)
    if deleted:
        return {"message": f"Course with ID {course_id} deleted successfully"}
    else:
        return {"error": f"Course with ID {course_id} not found"}

