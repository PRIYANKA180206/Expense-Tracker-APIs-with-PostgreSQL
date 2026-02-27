from fastapi import FastAPI
from database import Base, engine
from routes import auth,expense
from models.user import User
from models.expense import Expense


app = FastAPI(title="Expense API with PostgresSQL")

Base.metadata.create_all(bind=engine)
app.include_router(auth.router)
app.include_router(expense.router)


