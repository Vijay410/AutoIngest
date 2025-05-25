from typing import Optional, Dict, Any
from pydantic import BaseModel, Field

class StudentPerformance(BaseModel):
    StudentID: Optional[int] = Field(default=None, alias="studentId")
    StudentAdmissionNumber: Optional[str] = Field(default=None, alias="studentAdmissionNumber")
    Gender: Optional[str] = Field(default=None, alias="gender")
    RaceOREthnicity: Optional[str] = Field(default=None, alias="raceOrEthnicity")
    ParentalLevelOfEducation: Optional[str] = Field(default=None, alias="parentalLevelOfEducation")
    Lunch: Optional[str] = Field(default=None, alias="lunch")
    TestPreparationCource: Optional[str] = Field(default=None, alias="testPreparationCourse")
    MathScore: Optional[int] = Field(default=None, alias="mathScore")
    ReadingScore: Optional[int] = Field(default=None, alias="readingScore")
    WritingScore: Optional[int] = Field(default=None, alias="writingScore")

    class Config:
        from_attributes = True
        populate_by_name = True