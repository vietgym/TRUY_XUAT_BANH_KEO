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

    async def get_all_user(self, skip: int, limit: int):
        user_response = crud_user.get_all_user(db=self.db,
                                               skip=skip,
                                               limit=limit)
        if not user_response:
            return {"mess": "LỖI KHÔNG LẤY ĐƯỢC ALL USER"}
        return user_response

    async def delete_user_by_id(self, user_id: str):
        user_response = crud_user.delete_user(db=self.db, user_id=user_id)
        if not user_response:
            return {"mess": "LỖI KHÔNG XOÁ ĐƯỢC USER"}
        return user_response
