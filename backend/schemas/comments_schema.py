from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CommentCreate(BaseModel):
    user_id: int        
    post_id: int        
    text: str 

class CommentRead(BaseModel):
    id: int
    user_id: int
    post_id: int
    text: str
    created_at: datetime

class Config:
        orm_mode = True