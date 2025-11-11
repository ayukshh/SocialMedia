from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend import database, models
from backend.schemas import post_schemas
from backend.utils.token import get_current_user

router = APIRouter(prefix="/posts", tags=["Posts"])


@router.post("/", response_model=post_schemas.PostRead, status_code=status.HTTP_201_CREATED)
def create_post(
    post: post_schemas.PostCreate,
    db: Session = Depends(database.SessionLocal),
    current_user=Depends(get_current_user),
):
    if post.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Cannot create post for another user")

    new_post = models.Post(user_id=current_user.id, content=post.content)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post
