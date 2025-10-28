from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URI="postgresql://ayu:123456@localhost:5432/socialmedia_db"
engine=create_engine(DATABASE_URI)
SessionLocal=sessionmaker(autoflush=False,autocommit=False, bind=engine)

Base=declarative_base()