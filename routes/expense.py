from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List
from database import get_db
from models.expense import Expense, CategoryEnum
from models.user import User
from schemas.expense import ExpenseCreate, ExpenseResponse, ExpenseUpdate
from utils.current_user import get_current_user

router = APIRouter(prefix="/expenses", tags=["Expenses"])

@router.post("/", response_model=ExpenseResponse)
def create_expense(expense: ExpenseCreate,db: Session = Depends(get_db),current_user: User = Depends(get_current_user),):
    try:
        new_expense = Expense(title=expense.title,amount=expense.amount,category=expense.category,user_id=current_user.id,)
        db.add(new_expense)
        db.commit()
        db.refresh(new_expense)
        return new_expense
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/", response_model=List[ExpenseResponse])
def get_expenses(db: Session = Depends(get_db),current_user: User = Depends(get_current_user),):
    try:
        expenses = (db.query(Expense).filter(Expense.user_id == current_user.id).all())
        return expenses
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/category/{category}", response_model=List[ExpenseResponse])
def get_expenses_by_category(category: CategoryEnum,db: Session = Depends(get_db),current_user: User = Depends(get_current_user),):
    try:
        expenses = (db.query(Expense).filter(Expense.user_id == current_user.id,Expense.category == category,).all())
        return expenses
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/summary")
def expense_summary(db: Session = Depends(get_db),current_user: User = Depends(get_current_user),):
    try:
        total_amount = (db.query(func.sum(Expense.amount)).filter(Expense.user_id == current_user.id).scalar()or 0)
        expense_count = (db.query(func.count(Expense.id)).filter(Expense.user_id == current_user.id).scalar())
        return {
            "username": current_user.username,
            "total_expense": total_amount,
            "expense_count": expense_count,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{expense_id}", response_model=ExpenseResponse)
def get_expense_by_id(expense_id: int,db: Session = Depends(get_db),current_user: User = Depends(get_current_user),):
    try:
        expense = (db.query(Expense).filter(Expense.id == expense_id,Expense.user_id == current_user.id,).first())
        if not expense:
            raise HTTPException(status_code=404, detail="Expense not found")
        return expense
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.patch("/{expense_id}", response_model=ExpenseResponse)
def patch_expense(expense_id: int,expense_data: ExpenseUpdate,db: Session = Depends(get_db),current_user: User = Depends(get_current_user),):
    expense = (db.query(Expense).filter(Expense.id == expense_id,Expense.user_id == current_user.id,).first())
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    update_data = expense_data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(expense, key, value)
    db.commit()
    db.refresh(expense)
    return expense

@router.delete("/{expense_id}")
def delete_expense_by_id(expense_id: int,db: Session = Depends(get_db),current_user: User = Depends(get_current_user),):
    try:
        expense = (db.query(Expense).filter(Expense.id == expense_id,Expense.user_id == current_user.id,).first())
        if not expense:
            raise HTTPException(status_code=404, detail="Expense not found")
        db.delete(expense)
        db.commit()
        return {"message": "Expense deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))