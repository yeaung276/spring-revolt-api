from sqlalchemy.orm import Session
from models import models

def getAll(db:Session):
    return db.query(models.Person).all()

def getById(db:Session,id:int):
    return db.query(models.Person).get(id)

def add(db:Session,name='',age=0,photo='',desc='',org=''):
    new_person = models.Person(name=name,age=age,photo=photo,content='',desc=desc,org=org) 
    db.add(new_person)
    db.commit()
    db.refresh(new_person)
    return new_person

def updateById(db:Session,id,updateFields:dict):
    db.query(models.Person).filter(models.Person.id==id).update(updateFields)
    db.commit()
    return 1

def deleteById(db:Session,id:int):
    db.query(models.Person).filter(models.Person.id==id).delete(synchronize_session=False)
    db.commit()
    return 1