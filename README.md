EXPENSE TRACKER API Scalable, Secure & Production-Ready Expense
Management Backend Built with FastAPI & PostgreSQL

PROJECT OVERVIEW

Expense Tracker API is a high-performance backend system designed to
manage users, workspaces, and shared expenses efficiently.

Built using asynchronous FastAPI architecture, this project follows
clean coding principles, secure authentication practices, and scalable
database design.

Core Capabilities: - JWT Authentication - Workspace-based Expense
Management - Role-based Access Control - Async PostgreSQL Operations -
OTP Verification Flow - Modular Architecture

TECH STACK

-   FastAPI (Async)
-   PostgreSQL
-   SQLAlchemy (Async ORM)
-   JWT Authentication
-   Passlib / Bcrypt (Password Hashing)
-   Pydantic (Data Validation)
-   Python 3.10+

FEATURES

1.  Authentication & Security

-   User Registration
-   Secure Login
-   JWT Access Token Generation
-   Password Hashing
-   OTP Verification System
-   Protected Routes

2.  Workspace Management

-   Create Workspace
-   Add Members
-   Role-based Access
-   Workspace-level Expense Isolation

3.  Expense Management

-   Create Expense
-   Update Expense (PATCH Support)
-   Delete Expense
-   List Expenses by Workspace
-   Expense Summary Endpoint

4.  Technical Highlights

-   Fully Asynchronous DB Operations
-   Clean Dependency Injection
-   Modular Routing Structure
-   Proper Error Handling
-   RESTful API Standards

DATABASE TABLES

-   users
-   workspaces
-   workspace_members
-   expenses
-   otp_store

Relationships: - One User → Multiple Workspaces - One Workspace →
Multiple Members - One Workspace → Multiple Expenses

INSTALLATION GUIDE

1.  Clone Repository git clone
    https://github.com/your-username/your-repo-name.git cd
    your-repo-name

2.  Create Virtual Environment python -m venv venv venv

3.  Install Dependencies pip install -r requirements.txt

4.  Configure Environment Variables (.env)
    DATABASE_URL=postgresql+asyncpg://username:password@localhost:5432/expense_db
    SECRET_KEY=your_super_secret_key ALGORITHM=HS256
    ACCESS_TOKEN_EXPIRE_MINUTES=30

5.  Run Server uvicorn app.main:app –reload

Server URL: http://127.0.0.1:8000

API Documentation: http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc

AUTHENTICATION FLOW

1.  Register User
2.  Verify OTP (if enabled)
3.  Login to receive JWT token
4.  Pass token in request header: Authorization: Bearer

PRODUCTION READY

-   Docker Deployable
-   CI/CD Friendly Structure
-   Cloud Ready (AWS / Render / Railway)
-   Scalable Architecture
-   Migration Ready

AUTHOR

Priyanka Backend Developer 

If you find this project useful, consider giving it a star on GitHub.
