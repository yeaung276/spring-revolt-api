from sqlalchemy.orm import Session
from models import models

def getAll(db:Session):
    return db.query(models.Date).all()

def getById(db:Session,id:int):
    return db.query(models.Date).get(id)