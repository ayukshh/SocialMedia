from pydantic import BaseModel, EmailStr
from typing import List, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .post_schemas import PostRead
    from .likes_schemas import LikeRead

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    password: str

    class Config:
        orm_mode = True  
    username: str
    password: str

class UserRead(UserCreate):
    id: int
    posts: Optional[List["PostRead"]] = []  # Using forward reference
    likes: Optional[List["LikeRead"]] = []  # Using forward reference
    comments: Optional[List["LikeRead"]] = []  # Using forward reference

# Explicitly set forward references manually for Pydantic v2
UserRead.update_forward_refs()
UserRead.__annotations__["posts"] = Optional[List["PostRead"]]
UserRead.__annotations__["likes"] = Optional[List["LikeRead"]]
UserRead.__annotations__["comments"] = Optional[List["LikeRead"]]


PostRead.update_forward_refs()
LikeRead.update_forward_refs()
