from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models import models

def getAll(db:Session):
    return db.query(models.Tag).all()

def getById(db:Session,id:int):
    return db.query(models.Tag).get(id)

def add(db:Session,tagName:str=''):
    new_tag = models.Tag(name=tagName)
    db.add(new_tag)
    db.commit()
    db.refresh(new_tag)
    return new_tag

def deleteById(db:Session,id:int):
    db.query(models.Tag).filter(models.Tag.id==id).delete(synchronize_session=False)
    db.commit()
    return 1