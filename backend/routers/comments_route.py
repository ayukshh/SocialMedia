from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend import models, database
from backend.schemas import comments_schema
from backend.utils.token import get_current_user

router = APIRouter(prefix="/comments", tags=["Comments"])


@router.post("/{post_id}", status_code=status.HTTP_201_CREATED)
def create_comment(
    post_id: int,
    comment: comments_schema.CommentCreate,
    db: Session = Depends(database.SessionLocal),
    current_user=Depends(get_current_user),
):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="post not found")

    new_comment = models.Comment(
        text=comment.text,
        post_id=post_id,
        user_id=current_user.id,
    )

    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return {"message": "comment created", "id": new_comment.id}
