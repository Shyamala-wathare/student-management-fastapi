import logging
from entities.marks import Marks
from repositories.marks_repository import MarksRepository

class MarksService:
    def __init__(self, db):
        self.repo = MarksRepository(db)
        self.db = db
        self.logger = logging.getLogger("MarksService")

    def list_marks(self, skip: int = 0, limit: int = 100):
        self.logger.info(f"Fetching marks: skip={skip}, limit={limit}")
        return self.repo.get_all(skip, limit)

    def get_marks(self, mark_id: int):
        self.logger.info(f"Fetching marks with ID: {mark_id}")
        return self.repo.get_by_id(mark_id)

    def create_marks(self, data):
        self.logger.info(
            f"Creating marks for student_id={data.student_id}, course_id={data.course_id}, marks={data.marks_obtained}"
        )
        new_mark = Marks(
            student_id=data.student_id,
            course_id=data.course_id,
            marks_obtained=data.marks_obtained,
            grade=data.grade
        )
        return self.repo.create(new_mark)

    def update_marks(self, mark_id: int, data):
        self.logger.info(f"Updating marks entry with ID: {mark_id}")
        return self.repo.update(mark_id, data.dict())

    def delete_marks(self, mark_id: int):
        self.logger.warning(f"Deleting marks entry with ID: {mark_id}")
        return self.repo.delete(mark_id)
