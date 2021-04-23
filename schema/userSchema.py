from pydantic import BaseModel
from models import models

class User(BaseModel):
    username: str
    email: str
    password: str

class userGeneral(BaseModel):
    username: str
    email: str

    class Config():
        orm_mode = True

def toUserModel(user:User):
    return {
        'username': user.username,
        'email': user.email
    }


