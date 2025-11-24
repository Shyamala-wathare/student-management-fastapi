import logging
from entities.course import Course
from repositories.course_repository import CourseRepository

class CourseService:
    def __init__(self, db):
        self.repo = CourseRepository(db)
        self.db = db
        self.logger = logging.getLogger("CourseService")   # Logger added

    def list_courses(self, skip: int = 0, limit: int = 100):
        self.logger.info(f"Fetching courses: skip={skip}, limit={limit}")
        return self.repo.get_all(skip, limit)

    def get_course(self, course_id: int):
        self.logger.info(f"Fetching course with ID: {course_id}")
        return self.repo.get_by_id(course_id)

    def create_course(self, data):
        self.logger.info(f"Creating new course: {data.course_name}")
        new_course = Course(
            course_name=data.course_name,
            description=data.description,
            credits=data.credits
        )
        return self.repo.create(new_course)

    def update_course(self, course_id: int, data):
        self.logger.info(f"Updating course ID: {course_id}")
        return self.repo.update(course_id, data.dict())

    def delete_course(self, course_id: int):
        self.logger.warning(f"Deleting course ID: {course_id}")
        course = self.db.query(Course).filter(Course.course_id == course_id).first()
        if course:
            self.db.delete(course)
            self.db.commit()
            return True
        return False
