import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Controllers
from controllers import student_controller, course_controller, marks_controller
from controllers import auth_controller

# Database
from database import engine, Base


# -------------------------------------------------------
# LOGGING
# -------------------------------------------------------

logging.getLogger().handlers.clear()

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"

logging.basicConfig(
    level=logging.INFO,
    format=LOG_FORMAT
)

# SQLAlchemy Logging
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

logger = logging.getLogger("StudentApp")
logger.info("Application Started")


# -------------------------------------------------------
# FASTAPI APP
# -------------------------------------------------------

app = FastAPI(title="Student Management System")


# -------------------------------------------------------
# CORS
# -------------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -------------------------------------------------------
# DATABASE INIT (IMPORTANT)
# -------------------------------------------------------

@app.on_event("startup")
def startup_event():
    logger.info("🔌 Connecting to database...")
    Base.metadata.create_all(bind=engine)
    logger.info("🔥 DATABASE TABLES CHECKED/CREATED 🔥")


# -------------------------------------------------------
# ROUTERS
# -------------------------------------------------------

app.include_router(auth_controller.router)
app.include_router(student_controller.router)
app.include_router(course_controller.router)
app.include_router(marks_controller.router)


# -------------------------------------------------------
# HOME
# -------------------------------------------------------

@app.get("/")
def home():
    logger.info("Home API called")
    return {"message": "Student Management System API is running!"}
