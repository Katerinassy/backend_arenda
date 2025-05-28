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