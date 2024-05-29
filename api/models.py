from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


Base = declarative_base()


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)
    grade = Column(Integer)

    scores = relationship(
        "Score", back_populates="student", cascade="all, delete")


class Score(Base):
    __tablename__ = "scores"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    subject = Column(String, index=True)
    score = Column(Integer)
    created = Column(DateTime, default=datetime.now)

    student = relationship("Student", back_populates="scores")
