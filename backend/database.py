from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Prefer DATABASE_URI from environment; default to local SQLite for easy run
DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///./socialmedia.db")

# For SQLite, need check_same_thread when used in multi-threaded servers
engine_args = {}
if DATABASE_URI.startswith("sqlite"):
    engine_args["connect_args"] = {"check_same_thread": False}

engine = create_engine(DATABASE_URI, **engine_args)
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()