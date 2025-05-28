from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel

class OrderBase(BaseModel):
    start_date: date
    end_date: date
    total_price: float