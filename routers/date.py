from fastapi import APIRouter,Depends,HTTPException,status
from typing import List
from sqlalchemy.orm import Session
import repository.dateRepository as dateRepo
from models import models
from database import get_db
import schema.dateSchema as dateSch

dateRouter = APIRouter(
    prefix='/date',
    tags=['date']
)

@dateRouter.get('',response_model=List[dateSch.DateResponse])
def getDates(db:Session=Depends(get_db)):
    return dateRepo.getAll(db)

@dateRouter.get('/{id}',response_model=dateSch.EventsByDateResponse)
def getEventsByDate(id:int,db:Session=Depends(get_db)):
    events = dateRepo.getById(db,id)
    if not events:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='not found')
    return events