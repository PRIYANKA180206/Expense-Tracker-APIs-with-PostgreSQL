from fastapi import HTTPException,APIRouter,Depends,Response,Request
from sqlalchemy.orm import Session
from database import get_db
from models.user import User
from schemas.user import UserCreate,UserLogin
from utils.security import *
router = APIRouter(prefix="/auth",tags=["Auth"])

@router.post('/register')
def register(user : UserCreate,db: Session = Depends(get_db)):
   try:
       existing_user = db.query(User).filter(User.email == user.email).first()
       if existing_user:
           raise HTTPException(status_code=400, detail="Email already registered")

       new_user = User(
       username=user.username,
       email=user.email,
       hashed_password=hash_password(user.password)
       )
       db.add(new_user)
       db.commit()
       db.refresh(new_user)
       return {"message":"User registered successfully"}
   except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post('/login')
def login(user : UserLogin,response : Response,db: Session = Depends(get_db)):
    try:
        db_user = db.query(User).filter(User.email == user.email).first()
        if not db_user or not verify_password(user.password, db_user.hashed_password):
            raise HTTPException(status_code=401, detail="Incorrect email or password")

        access_token=create_access_token({"sub" : str(db_user.id)})
        refresh_token=create_refresh_token({"sub": str(db_user.id)})

        response.set_cookie(key="access_token", value=access_token, httponly=True, samesite="lax")
        response.set_cookie(key="refresh_token", value=refresh_token, httponly=True, samesite="lax")

        return {"message" : "Logged in successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post('/refresh')
def refresh_token(request : Request,response : Response):
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(status_code=401, detail="Could not refresh token")
    try:
        payload = decode_token(token)
        user_id = payload.get("sub")

        new_access_token = create_access_token({"sub": str(user_id)})

        response.set_cookie(key="access_token", value=new_access_token, httponly=True, samesite="lax")

        return {"message": "Successfully refreshed token"}
    except:
        raise HTTPException(status_code=401, detail="Invalid refresh token")

@router.post('/logout')
def logout(response : Response):
    response.delete_cookie("access_token")
    response.delete_cookie("refresh_token")
    return {"message": "Successfully logged out"}







