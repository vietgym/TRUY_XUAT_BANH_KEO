import uuid
from sqlalchemy.orm import Session
from datetime import datetime
import hashlib
import json

from app.model.all import Product, User, Trans
from app.schemas import schemas
from app.crud import crud_product, crud_user


def hash_string(input_string, algorithm='sha256'):
    hash_algorithm = hashlib.new(algorithm)
    hash_algorithm.update(input_string.encode('utf-8'))
    hashed_string = hash_algorithm.hexdigest()
    return hashed_string


def creat_trans(db: Session, user_id: str, product_id: str):
    crt_trans = schemas.TransBase

    crt_trans.transTime = (datetime.now()).strftime("%Y-%m-%d %H:%M:%S")

    str_hash = user_id + product_id + crt_trans.transTime
    crt_trans.transHash = hash_string(str_hash)

    id_trans = str(uuid.uuid4())
    db_trans = Trans(transID=id_trans,
                     transTime=crt_trans.transTime,
                     transHash=crt_trans.transHash,
                     userID=user_id,
                     productID=product_id)

    db.add(db_trans)
    db.commit()
    db.refresh(db_trans)
    return db_trans


def get_trans(db: Session, trans_id: str):
    trans = db.query(Trans).filter(Trans.transID == trans_id).first()
    return trans


def get_full_info_trans(db: Session, trans_id: str):
    trans = db.query(Trans).filter(Trans.transID == trans_id).first()
    user = db.query(User).filter(User.userID == trans.userID).first()
    product = db.query(Product).filter(Product.proID == trans.productID).first()
    data = {"trans": trans, "user": user, "product": product}
    return data


def get_all_trans(db: Session, skip: int, limit: int):
    all_trans_db = (db.query(Trans)
                      .offset(skip)
                      .limit(limit)
                      .all())
    return all_trans_db


def get_all_trans_by_user_id(db: Session, user_id: str):
    trans = db.query(Trans).filter(Trans.userID == user_id).all()
    return trans


def delete_trans(db: Session, trans_id: str):
    trans_dlt = db.query(Trans).filter(Trans.transID == trans_id).first()
    if trans_dlt:
        db.delete(trans_dlt)
        db.commit()
    return trans_dlt

