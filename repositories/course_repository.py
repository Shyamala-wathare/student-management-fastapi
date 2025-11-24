from entities.course import Course

class CourseRepository:
    def __init__(self, db):
        self.db = db

    def get_all(self, skip: int = 0, limit: int = 100):
        return self.db.query(Course).offset(skip).limit(limit).all()

    def get_by_id(self, course_id: int):
        return self.db.query(Course).filter(Course.course_id == course_id).first()

    def create(self, course: Course):
        self.db.add(course)
        self.db.commit()
        self.db.refresh(course)
        return course

    def update(self, course_id: int, updated_data: dict):
        course = self.get_by_id(course_id)
        if course:
            for key, value in updated_data.items():
                setattr(course, key, value)
            self.db.commit()
            self.db.refresh(course)
        return course

    def delete(self, course_id: int):
        course = self.get_by_id(course_id)
        if course:
            self.db.delete(course)
            self.db.commit()
        return course
