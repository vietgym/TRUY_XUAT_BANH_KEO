from fastapi import Request
from sqlalchemy.orm import Session


def get_session(request: Request):
    return request.session


def set_current_user(session: Session, user_id: str):
    session["current_user_id"] = user_id
