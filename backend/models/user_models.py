from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..database import Base

class Users (Base):
    __tablename__ ="Users"
    id=Column(Integer, primary_key=True, index=True)
    username=Column(String, unique=True, index=True)
    email=Column(String, unique=True, index=True)
    password=Column(String)

post=relationship("Post", back_populates="author")
comments=relationship("Comments", back_populates="comments")
likes=relationship("Likes", back_populates="likes")