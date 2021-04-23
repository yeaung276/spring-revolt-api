from pydantic import BaseModel
from sqlalchemy.orm import Session
from models import models


def getById(db:Session,id:int):
    return db.query(models.Content).get(id)

def add(db:Session,event_id=None,content_type=0,label='',content=''):
    new_content = models.Content(event_id=event_id,content_type=content_type,label=label,content=content)
    db.add(new_content)
    db.commit()
    db.refresh(new_content)
    return new_content

def deleteById(db:Session,id:int):
    db.query(models.Content).filter(models.Content.id==id).delete(synchronize_session=False)
    db.commit()
    return 1