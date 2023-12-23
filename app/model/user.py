from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base
from app.model.trans import Trans

class User(Base):
    __tablename__ = "users"
    userID = Column(String, primary_key=True, index=True)
    userEmail = Column(String)
    userLg = Column(String)
    userPass = Column(String)
    role = Column(String)

    trans = relationship("Trans", back_populates="user")