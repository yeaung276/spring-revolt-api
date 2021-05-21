from fastapi import APIRouter,Depends,status, HTTPException
from typing import List
import datetime
from sqlalchemy.orm import Session
import repository.timelineRepository as timelineRepo
import schema.timelineSchema as timelineSch
import schema.eventSchema as eventSch
from routers.events import createEvent
from database import get_db

timelineRouter = APIRouter(
    prefix='/timelines',
    tags=['timelines']
)


@timelineRouter.get('')
def getTimelines(db:Session = Depends(get_db)):
    return timelineRepo.getAll(db)

@timelineRouter.get('/{id}')
def getTimeline(id:int,db:Session=Depends(get_db)):
    timeline = timelineRepo.getById(db,id)
    if not timeline:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Timeline not found.")
    return timeline

@timelineRouter.post('/create-timeline',status_code=status.HTTP_201_CREATED)
def createTimeline(requestBody: timelineSch.Timeline,db:Session=Depends(get_db)):
    if(requestBody.create_event):
        event = eventSch.EventRequestBody(title=requestBody.title,title_img='',location='',datetime=requestBody.datetime)
        event_id = createEvent(event,db)["id"]
    else:
        event_id = None
    return timelineRepo.add(db,datetime=requestBody.datetime,title=requestBody.title,
                            timeline_type=requestBody.timeline_type,event_id=event_id)

@timelineRouter.put('/edit-timeline/{id}',status_code=status.HTTP_202_ACCEPTED)
def editTimeline(id:int,requestBody:timelineSch.Timeline,db:Session=Depends(get_db)):
    timeline = timelineRepo.getById(db,id)
    if not timeline:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Timeline not found')
    timeline.title = requestBody.title
    timeline.datetime = requestBody.datetime
    timeline.timeline_type = requestBody.timeline_type
    timeline.event_id = requestBody.event_id
    db.commit()
    db.refresh(timeline)
    return timeline

@timelineRouter.delete('/delete-timeline/{id}')
def deleteTimeline(id:int,db:Session=Depends(get_db)):
    timeline = timelineRepo.getById(db,id)
    if not timeline:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Timeline not found')
    timelineRepo.deleteById(db,id)
    return {'detail': 'done'}
