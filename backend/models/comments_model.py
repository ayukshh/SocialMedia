from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from datetime import datetime, timezone
from sqlalchemy.orm import relationship
from ..database import Base

class Comments(Base):
    __tablename__="comments"
    id=Column(Integer, primary_key=True, index=True)
    user_id=Column(Integer, ForeignKey("user_id"))
    post_id=Column(Integer, ForeignKey("post_id"))
    text=Column(String)
    created_at=Column(DateTime,default=datetime.utcnow)

author=relationship("User",backref="comments")
post=relationship("Post", back_populates="comments")
