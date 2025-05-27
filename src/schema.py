from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel

class CarBase(BaseModel):
    name: str
    year: int
    price: float
    # остальные базовые поля Car

class CarCreate(CarBase):
    pass

class CarResponse(CarBase):
    id: int
    created_at: datetime
    # остальные поля для ответа

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str
    full_name: str

class OrderBase(BaseModel):
    start_date: date
    end_date: date
    total_price: float