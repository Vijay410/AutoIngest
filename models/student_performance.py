from sqlalchemy import Column, Intger, String, Float
from db.base import Base

class StudentPerformance(Base):
    __tablename__ = "students"
    Id = Column(Integer, primary_key=True, index=True)
    Gender = Column(String(10))
    RaceOrEthnicity = Column(String)
    ParentalLevelOfEducation = Column(String)
    Lunch = Column(String(20))
    TestPreparationCourse = Column(String(50))
    MathScore = Column(Integer)
    ReadingScore = Column(Integer)
    WritingScore = Column(Integer)
