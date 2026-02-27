from sqlalchemy import Integer, Column, String, DateTime, ForeignKey, Float, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base
import enum


class CategoryEnum(str, enum.Enum):
    FOOD = "food"
    Travel = "travel"
    Shopping = "shopping"
    Bills = "bills"
    Entertainment = "entertainment"
    Other = "other"


class Expense(Base):
    __tablename__ = "expense"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)

    title = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    category = Column(Enum(CategoryEnum), nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    user = relationship("User", back_populates="expenses")