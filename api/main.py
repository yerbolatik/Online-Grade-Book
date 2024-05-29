from fastapi import FastAPI, Depends, HTTPException, Response
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from . import crud, models, schemas, database

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)


# Редирект на документацию
@app.get("/", include_in_schema=False)
async def redirect_to_docs():
    return RedirectResponse(url="/docs")


# Маршруты для работы с студентами
@app.post("/students/", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, db: Session = Depends(database.get_db)):
    return crud.create_student(db=db, student=student)


@app.get("/students/{student_id}", response_model=schemas.Student)
def read_student(student_id: int, db: Session = Depends(database.get_db)):
    db_student = crud.get_student(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student


@app.patch("/students/{student_id}", response_model=schemas.Student)
def update_student(student_id: int, student: schemas.StudentUpdate, db: Session = Depends(database.get_db)):
    return crud.update_student(db=db, student_id=student_id, student=student)


@app.delete("/students/{student_id}", response_model=schemas.Student)
def delete_student(student_id: int, db: Session = Depends(database.get_db)):
    return crud.delete_student(db=db, student_id=student_id)


# Маршруты для работы с оценками
@app.post("/scores/", response_model=schemas.Score)
def create_score(score: schemas.ScoreCreate, db: Session = Depends(database.get_db)):
    return crud.create_score(db=db, score=score)


@app.get("/scores/{score_id}", response_model=schemas.Score)
def read_score(score_id: int, db: Session = Depends(database.get_db)):
    db_score = crud.get_score(db, score_id=score_id)
    if db_score is None:
        raise HTTPException(status_code=404, detail="Score not found")
    return db_score


@app.patch("/scores/{score_id}", response_model=schemas.Score)
def update_score(score_id: int, score: schemas.ScoreUpdate, db: Session = Depends(database.get_db)):
    return crud.update_score(db=db, score_id=score_id, score=score)


@app.delete("/scores/{score_id}", response_model=schemas.Score)
def delete_score(score_id: int, db: Session = Depends(database.get_db)):
    return crud.delete_score(db=db, score_id=score_id)
