from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    userID = Column(String, primary_key=True, index=True)
    userName = Column(String)
    userEmail = Column(String)
    userLg = Column(String)
    userPass = Column(String)
    role = Column(String)

    trans = relationship("Trans", back_populates="user")


class Product(Base):
    __tablename__ = "products"
    proID = Column(String, primary_key=True, index=True)
    proName = Column(String)
    manufacturerAdd = Column(String)
    manufacturerName = Column(String)
    manufacturerCont = Column(String)
    distributorAdd = Column(String)
    distributorName = Column(String)
    distributorCont = Column(String)
    otherDetails = Column(String)

    trans = relationship("Trans", back_populates="product")


class Trans(Base):
    __tablename__ = "trans"
    transID = Column(String, primary_key=True, index=True)
    transTime = Column(String)
    transHash = Column(String)

    userID = Column(String, ForeignKey("users.userID", ondelete="CASCADE"))
    productID = Column(String, ForeignKey("products.proID", ondelete="CASCADE"))
    user = relationship("User", back_populates="trans")
    product = relationship("Product", back_populates="trans")
