from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend import models, database
from backend.schemas import user_schemas

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=list[user_schemas.UserOut])
def get_users(db: Session = Depends(database.SessionLocal)):
    return db.query(models.User).all()


@router.get("/{user_id}", response_model=user_schemas.UserOut)
def get_user(user_id: int, db: Session = Depends(database.SessionLocal)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User Not Found")
    return user
