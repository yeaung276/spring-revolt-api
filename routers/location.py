from fastapi import APIRouter,Depends,status,HTTPException
from typing import List
from sqlalchemy.orm import Session
from database import get_db
import repository.locationRepository as locationRepo
import schema.locationSchema as locSch

locationRouter = APIRouter(
    prefix='/locations',
    tags=['location']
)

@locationRouter.get('',response_model=List[locSch.LocationGeneralResponse])
def getAllLocations(db:Session=Depends(get_db)):
    return locationRepo.getAll(db)

@locationRouter.get('/{id}')
def getLocationById(id:int, db:Session=Depends(get_db)):
    return locationRepo.getById(db,id)

@locationRouter.post('/create-location',status_code=status.HTTP_201_CREATED)
def createLocation(requestBody:locSch.LocationRequest,db:Session=Depends(get_db)):
    return locationRepo.add(db,**requestBody.dict())

@locationRouter.put('/update-location/{id}',status_code=status.HTTP_202_ACCEPTED)
def updateLocation(id:int,requestBody:locSch.LocationRequest,db:Session=Depends(get_db)):
    location = locationRepo.getById(db,id)
    if not location:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='data not found')
    location.address = requestBody.address
    location.region = requestBody.region
    location.name = requestBody.name
    location.cover_img = requestBody.cover_img
    db.commit()
    db.refresh(location)
    return location

@locationRouter.put('/update-location-content/{id}',status_code=status.HTTP_202_ACCEPTED)
def updateContent(id:int,requestBody:locSch.ContentUpdateRequest,db:Session=Depends(get_db)):
    location = locationRepo.getById(db,id)
    if not location:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='data not found')
    location.content = requestBody.content
    db.commit()
    db.refresh(location)
    return {'detail': 'done'}

@locationRouter.delete('/delete-location/{id}')
def deleteContent(id:int,db:Session=Depends(get_db)):
    if not locationRepo.getById(db,id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='data not found')
    locationRepo.deleteById(db,id)
    return {'detail': 'done'}