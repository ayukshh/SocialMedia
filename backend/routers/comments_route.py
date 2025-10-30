from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend import models, schemas, database
from backend.utils.token import get_current_user

router= APIRouter(prefix="/comments", tags=["Comments"])
def CreateComment(post_id: int, comments: schemas.comments_schema.CommentCreate,db: Session= Depends(get_current_user)):
    post=db.query(models.post_models.Post).filter(models.post_models.Post.id==post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="post not found")
    
    new_comment=models.comments_model.py.Comment(
        text=comments.text,
        post_id=post_id,
        user_id=get_current_user.id,
    )

    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
