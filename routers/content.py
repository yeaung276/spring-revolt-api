from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
import repository.contentRepository as contentRepo
import schema.contentSchema as contentSch
from database import get_db

contentRouter = APIRouter(
    prefix='/contents',
    tags=['content']
)


@contentRouter.post('/create-content')
def createContent(requestBody:contentSch.Content,db:Session=Depends(get_db)):
    return contentRepo.add(db,event_id=requestBody.event_id,content_type=requestBody.content_type,
                                label=requestBody.label,content=requestBody.content)

@contentRouter.put('/update-content/{id}')
def updateContent(id:int, requestBody:contentSch.ContentEditRequest,db:Session=Depends(get_db)):
    content = contentRepo.getById(db,id)
    if not content:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='content not found.')
    content.label = requestBody.label
    content.content = requestBody.content
    db.commit()
    db.refresh(content)
    return content

@contentRouter.delete('/delete-content/{id}')
def deleteContent(id:int,db:Session=Depends(get_db)):
    content = contentRepo.getById(db,id)
    if not content:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='content not found')
    contentRepo.deleteById(db,id)
    return {'detail': 'done'}
