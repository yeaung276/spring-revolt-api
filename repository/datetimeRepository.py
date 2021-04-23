from sqlalchemy.orm import Session
from datetime import datetime
from models import models

def getByDatetime(db:Session,datetime:datetime):
    return db.query(models.Date).filter(models.Date.datetime==datetime).first()

def add(db:Session,datetime:datetime):
    new_date = models.Date(datetime=datetime)
    db.add(new_date)
    db.commit()
    db.refresh(new_date)
    return new_date