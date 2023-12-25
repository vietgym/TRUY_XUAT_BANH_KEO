import uuid
import json
from sqlalchemy.orm import Session
from app.model.all import User, Trans, Product
from app.schemas import schemas


def create_user(db: Session, user: schemas.UserBase):
    ID = str(uuid.uuid4())
    db_user = User(userID=ID,
                   userEmail=user.userEmail,
                   userLg=user.userLg,
                   userPass=user.userPass,
                   role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user_id: str, user_update: schemas.UserBase):
    db_user_check = get_user(db=db, user_id=user_id)
    if db_user_check is None:
        return {"mess": "LỖI KHÔNG TẠO ĐƯỢC PRODUCT MỚI"}
    for field, value in user_update.dict().items():
        setattr(db_user_check, field, value)
    db.commit()
    db.refresh(db_user_check)
    return db_user_check


def get_user(db: Session, user_id: str):
    user_respond = db.query(User).filter(User.userID == user_id).first()
    return user_respond


def get_full_trans_user(db: Session, user_id: str):
    user = db.query(User).filter(User.userID == user_id).first()
    trans = db.query(Trans).filter(Trans.userID == user_id).all()
    data = {"user": user, "trans": trans}
    return data


def get_full_product_user(db: Session, user_id: str):
    user = db.query(User).filter(User.userID == user_id).first()
    trans = db.query(Trans).filter(Trans.userID == user_id).all()
    data = {"user": user, "trans": trans}
    return data


def get_all_user(db: Session, skip: int, limit: int):
    all_user_db = (db.query(User)
                   .offset(skip)
                   .limit(limit)
                   .all())
    return all_user_db


def delete_user(db: Session, user_id: str):
    db_user = db.query(User).filter(User.userID == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user


# class UserAndTransResponse:
#     def __init__(self, user, trans):
#         self.user = user
#         self.trans = trans
#
#
# def get_full_trans_user(db: Session, user_id: str):
#     # user = db.query(User).filter(User.userID == user_id).first()
#     # trans = db.query(Trans).filter(Trans.userID == user_id).all()
#     data = (db.query(User, Trans)
#             .outerjoin(Trans, User.userID == Trans.userID)
#             .filter(User.userID == user_id).all())
#     response = [UserAndTransResponse(user=user, trans=trans) for user, trans in data]
#     return response