from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend import database, models, schemas
from backend.utils.token import get_current_user

router=APIRouter(prefix="/posts", tags=["Posts"])

@router.post("/", response_model=list[schemas.posts.PostOut])
def create_post(post: schemas.post.PostCreate, db: Session=Depends(database.get_db), current_user: int=Depends(get_current_user)):
    new_post=models.post_models.Post(owner_id=current_user.id, **post.dict())

    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post 




