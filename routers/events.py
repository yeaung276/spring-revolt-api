from typing import List
from fastapi import APIRouter,Depends,status,HTTPException
import repository.eventRepository as eventRepo
import repository.datetimeRepository as datetimeRepo
import repository.contentRepository as contentRepo
from sqlalchemy.orm import Session
from database import get_db
import schema.eventSchema as eventSch


eventRouter = APIRouter(
    prefix='/events',
    tags=['event']
)

@eventRouter.get('/{id}',response_model=eventSch.eventDetail)
def getEvent(id:int,db:Session=Depends(get_db)):
    event = eventRepo.getById(db,id)
    if not event:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Event not found')
    return  event

@eventRouter.post('/create-event',status_code=status.HTTP_201_CREATED)
def createEvent(requestBody:eventSch.EventRequestBody,db:Session=Depends(get_db)):
    # check if there is a date for the event
    date = datetimeRepo.getByDatetime(db,requestBody.datetime)
    # create one if not
    if not date:
        date = datetimeRepo.add(db,datetime=requestBody.datetime)

    # create the event
    new_event = eventRepo.add(db,title=requestBody.title,title_img=requestBody.title_img,
                                location=requestBody.location,datetime_id=date.id)
    # add default content
    contentRepo.add(db,event_id=new_event.id)

    return {"id": new_event.id}

@eventRouter.put('/update-event/{id}',status_code=status.HTTP_202_ACCEPTED)
def updateEvent(id:int,requestBody:eventSch.EventRequestBody,db:Session=Depends(get_db)):
    # check if there is a date for the event
    date = datetimeRepo.getByDatetime(db,requestBody.datetime)
    # create on if not
    if not date:
        date = datetimeRepo.add(db,datetime=requestBody.datetime)
    event = eventRepo.getById(db,id)
    if not event:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Event not found')
    event.datetime_id = date.id
    event.title = requestBody.title
    event.title_img = requestBody.title_img
    event.location = requestBody.location
    db.commit()
    db.refresh(event)
    return event

@eventRouter.delete('/delete-event/{id}')
def deleteEvent(id:int,db:Session=Depends(get_db)):
    event = eventRepo.getById(db,id)
    if not event:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='event not found')
    eventRepo.deleteById(db,id)
    return {'detail': 'done'}

@eventRouter.get('/getTags/{id}',response_model=eventSch.eventTags)
def getTagsByEvent(id:int,db:Session=Depends(get_db)):
    event = eventRepo.getById(db,id)
    if not event:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Event not found')
    return  event
