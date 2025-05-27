

from datetime import date
from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from src.BaseModel import CarCreate, CarOut
from src.database import get_db
from src.models import (
    User, Order, Car,
    ColorType, DriveType, EngineType, FuelType,
    TransmissionType, InteriorType, BodyType
)

app = FastAPI()

# Pydantic модели для запросов и ответов
class UserBase(BaseModel):
    full_name: str
    email: str
    birth_date: date
    inn: int
    citizenship: str
    password_hash: str

class UserCreate(UserBase):
    pass

class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True

# Аналогично для других моделей (OrderOut, CarOut и т.д.)

# Users endpoints
@app.get("/users", response_model=List[UserOut])
def list_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@app.post("/users", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.put("/users/{user_id}", response_model=UserOut)
def update_user(
    user_id: int,
    user_update: UserCreate,
    db: Session = Depends(get_db)
):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    for key, value in user_update.dict().items():
        setattr(db_user, key, value)
    
    db.commit()
    db.refresh(db_user)
    return db_user

@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    db.delete(db_user)
    db.commit()
    return {"message": "User deleted successfully"}

# Cars endpoints
@app.get("/cars", response_model=List[CarOut])
def list_cars(db: Session = Depends(get_db)):
    return db.query(Car).all()

@app.post("/cars", response_model=CarOut)
def create_car(car: CarCreate, db: Session = Depends(get_db)):
    db_car = Car(**car.dict())
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car

# Аналогичные endpoints для Order, ColorType, DriveType и т.д.

# Contacts
@app.get("/contacts")
def get_contacts():
    return {
        "tel": "8 800 555 35 34",
        "email": "aaa@aaa.aaa",
        "VK": "auto"
    }