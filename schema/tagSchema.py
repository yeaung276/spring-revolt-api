from pydantic import BaseModel

class tagEvent(BaseModel):
    event_id: int
    tag_id: int