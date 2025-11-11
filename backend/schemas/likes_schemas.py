from pydantic import BaseModel
from typing import TYPE_CHECKING

# Forward references
if TYPE_CHECKING:
    from .user_schemas import UserRead
    from .post_schemas import PostRead


class LikeBase(BaseModel):
    user_id: int
    post_id: int


class LikeCreate(LikeBase):
    pass


class LikeRead(LikeBase):
    user: "UserRead"
    post: "PostRead"

    class Config:
        from_attributes = True