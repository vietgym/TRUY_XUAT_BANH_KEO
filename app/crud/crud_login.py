import uuid
from sqlalchemy.orm import Session
from app.model.all import User
from app.schemas import schemas


def login_user(db: Session, user_lg: str, password: str):
    user = (db.query(User)
            .filter(User.userLg == user_lg, User.userPass == password)
            .first())
    return user
