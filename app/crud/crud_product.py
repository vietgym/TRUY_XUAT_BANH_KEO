import uuid
from sqlalchemy.orm import Session
from app.model.all import Product
from app.schemas import schemas


def creat_product(db: Session, product: schemas.ProductBase):
    proID = str(uuid.uuid4())
    db_product = Product(proID=proID, proName=product.proName,
                         manufacturerAdd=product.manufacturerAdd,
                         manufacturerName=product.manufacturerName,
                         manufacturerCont=product.manufacturerCont,
                         distributorAdd=product.distributorAdd,
                         distributorName=product.distributorName,
                         distributorCont=product.distributorCont,
                         otherDetails=product.otherDetails)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def update_product(db: Session, pro_id: str, pro_update: schemas.ProductBase):
    db_product_check = get_product(db=db, pro_id=pro_id)
    if db_product_check is None:
        return {"mess": "LỖI KHÔNG TẠO ĐƯỢC PRODUCT MỚI"}
    for field, value in pro_update.dict().items():
        setattr(db_product_check, field, value)
    db.commit()
    db.refresh(db_product_check)
    return db_product_check


def get_product(db: Session, pro_id: str):
    product_respond = db.query(Product).filter(Product.proID == pro_id).first()
    return product_respond


def get_all_product(db: Session, skip: int, limit: int):
    all_product_db = (db.query(Product)
                      .offset(skip)
                      .limit(limit)
                      .all())
    return all_product_db


def delete_product(db: Session, pro_id: str):
    db_product = db.query(Product).filter(Product.proID == pro_id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
    return db_product
