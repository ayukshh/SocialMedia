from pydantic import BaseModel
from datetime import datetime


class CommentCreate(BaseModel):
    text: str


class CommentRead(BaseModel):
    id: int
    user_id: int
    post_id: int
    text: str
    created_at: datetime

    class Config:
        from_attributes = True