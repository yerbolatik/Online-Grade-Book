from sqlalchemy.orm import Session, joinedload
from . import models, schemas
from datetime import datetime


def create_student(db: Session, student: schemas.StudentCreate):
    try:
        db_student = models.Student(**student.dict())
        db.add(db_student)
        db.commit()
        db.refresh(db_student)
        return db_student
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()


def get_student(db: Session, student_id: int):
    try:
        return db.query(models.Student).\
            options(joinedload(models.Student.scores)).\
            filter(models.Student.id == student_id).\
            first()
    finally:
        db.close()


def get_students(db: Session, skip: int = 0, limit: int = 10):
    try:
        return db.query(models.Student).offset(skip).limit(limit).all()
    finally:
        db.close()


def update_student(db: Session, student_id: int, student: schemas.StudentUpdate):
    try:
        db_student = db.query(models.Student).filter(
            models.Student.id == student_id).first()
        if db_student:
            for key, value in student.dict(exclude_unset=True).items():
                setattr(db_student, key, value)
            db.commit()
            db.refresh(db_student)
        return db_student
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()


def delete_student(db: Session, student_id: int):
    try:
        db_student = db.query(models.Student).filter(
            models.Student.id == student_id).first()
        db.delete(db_student)
        db.commit()
        return db_student
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()


def create_score(db: Session, score: schemas.ScoreCreate):
    try:
        db_score = models.Score(**score.dict())
        db.add(db_score)
        db.commit()
        db.refresh(db_score)
        return db_score
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()


def get_score(db: Session, score_id: int):
    try:
        return db.query(models.Score).filter(models.Score.id == score_id).first()
    finally:
        db.close()


def get_scores(db: Session, skip: int = 0, limit: int = 10):
    try:
        return db.query(models.Score).offset(skip).limit(limit).all()
    finally:
        db.close()


def update_score(db: Session, score_id: int, score: schemas.ScoreUpdate):
    try:
        db_score = db.query(models.Score).filter(
            models.Score.id == score_id).first()
        if db_score:
            for key, value in score.dict(exclude_unset=True).items():
                setattr(db_score, key, value)
            db.commit()
            db.refresh(db_score)
        return db_score
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()


def delete_score(db: Session, score_id: int):
    try:
        db_score = db.query(models.Score).filter(
            models.Score.id == score_id).first()
        db.delete(db_score)
        db.commit()
        return db_score
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()
