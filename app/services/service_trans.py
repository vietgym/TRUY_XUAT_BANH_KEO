import logging
from sqlalchemy.orm import Session

from app.schemas.schemas import TransBase
from app.crud import crud_trans, crud_user, crud_product

logger = logging.getLogger(__name__)


class TransService:
    def __init__(self, db: Session):
        self.db = db

    async def creat_trans(self, user_id: str, product_id: str):
        ck_user = crud_user.get_user(db=self.db, user_id=user_id)
        ck_product = crud_product.get_product(db=self.db, pro_id=product_id)
        if not ck_user or not ck_product:
            return {"mess": "LỖI ID USER HOẶC ID PRODUCT"}
        crt_trans = crud_trans.creat_trans(db=self.db,
                                           user_id=user_id,
                                           product_id=product_id)
        if not crt_trans:
            return {"mess": "LỖI KHÔNG TẠO ĐƯỢC TRANS MỚI"}
        return crt_trans

    async def get_trans(self, trans_id: str):
        trans_response = crud_trans.get_trans(db=self.db, trans_id=trans_id)
        if not trans_response:
            return {"mess": "LỖI KHÔNG GET ĐƯỢC TRANS"}
        return trans_response

    async def get_full_info_trans(self, trans_id: str):
        trans_response = crud_trans.get_full_info_trans(db=self.db, trans_id=trans_id)
        if not trans_response:
            return {"mess": "LỖI KHÔNG GET FULL INFO ĐƯỢC TRANS"}
        return trans_response

    async def get_all_trans(self, skip: int, limit: int):
        trans_response = crud_trans.get_all_trans(db=self.db, skip=skip, limit=limit)
        if not trans_response:
            return {"mess": "LỖI KHÔNG GET ALL ĐƯỢC TRANS"}
        return trans_response

    async def delete_trans(self, trans_id: str):
        trans_response = crud_trans.delete_trans(db=self.db, trans_id=trans_id)
        if not trans_response:
            return {"mess": "LỖI KHÔNG DELETE ĐƯỢC TRANS"}
        return trans_response
