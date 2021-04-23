from fastapi import APIRouter,Depends,status,HTTPException
from sqlalchemy.orm import Session
from database import get_db
import schema.tagSchema as tagSch
import repository.tagRepository as tagRepo
import repository.tagMapperRepository as tagMapperRepo


tagRouter = APIRouter(
    prefix='/tags',
    tags=['tags']
)

@tagRouter.get('')
def getTags(db:Session = Depends(get_db)):
    return tagRepo.getAll(db)

@tagRouter.post('/create-tag',status_code=status.HTTP_201_CREATED)
def createTag(name:str,db:Session=Depends(get_db)):
    return tagRepo.add(db,name)

@tagRouter.delete('/delete-tag/{id}')
def deleteTag(id:int,db:Session=Depends(get_db)):
    tag = tagRepo.getById(db,id)
    if not tag:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Tag not found')
    tagMapperRepo.deleteByTagId(db,id)
    tagRepo.deleteById(db,id)
    return {'detail': 'done'}

@tagRouter.post('/tag-event',status_code=status.HTTP_201_CREATED)
def tagEvent(requestBody:tagSch.tagEvent,db:Session=Depends(get_db)):
    mapper = tagMapperRepo.findByEventIdandTagId(db,requestBody.event_id,requestBody.tag_id)
    if not mapper.first():
        tagMapperRepo.add(db,requestBody.event_id,requestBody.tag_id)
    return {'detail': 'done'}

@tagRouter.delete('/untag-event/{id}')
def untagEvent(id:int,db:Session=Depends(get_db)):
    if not tagMapperRepo.getById(db,id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Tag not found')
    tagMapperRepo.deleteById(db,id)
    return {'detail': 'done'}