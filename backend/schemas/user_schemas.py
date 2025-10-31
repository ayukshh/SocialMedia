from pydantic import BaseModel, EmailStr
from typing import List, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .post_schemas import PostRead
    from .likes_schemas import LikeRead

class UserBase(BaseModel):
    username: str

    class Config:
        from_attributes = True  # New name for orm_mode in Pydantic v2

class UserLogin(UserBase):
    password: str

class UserCreate(UserBase):
    email: EmailStr
    password: str

class UserOut(UserBase):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True

class UserRead(UserBase):
    id: int
    email: EmailStr
    posts: Optional[List["PostRead"]] = []
    likes: Optional[List["LikeRead"]] = []
    comments: Optional[List["LikeRead"]] = []

    class Config:
        from_attributes = True
