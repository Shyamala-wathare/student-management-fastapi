from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from utils.db_session import get_db
from service.marks_service import MarksService
from models.marks_models import MarksCreate, MarksResponse
from typing import List

router = APIRouter(prefix="/marks", tags=["Marks"])

@router.get("/", response_model=List[MarksResponse])
def list_marks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    service = MarksService(db)
    return service.list_marks(skip, limit)

@router.get("/{mark_id}", response_model=MarksResponse)
def get_marks(mark_id: int, db: Session = Depends(get_db)):
    service = MarksService(db)
    return service.get_marks(mark_id)

@router.post("/", response_model=MarksResponse)
def create_marks(data: MarksCreate, db: Session = Depends(get_db)):
    service = MarksService(db)
    return service.create_marks(data)

@router.put("/{mark_id}", response_model=MarksResponse)
def update_marks(mark_id: int, data: MarksCreate, db: Session = Depends(get_db)):
    service = MarksService(db)
    return service.update_marks(mark_id, data)

@router.delete("/{mark_id}", response_model=MarksResponse)
def delete_marks(mark_id: int, db: Session = Depends(get_db)):
    service = MarksService(db)
    return service.delete_marks(mark_id)
