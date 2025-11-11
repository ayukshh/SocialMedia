from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend import models, database
from backend.utils.token import get_current_user

router = APIRouter(prefix="/likes", tags=["likes"])


@router.post("/{post_id}", status_code=status.HTTP_201_CREATED)
def like_post(
    post_id: int,
    db: Session = Depends(database.SessionLocal),
    current_user=Depends(get_current_user),
):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="post not found")

    existing_like = (
        db.query(models.Like)
        .filter(models.Like.post_id == post_id, models.Like.user_id == current_user.id)
        .first()
    )
    if existing_like:
        raise HTTPException(status_code=400, detail="post already liked")

    like = models.Like(post_id=post_id, user_id=current_user.id)
    db.add(like)
    db.commit()
    return {"message": "post liked"}


@router.delete("/{post_id}", status_code=status.HTTP_200_OK)
def unlike_post(
    post_id: int,
    db: Session = Depends(database.SessionLocal),
    current_user=Depends(get_current_user),
):
    like = (
        db.query(models.Like)
        .filter(models.Like.post_id == post_id, models.Like.user_id == current_user.id)
        .first()
    )
    if not like:
        raise HTTPException(status_code=400, detail="you have not liked the post")
    db.delete(like)
    db.commit()
    return {"message": "post unliked"}