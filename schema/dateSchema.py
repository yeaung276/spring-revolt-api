from pydantic import BaseModel
from datetime import datetime
from typing import List

class Event(BaseModel):
    id:int
    class Config():
        orm_mode=True

class DateResponse(BaseModel):
    id:int
    datetime: datetime
    event: List[Event]
    class Config():
        orm_mode=True

class Date(BaseModel):
    datetime: datetime
    class Config():
        orm_mode=True

class EventDetail(Event):
    title:str
    location:str
    title_img:str
    datetime: Date


class EventsByDateResponse(BaseModel):
    id:int
    datetime: datetime
    event: List[EventDetail]
    class Config():
        orm_mode = True

