from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

# Forward references
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .user_schemas import UserRead
    from .likes_schemas import LikeRead


class PostBase(BaseModel):
    content: str

    class Config:
        from_attributes = True


class PostCreate(PostBase):
    user_id: int


class PostRead(PostBase):
    id: int
    user_id: int
    created_at: datetime
    author: Optional["UserRead"] = None
    likes: Optional[List["LikeRead"]] = []

    class Config:
        from_attributes = True
