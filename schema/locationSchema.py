from pydantic import BaseModel

class LocationRequest(BaseModel):
    address: str = ''
    region: str = ''
    name:str = ''
    cover_img: str

class LocationGeneralResponse(BaseModel):
    id:int
    address: str
    region: str
    cover_img: str
    name:str
    class Config():
        orm_mode = True

class ContentUpdateRequest(BaseModel):
    content: str

