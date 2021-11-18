from sqlalchemy.orm import Session



from . import models, schemas




def get_all_disciplines(db: Session):

    return db.query(models.Disciplines).all()



def get_discipline(db: Session, name: str):

    return db.query(models.Disciplines).filter(models.Disciplines.discipline == name).first()

def get_discipline_notes(db: Session, name: str):

    db_discipline = db.query(models.Disciplines).filter(models.Disciplines.discipline == name).first()

    return db.query(models.Notes).filter(models.Notes.discipline_id == db_discipline.id).all()

def create_discipline(db: Session, data: schemas.DisciplineCreate):

    db_discipline = models.Disciplines(discipline=data.discipline, professor=data.professor)
    db.add(db_discipline)
    db.commit()
    db.refresh(db_discipline)
    return db_discipline

def delete_discipline(db: Session, name: str):

    db.query(models.Disciplines).filter(models.Disciplines.discipline == name).delete()

    db.commit()


    return True

def add_note(db: Session, name: str, note: str):

    db_discipline = db.query(models.Disciplines).filter(models.Disciplines.discipline == name).first()

    db_note = models.Notes(note=note, discipline_id=db_discipline.id)

    db.add(db_note)
    db.commit()
    db.refresh(db_note)

    return db_note



def delete_note(db: Session, note_id: int):

    to_delete = db.query(models.Notes).filter(models.Notes.id == note_id).first()

    db.delete(to_delete)
    db.commit()

    return True



def update_discipline(db: Session,name: str, data: schemas.DisciplineUpdate):

    db_discipline = db.query(models.Disciplines).filter(models.Disciplines.discipline == name).first()

    db_discipline.discipline = data.discipline
    db_discipline.professor = data.professor

    db.commit()
    db.refresh(db_discipline)

    return db_discipline

def update_note(db: Session, id: int, data: schemas.NoteUpdate):

    db_note = db.query(models.Notes).filter(models.Notes.id == id).first()

    db_note.note = data.note

    db.commit()
    db.refresh(db_note)

    return db_note






    




