from fastapi import APIRouter,Depends,status,HTTPException
from sqlalchemy.orm import Session
import repository.personRepository as personRepo
import schema.personSchema as personSch
from database import get_db

personRouter = APIRouter(
    prefix='/persons',
    tags=['person']
)

@personRouter.get('')
def getAll(db:Session=Depends(get_db)):
    return personRepo.getAll(db)

@personRouter.get('/{id}')
def getById(id,db:Session=Depends(get_db)):
    return personRepo.getById(db,id)

@personRouter.post('/create-person',status_code=status.HTTP_201_CREATED)
def createPerson(requestBody:personSch.PersonRequest,db:Session=Depends(get_db)):
    return personRepo.add(db,**requestBody.dict())

@personRouter.put('/update-person/{id}',status_code=status.HTTP_202_ACCEPTED)
def updatePerson(id:int,requestBody:personSch.PersonRequest,db:Session=Depends(get_db)):
    person = personRepo.getById(db,id)
    if not person:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='data not found')
    personRepo.updateById(db,id,requestBody.dict())
    db.refresh(person)
    return person

@personRouter.put('/update-person-content/{id}',status_code=status.HTTP_202_ACCEPTED)
def updatePersonConent(id:int,requestBody:personSch.ContentUpdateRequest,db:Session=Depends(get_db)):
    person = personRepo.getById(db,id)
    if not person:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='data not found')
    person.content = requestBody.content
    db.commit()
    return {'detail': 'done'}

@personRouter.delete('/delete-person/{id}')
def deletePerson(id:int,db:Session=Depends(get_db)):
    if not personRepo.getById(db,id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='data not found')
    personRepo.deleteById(db,id)
    return {'detail': 'done'}