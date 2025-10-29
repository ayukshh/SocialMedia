from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend import database, models, schemas
from backend.utils.password_utils import get_current_user
