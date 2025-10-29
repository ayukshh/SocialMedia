from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from datetime import datetime, timezone
from sqlalchemy.orm import relationship

from ..database import Base

class Likes(Base):
    __tablename__="likes"
    user_id=Column(Integer, ForeignKey("user_id"), primary_key=True)
    post_id=Column(Integer, ForeignKey("post_id"), primary_key=True)

user=relationship("User", backref="likes")
post=relationship("Post", back_populates="likes")

