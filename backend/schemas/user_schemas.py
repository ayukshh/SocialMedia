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

class config:
            orm_mode=True

class UserLogin(BaseModel):
                username: str
                password: str

class UserRead(UserCreate):
        id: int
        posts:Optional[List["PostRead"]]=[]
        likes:Optional[List["LikeRead"]]=[]
        comments: Optional[list[LikeRead]]=[] 

UserRead.update_forward_refs()
PostRead.update_forward_refs()
LikeRead.update_forward_refs()