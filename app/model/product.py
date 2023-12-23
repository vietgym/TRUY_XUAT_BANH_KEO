from sqlalchemy import Column, String, ForeignKey, LargeBinary
from sqlalchemy.orm import relationship
from app.db.database import Base
from app.model.trans import Trans


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
