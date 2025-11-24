from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session

from utils.jwt_handler import create_access_token, verify_token
from utils.db_session import get_db
from entities.student import Student

router = APIRouter(prefix="/auth", tags=["Auth"])
security = HTTPBearer()


class SignupRequest(BaseModel):
    student_name: str
    email: str
    dob: str | None = None
    password: str


class LoginRequest(BaseModel):
    email: str
    password: str


# ------------------ SIGNUP ------------------
@router.post("/signup")
def signup(data: SignupRequest, db: Session = Depends(get_db)):
    existing = db.query(Student).filter(Student.email == data.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    import bcrypt
    hashed = bcrypt.hashpw(data.password.encode(), bcrypt.gensalt()).decode()

    user = Student(
        student_name=data.student_name,
        email=data.email,
        dob=data.dob,
        password=hashed
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return {"message": "User created", "student_id": user.student_id}


# ------------------ LOGIN ------------------
@router.post("/login")
def login(data: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(Student).filter(Student.email == data.email).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    import bcrypt
    if not bcrypt.checkpw(data.password.encode(), user.password.encode()):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    # FIXED → pass only the email!
    token = create_access_token(user.email)

    return {"access_token": token, "token_type": "bearer"}


# ------------------ TOKEN VERIFICATION ------------------
def get_current_user(token=Depends(security), db: Session = Depends(get_db)):
    email = verify_token(token.credentials)

    if not email:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    user = db.query(Student).filter(Student.email == email).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    return user
