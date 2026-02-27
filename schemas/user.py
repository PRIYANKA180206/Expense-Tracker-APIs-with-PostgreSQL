from datetime import datetime
from pydantic import BaseModel, EmailStr,Field,field_validator
import re


class UserCreate(BaseModel):
    id : int = Field(...,description="User ID")
    username: str = Field(..., example="Username", description="Enter your username")
    email: EmailStr = Field(..., example="user@example.com", description="Enter your email address")
    password: str = Field(..., example="Password@123",description="Strong password (8+ chars, 1 capital, 1 number, 1 special char)")
    created_at: datetime = Field(default_factory=datetime.now, description="Date and time of creation")
    @field_validator("password")
    @classmethod
    def validate_strong_password(cls, value: str):
        pattern = r"^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$"
        if not re.match(pattern, value):
            raise ValueError(
                "Password must be at least 8 characters long, "
                "contain one uppercase letter, one number and one special character."
            )
        return value

class UserLogin(BaseModel):
    email : EmailStr
    password : str
