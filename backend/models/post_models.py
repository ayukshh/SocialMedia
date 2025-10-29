from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from datetime import datetime, timezone
from sqlalchemy.orm import relationship
from ..database import Base

class Post(Base):
    __tablename__="Post"
    id=Column(Integer, primary_key=True, index=True)
    user_id=Column(Integer, ForeignKey("user_id"))
    content=Column(String) #text of the post
    created_at=Column(DateTime, default=datetime.utcnow)

author=relationship("User", backref="post")
likes=relationship("Likes", back_populates="post")
comments=relationship("Comments", back_populates="post")

