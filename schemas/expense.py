from pydantic import BaseModel
from datetime import datetime
from models.expense import CategoryEnum
from typing import Optional


class ExpenseCreate(BaseModel):
    title: str
    amount: float
    category: CategoryEnum
    created_at: Optional[datetime] = None


class ExpenseResponse(BaseModel):
    id: int
    user_id: int
    title: str
    amount: float
    category: CategoryEnum
    created_at: datetime

    class Config:
        from_attributes = True


class ExpenseUpdate(BaseModel):
    title: Optional[str] = None
    amount: Optional[float] = None
    category: Optional[CategoryEnum] = None