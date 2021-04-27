from sqlalchemy.orm import Session
from models import models

def getAll(db:Session):
    return db.query(models.Location).all()

def getById(db:Session, id:int):
    return db.query(models.Location).get(id)

def add(db:Session,address:str='',region:str='',cover_img:str='',name=''):
    new_location = models.Location(address=address,name=name,region=region,cover_img=cover_img,content='')
    db.add(new_location)
    db.commit()
    db.refresh(new_location)
    return new_location

def deleteById(db:Session, id:int):
    db.query(models.Location).filter(models.Location.id==id).delete(synchronize_session=False)
    db.commit()
    return 1