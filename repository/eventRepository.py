from sqlalchemy.orm import Session
from models import models

def getAll(db:Session):
    return db.query(models.Event).all()

def getById(db:Session,id:int):
    return db.query(models.Event).get(id)

def add(db:Session,title='',title_img='',location='',datetime_id=None,):
    new_event = models.Event(title=title,title_img=title_img,location=location,datetime_id=datetime_id)
    db.add(new_event)
    db.commit()
    db.refresh(new_event)
    return new_event

def deleteById(db:Session,id:int):
    event = db.query(models.Event).filter(models.Event.id==id).first()
    db.delete(event)
    db.commit()
    return 1

