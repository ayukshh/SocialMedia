from pydantic import BaseModel

# Forward references
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .user_schemas import UserRead
    from .post_schemas import PostRead

    class LikeBase(BaseModel):
        user_id:int
        post_id:int

class LikeCreate(LikeBase):
    pass 

class LikeRead(LikeBase):
    user:"UserRead"
    post:"PostRead" 

    class config:
        orm_mode=True

UserRead.update_forward_refs()
PostRead.update_forward_refs()
LikeRead.update_forward_refs()