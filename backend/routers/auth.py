from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from datetime import datetime, timedelta
from backend import models, utils, database
from backend.schemas import schemas 



router=APIRouter(
    prefix="/auth", 
    tags=["authentication"]
)

SECRET_KEY="justme123"
ALGORITHM= "HS256"
ACESS_TOKEN_EXPIRE_MINUTES= 45

#function to create JWT
def create_acess_tokens(data: dict):
    to_encode=data.copy()
    expire=datetime.utcnow()+timedelta(minutes=ACESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

@router.post("/register", response_model=schemas.UserOut) 
def register(user: schemas.UserCreate, db: Session=Depends(database.SessionLocal)):
    existing_user = db.query(models.Users).filter(models.Users.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="username already taken, try another one")
    
    hashed_pw=utils.hash_password(user.password)
    new_user=models.Users(username=user.username, email=user.email, password=hashed_pw)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/login")
def login(user: schemas.UserLogin, db: Session=Depends(database.SessionLocal)):
    db_user=db.query(models.Users).filter(models.Users.username==user.username).first()
    if not db_user or not utils.verify_password(user.password, db_user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="invalid credentials")
    
    tokens=create_acess_tokens(data={"sub":db_user.username})
    return{"acess_token": tokens, "token_type": "bearer"}


