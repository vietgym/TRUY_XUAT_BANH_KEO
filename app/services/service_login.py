import logging
from sqlalchemy.orm import Session

from app.schemas.schemas import User, UserBase
from app.crud import crud_login, crud_user

logger = logging.getLogger(__name__)


class LoginService:
    def __init__(self, db: Session):
        self.db = db

    async def login_user(self, user_lg: str, password: str):
        user = crud_login.login_user(db=self.db, user_lg=user_lg, password=password)
        if not user:
            return "SAITKMK"
        return user

    async def ck_register_user(self, userName: str, userEmail: str,
                               userLg: str, userPass: str,
                               re_password: str):
        if userPass != re_password:
            return {"message": "mat khau nhap lai khong giong"}
        user = UserBase
        user.userName = userName
        user.userEmail = userEmail
        user.userLg = userLg
        user.userPass = userPass
        user.role = "user"
        return user

    async def creat_user(self, user: UserBase):
        crt_user = crud_user.create_user(db=self.db, user=user)
        if not crt_user:
            return "LOi"
        return crt_user
