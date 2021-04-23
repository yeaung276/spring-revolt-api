from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from models import models

class Timeline(BaseModel):
    title: str
    datetime: datetime
    timeline_type: int
    create_event: bool
    event_id: Optional[int]
    
def toTimelineModel(timeline:Timeline):
    return {
        'title': timeline.title,
        'datetime': timeline.datetime,
        'timeline_type': timeline.timeline_type,
        'event_id': timeline.event_id
    }