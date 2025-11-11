from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend import database, models
from backend.schemas import post_schemas
from backend.utils.token import get_current_user, get_optional_user
from typing import List

router = APIRouter(prefix="/posts", tags=["Posts"])

@router.get("/", response_model=List[dict])
def list_posts(
    db: Session = Depends(database.SessionLocal),
    current_user=Depends(get_optional_user),
):
    posts = db.query(models.Post).order_by(models.Post.created_at.desc()).all()
    feed = []
    for p in posts:
        likes_count = db.query(models.Like).filter(models.Like.post_id == p.id).count()
        liked_by_user = False
        if current_user:
            liked_by_user = (
                db.query(models.Like)
                .filter(models.Like.post_id == p.id, models.Like.user_id == current_user.id)
                .first()
                is not None
            )
        comments = (
            db.query(models.Comment)
            .filter(models.Comment.post_id == p.id)
            .order_by(models.Comment.created_at.asc())
            .all()
        )
        feed.append({
            "id": p.id,
            "content": p.content,
            "owner_name": p.author.username if p.author else None,
            "likes_count": likes_count,
            "liked_by_user": liked_by_user,
            "comments": [
                {
                    "id": c.id,
                    "text": c.text,
                    "user_name": c.author.username if c.author else None,
                }
                for c in comments
            ],
            "created_at": p.created_at.isoformat() if p.created_at else None,
        })
    return feed


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
