from entities.marks import Marks

class MarksRepository:
    def __init__(self, db):
        self.db = db

    def get_all(self, skip: int = 0, limit: int = 100):
        return self.db.query(Marks).offset(skip).limit(limit).all()

    def get_by_id(self, mark_id: int):
        return self.db.query(Marks).filter(Marks.mark_id == mark_id).first()

    def create(self, marks: Marks):
        self.db.add(marks)
        self.db.commit()
        self.db.refresh(marks)
        return marks

    def update(self, mark_id: int, data: dict):
        db_mark = self.get_by_id(mark_id)
        if db_mark:
            for key, value in data.items():
                setattr(db_mark, key, value)
            self.db.commit()
            self.db.refresh(db_mark)
        return db_mark

    def delete(self, mark_id: int):
        db_mark = self.get_by_id(mark_id)
        if db_mark:
            self.db.delete(db_mark)
            self.db.commit()
        return db_mark
