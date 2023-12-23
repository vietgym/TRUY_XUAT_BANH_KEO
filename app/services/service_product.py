import logging
from sqlalchemy.orm import Session

from app.schemas.schemas import ProductBase
from app.crud import crud_product

logger = logging.getLogger(__name__)


class ProductService:
    def __init__(self, db: Session):
        self.db = db

    async def creat_product(self, product: ProductBase):
        crt_product = crud_product.creat_product(db=self.db, product=product)
        if not crt_product:
            return {"mess": "LỖI KHÔNG TẠO ĐƯỢC PRODUCT MỚI"}
        return crt_product

    async def update_product(self, pro_id: str, pro_update: ProductBase):
        upd_product = crud_product.update_product(db=self.db, pro_id=pro_id, pro_update=pro_update)
        if not upd_product:
            return {"mess": "LỖI KHÔNG UPDATE ĐƯỢC PRODUCT"}
        return upd_product

    async def get_product(self, pro_id: str):
        product_response = crud_product.get_product(db=self.db, pro_id=pro_id)
        if not product_response:
            return {"mess": "LỖI KHÔNG LẤY ĐƯỢC PRODUCT"}
        return product_response

    async def get_all_product(self, skip: int, limit: int):
        product_response = crud_product.get_all_product(db=self.db,
                                                        skip=skip,
                                                        limit=limit)
        if not product_response:
            return {"mess": "LỖI KHÔNG LẤY ĐƯỢC ALL PRODUCT"}
        return product_response

    async def delete_product_by_id(self, pro_id: str):
        product_response = crud_product.delete_product(db=self.db, pro_id=pro_id)
        if not product_response:
            return {"mess": "LỖI KHÔNG XOÁ ĐƯỢC PRODUCT"}
        return product_response
