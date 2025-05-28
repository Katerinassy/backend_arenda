from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    full_name: str
    
    
class UserCreate(BaseModel):
    role: Optional[str] = "user"
    full_name: str
    birth_date: date
    driving_experience: Optional[int] = None
    citizenship: Optional[str] = None
    inn: Optional[str] = None
    email: str
    password: str


class UserUpdate(BaseModel):
    role: Optional[str] = None
    full_name: Optional[str] = None
    birth_date: Optional[date] = None
    driving_experience: Optional[int] = None
    citizenship: Optional[str] = None
    inn: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None

class UserResponse(BaseModel):
    id: int
    role: str
    full_name: str
    birth_date: date
    driving_experience: Optional[int]
    citizenship: Optional[str]
    inn: Optional[str]
    email: str
    created_at: datetime

    class Config:
        from_attributes = True

class LoginRequest(BaseModel):
    email: str
    password: str