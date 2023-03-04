from typing import List

from sqlalchemy.orm import Session

from app.core.entities.user import User


class UserService:
    def __init__(self, db: Session):
        self.db = db

    def get_users(self) -> List[User]:
        return self.db.query(User).all()

    def create_user(self, user_data: dict) -> User:
        user = User(**user_data)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
