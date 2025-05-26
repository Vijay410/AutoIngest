from typing import Optional, Dict, Any
from fastapi import Depends
from db.database import Session, create_session
from repo.student.student_performance import StudentRepository
from apis.functionalities.student.service import StudentService

class StudentFactory:
    def __init__(
        self, 
        repo: StudentRepository
        ):
        self.repo = repo

    def get_service(self) -> StudentService:
        """
        Create and return an instance of StudentService using the provided repository.
        
        Returns:
            StudentService: An instance of StudentService initialized with the repository.
        """
        return StudentService(
            repo=self.repo
            )

def get_student_service(
    db: Session = Depends(create_session)

)-> StudentService:
    """
    Dependency injection function to provide an instance of StudentService.
    
    Args:
        db (Session): The database session dependency.
        
    Returns:
        StudentService: An instance of StudentService.
    """
    repo = StudentRepository(db=db)
    factory = StudentFactory(repo=repo)
    return factory.get_service()
