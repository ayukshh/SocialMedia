from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# PostgreSQL URI: postgresql://USER:PASSWORD@HOST:PORT/DBNAME
DATABASE_URI = os.getenv(
    "DATABASE_URI",
    "postgresql://ayu:123456@localhost:5432/socialmedia_db",  # default database name
)

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URI)

# Create a configured "Session" class
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

# Base class for ORM models
Base = declarative_base()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
