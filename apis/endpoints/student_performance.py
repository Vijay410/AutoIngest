from typing import Optional, Dict, List
from fastapi import APIRouter, Depends, HTTPException, Path
from apis.functionalities.student.service import StudentService
from apis.functionalities.student.factory import get_student_service

router = APIRouter()

@router.get("/students/student-performance/{student_id}")
def get_student_performance(
    student_id: int = Path(..., description="The unique identifier of the student"),
    student_service: StudentService = Depends(get_student_service)
):
    """
    Retrieve a student's performance record by their unique student ID.
    """
    return student_service.get_student_by_id(
        student_id=student_id
        )
