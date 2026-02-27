from sqlalchemy.orm import relationship
from sqlalchemy import Column,Integer,String,DateTime
from datetime import datetime
from database import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True,nullable=False)
    username = Column(String, nullable=False, index=True)
    email = Column(String, unique=True, index=True,nullable=False)
    hashed_password = Column(String)

    expenses = relationship("Expense", back_populates="user")

