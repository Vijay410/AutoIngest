from sqlalchemy.orm import Session
from typing import List, Optional
from models.student_performance import StudentsInfo


class StudentRepository:
    """
    Repository for managing students data.
    """
    def __init__(
        self, 
        db: Session
        ):
        self.db = db

    def get_student_by_id(
        self, 
        student_id: int
        ) -> StudentsInfo | None:
        """Retrieve a student by studentID."""
        return self.db.query(StudentsInfo).\
            filter(
                StudentsInfo.StudentID == student_id
                ).first()

