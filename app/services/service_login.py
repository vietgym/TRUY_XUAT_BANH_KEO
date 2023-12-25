import logging
from sqlalchemy.orm import Session

from app.schemas.schemas import User
from app.crud import crud_login

logger = logging.getLogger(__name__)


class LoginService:
    def __init__(self, db: Session):
        self.db = db

    async def login_user(self, user_lg: str, password: str):
        user = crud_login.login_user(db=self.db, user_lg=user_lg, password=password)
        if not user:
            return "SAITKMK"
        return user
