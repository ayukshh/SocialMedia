from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import database
from .routers import user_auth

# Create tables
database.Base.metadata.create_all(bind=database.engine)

# Initialize FastAPI app
app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_auth.router)

