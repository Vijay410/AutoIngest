from sqlalchemy import Column, String, Float, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class StudentsInfo(Base):
    __tablename__ = "StudentsInfo"
    StudentID = Column(Integer, primary_key=True, index=True)
    StudentAdmissionNumber = Column(String(50), unique=True, nullable=False)
    Gender = Column(String(10))
    RaceOREthnicity = Column(String)
    ParentalLevelOfEducation = Column(String)
    Lunch = Column(String(20))
    TestPreparationCource = Column(String(50))
    MathScore = Column(Integer)
    ReadingScore = Column(Integer)
    WritingScore = Column(Integer)
