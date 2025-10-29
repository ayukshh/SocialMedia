from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend import models, database, schemas

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/", response_model=list[schemas.user.UserOut])
def get_users(db: Session = Depends(database.get_db)):
    return db.query(models.user.User).all()

@router.get("/{user_id}", response_model=schemas.user.UserOut)
def get_user(user_id:int, db: Session=Depends(database.get_db)):
    user = db.query(models.user.User).filter(models.user.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User Not Found")
    return user
