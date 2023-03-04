from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.core.services.user import UserService

router = APIRouter()


@router.get("/users")
async def get_users(db: Session = Depends(get_db)):
    users = UserService(db).get_users()
    return users


@router.post("/users")
async def create_user(user_data: dict, db: Session = Depends(get_db)):
    user = UserService(db).create_user(user_data)
    return user
