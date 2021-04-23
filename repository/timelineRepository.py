from sqlalchemy.orm import Session
from models import models

def getAll(db:Session):
    return db.query(models.Timeline).all()

def getById(db:Session,id:int):
    return db.query(models.Timeline).get(id)

def add(db:Session,datetime='',title='',timeline_type=0,event_id=None):
    new_timeline = models.Timeline(datetime=datetime,title=title,timeline_type=timeline_type,event_id=event_id)
    db.add(new_timeline)
    db.commit()
    db.refresh(new_timeline)
    return new_timeline

def deleteById(db:Session,id:int):
    db.query(models.Timeline).filter(models.Timeline.id==id).delete(synchronize_session=False)
    db.commit()
    return 1