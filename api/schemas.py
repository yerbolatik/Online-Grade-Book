from pydantic import BaseModel, validator
from typing import Optional, List
from datetime import datetime


class StudentBase(BaseModel):
    first_name: str
    last_name: str
    age: int
    grade: int

    @validator('grade')
    def validate_grade(cls, value):
        if value < 0 or value > 12:
            raise ValueError('Grade must be between 0 and 11')
        return value

    class Config:
        orm_mode = True
        json_encoders = {
            datetime: lambda v: v.strftime("%d %B %Y %H:%M:%S")
        }


class StudentCreate(StudentBase):
    pass


class StudentUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    age: Optional[int] = None
    grade: Optional[int] = None


class ScoreBase(BaseModel):
    subject: str
    score: int

    @validator('score')
    def validate_score(cls, value):
        if value < 0 or value > 5:
            raise ValueError('Score must be between 0 and 5')
        return value


class ScoreCreate(ScoreBase):
    student_id: int


class ScoreUpdate(ScoreBase):
    subject: Optional[str] = None
    score: Optional[int] = None
    student_id: Optional[int] = None


class Score(ScoreBase):
    id: int
    student_id: int
    created: datetime

    class Config:
        orm_mode = True
        json_encoders = {
            datetime: lambda v: v.strftime("%d %B %Y %H:%M:%S")
        }


class Student(StudentBase):
    id: int
    scores: List[Score] = []

    class Config:
        orm_mode = True
