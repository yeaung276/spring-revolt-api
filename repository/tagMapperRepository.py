from sqlalchemy.orm import Session
from models import models

def findByEventIdandTagId(db:Session,eventId:int,tagId:int):
    return db.query(models.TagMapper).filter(models.TagMapper.tag_id==tagId).filter(models.TagMapper.event_id==eventId)

def getById(db:Session,id:int):
    return db.query(models.TagMapper).get(id)

def add(db:Session,eventId:int,tagId:int):
    new_mapper = models.TagMapper(event_id=eventId,tag_id=tagId)
    db.add(new_mapper)
    db.commit()
    db.refresh(new_mapper)
    return new_mapper

def deleteById(db:Session,id:int):
    db.query(models.TagMapper).filter(models.TagMapper.id==id).delete(synchronize_session=False)
    db.commit()
    return 1

def deleteByTagId(db:Session,tagId:int):
    db.query(models.TagMapper).filter(models.TagMapper.tag_id==tagId).delete(synchronize_session=False)
    db.commit()
    return 1