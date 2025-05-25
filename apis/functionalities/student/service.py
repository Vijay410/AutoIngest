from repo.student.student_performance import StudentRepository
from models.student_performance import StudentsInfo
from fastapi import HTTPException, status
from schemas.student_performance import StudentPerformance

class StudentService:
    """
    Service for managing student performance records.
    """
    
    def __init__(self, repo: StudentRepository):
        self.repo = repo

    def get_student_by_id(
        self, 
        student_id: int
        ):

        """     
        Retrieve a student's performance record by their unique student ID.

        Args:
            student_id (int): The unique identifier of the student.

        Returns:
            StudentPerformance | None: 
            The performance record of the student if found, otherwise None."""
        
        # get student performance info from the repository
        student_performance_info = self.repo.get_student_by_id(student_id)
        # validate and return the student performance info if found
        if student_performance_info:
            return StudentPerformance.model_validate(student_performance_info)
        # return an HTTP exception if the student is not found
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with ID {student_id} not found."
        )

