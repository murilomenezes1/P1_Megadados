from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)


app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/discipline/", response_model=schemas.Discipline)
def create_discipline(discipline: schemas.DisciplineCreate, db: Session = Depends(get_db)):
    db_discipline = crud.get_discipline(db, name=discipline.discipline)
    if db_discipline:
        raise HTTPException(status_code=400, detail="discipline already registered")
    return crud.create_discipline(db=db, data=discipline)

@app.post("/discipline/notes", response_model=schemas.Note)
def create_note(discipline: str, note: str, db: Session = Depends(get_db)):

    return crud.add_note(db,discipline,note)


@app.get("/discipline/", response_model=List[schemas.Discipline])
def get_disciplines(db: Session = Depends(get_db)):

    return crud.get_all_disciplines(db)

@app.get("/notes/", response_model=List[schemas.Note])
def get_notes(discipline: str, db: Session = Depends(get_db)):

    return crud.get_discipline_notes(db, discipline)


@app.delete("/discipline/")
def delete_discipline(discipline: str,db: Session = Depends(get_db)):

    db_discipline = crud.get_discipline(db, name=discipline)
    if not db_discipline:
        raise HTTPException(status_code=400, detail="Discipline not registered")
    return crud.delete_discipline(db,name=discipline)

@app.delete('/discipline/note')
def delete_note(note_id:int, db: Session = Depends(get_db)):

    return crud.delete_note(db,note_id)


@app.put('/discipline/', response_model=schemas.Discipline)
async def update_discipline(data: schemas.DisciplineUpdate, discipline: str, db: Session = Depends(get_db)):
    
    return crud.update_discipline(db,name = discipline,data = data)

@app.patch('/note/', response_model=schemas.Note)
def update_note(data: schemas.NoteUpdate, note_id: int, db: Session = Depends(get_db)):

    return crud.update_note(db, id=note_id, data=data)

