from fastapi import FastAPI
from . import database, models
from .routers import user_auth

database.Base.metadata.create_all(bind=database.engine)
app = FastAPI()
app.include_router(user_auth.router)

