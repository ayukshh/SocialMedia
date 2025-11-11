from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import database
from .routers import user_auth, user, post_route, likes_route, comments_route

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
app.include_router(user.router)
app.include_router(post_route.router)
app.include_router(likes_route.router)
app.include_router(comments_route.router)

