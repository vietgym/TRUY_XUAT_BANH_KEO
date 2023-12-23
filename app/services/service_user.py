import logging
from sqlalchemy.orm import Session

from app.schemas.schemas import UserBase
from app.crud import crud_user

logger = logging.getLogger(__name__)


class UserService:
    def __init__(self, db: Session):
        self.db = db

    async def creat_user(self, user: UserBase):
        crt_user = crud_user.create_user(db=self.db, user=user)
        if not crt_user:
            return {"mess": "LỖI KHÔNG TẠO ĐƯỢC USER MỚI"}
        return crt_user

    async def update_user(self, user_id: str, user_update: UserBase):
        upd_user = crud_user.update_user(db=self.db, user_id=user_id, user_update=user_update)
        if not upd_user:
            return {"mess": "LỖI KHÔNG UPDATE ĐƯỢC USER"}
        return upd_user

    async def get_product(self, user_id: str):
        user_response = crud_user.get_user(db=self.db, user_id=user_id)
        if not user_response:
            return {"mess": "LỖI KHÔNG LẤY ĐƯỢC PRODUCT"}
        return user_response
