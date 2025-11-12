from pydantic import BaseModel, EmailStr
from datetime import datetime

# Schema used for user registration
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

# Schema used when returning user data
class UserRead(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime  # Ensures proper datetime parsing in responses

    class Config:
        from_attributes = True  # Enables conversion from SQLAlchemy models
