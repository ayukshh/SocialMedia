from fastapi import FastAPI
from . import models, database
from .routers import auth

database.Base.metadata.create_all(bind=database.engine)
app = FastAPI()
app.include_router(auth.router)

