from datetime import datetime
from pydantic import BaseModel


class ProductBase(BaseModel):
    proName: str
    manufacturerAdd: str
    manufacturerName: str
    manufacturerCont: str
    distributorAdd: str
    distributorName: str
    distributorCont: str
    otherDetails: str


class Product(ProductBase):
    proID: str

    class Config:
        from_attributes = True


class UserBase(BaseModel):
    userName: str
    userEmail: str
    userLg: str
    userPass: str
    role: str


class UserLogin(BaseModel):
    userLg: str
    userPass: str


class UserUpdate(BaseModel):
    userName: str
    userEmail: str


class User(UserBase):
    userID: str

    class Config:
        from_attributes = True


class TransBase(BaseModel):
    transTime: str
    transHash: str


class Trans(TransBase):
    transID: str
    userID: str
    productID: str

    class Config:
        from_attributes = True
        json_encoders = {
            datetime: lambda v: int(v.timestsmp())
        }
