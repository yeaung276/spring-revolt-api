from pydantic import BaseModel

class ContentEditRequest(BaseModel):
    label: str
    content: str

class Content(ContentEditRequest):
    event_id: int
    content_type: int
    class Config():
        orm_mode = True