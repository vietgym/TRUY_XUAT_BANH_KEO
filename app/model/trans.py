from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base
from app.model.user import User
from app.model.product import Product


class Trans(Base):
    __tablename__ = "trans"
    transID = Column(String, primary_key=True, index=True)
    transTime = Column(String)
    transHash = Column(String)

    userID = Column(String, ForeignKey("users.userID", ondelete="CASCADE"))
    productID = Column(String, ForeignKey("products.proID", ondelete="CASCADE"))
    user = relationship("User", back_populates="trans")
    product = relationship("Product", back_populates="trans")