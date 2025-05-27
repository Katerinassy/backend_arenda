# from ast import List
# from fastapi import Depends, FastAPI, HTTPException
# from sqlalchemy import create_engine, Column, Integer,String,Boolean, ForeignKey, Date, Float
# from sqlalchemy.orm import Session

# from BaseModel import CarOut, CarsCreate, CarsOut, ColorsCreate, DrivesCreate, DrivesOut, EnginesCreate, EnginesOut, FuelsCreate, FuelsOut, OrderCreate, OrderOut, UserOut, ColorsOut, UserCreate
# from database import get_db
# from models import Colors, Drives, Engines, Fuels, User, Order, Cars
# app = FastAPI()

# users = []

# @app.get("/users", response_model=list[UserOut])
# def list_users(db: Session = Depends(get_db)):
#     return db.query(User).all()

# @app.post("/users", response_model=UserOut)
# def add_user(user: UserCreate, db: Session = Depends(get_db)):
#     db_user = User(**user.dict)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user

# @app.put("/users")
# def update_item(old:str, new: str, id: int, FIO: str, email: str, birthday: Date, INN: int, citizenship: str, password: str):
#     if old in users:
#         index = users.index(old)
#         users[index] = new
#         return{"message":"Обновлено","item": new}

# @app.delete("/users")
# def delete_item(item: str):
#     if item in users:
#         users.remove(item)
#         return{"message": "Пользователь удален","item":item}

# order = []

# @app.get("/order", response_model=list[OrderOut])
# def list_order(db: Session = Depends(get_db)):
#     return db.query(Order).all()

# @app.post("/order", response_model=OrderOut)
# def add_order(order: OrderCreate, db: Session = Depends(get_db)):
#     db_order = Order(**order.dict)
#     db.add(db_order)
#     db.commit()
#     db.refresh(db_order)
#     return db_order

# @app.put("/order")
# def update_item(old:str, new: str, id: int, The_beginning_of_the_lease: Date, end_of_lease: Date, place: str, final_price: float, user_id: int, cars_id: int):
#     if old in Order:
#         index = Order.index(old)
#         Order[index] = new
#         return{"message":"Заказ обновился","item": new}

# @app.delete("/order")
# def delete_item(item: str):
#     if item in Order:
#         Order.remove(item)
#         return{"message": "Заказ удалился","item":item}
    
# cars = []

# @app.get("/cars", response_model=list[CarsOut])
# def list_cars(db: Session = Depends(get_db)):
#     return db.query(Cars).all()

# @app.post("/cars", response_model=CarsOut)
# def add_cars(cars: CarsCreate, db: Session = Depends(get_db)):
#     db_cars = Cars(**cars.dict)
#     db.add(db_cars)
#     db.commit()
#     db.refresh(db_cars)
#     return db_cars

# @app.put("/cars")
# def update_item(old:str, new: str, id: int, name_car: str, price: float, year: int, box: str, body_type: str, salon: str, tank_capacity: float, cruise_control: Boolean, maximum_speed: float, fuel_consumption: float, colors_id: int, engines_id: int, drives_id: int, fuels_id: int):
#     if old in Cars:
#         index = Cars.index(old)
#         Cars[index] = new
#         return{"message":"Обновлено","item": new}

# @app.delete("/cars")
# def delete_item(item: str):
#     if item in Cars:
#         Cars.remove(item)
#         return{"message": "Машина не арендована","item":item}
    
# fuels = []

# @app.get("/fuels", response_model=List[FuelsOut])
# def list_fuels(db: Session = Depends(get_db)):
#     return db.query(Fuels).all()

# @app.post("/fuels", response_model=FuelsOut)
# def add_fuels(fuels: FuelsCreate, db: Session = Depends(get_db)):
#     db_fuels = Fuels(**fuels.dict)
#     db.add(db_fuels)
#     db.commit()
#     db.refresh(db_fuels)
#     return db_fuels

# @app.put("/fuels")
# def update_item(old:str, new: str, id: int, fuel: str):
#     if old in fuels:
#         index = fuels.index(old)
#         fuels[index] = new
#         return{"message":"Обновлено","item": new}
  
# @app.delete("/fuels")
# def delete_item(item: str):
#     if item in fuels:
#         fuels.remove(item)
#         return{"message": "Топливо не вырано","item":item}
    
# colors = []

# @app.get("/colors", response_model=List[Colors])
# def list_colors(db: Session = Depends(get_db)):
#     return db.query(Colors).all()

# @app.post("/colors", response_model=ColorsOut)
# def add_colors(colors: ColorsCreate, db: Session = Depends(get_db)):
#     db_colors = Colors(**colors.dict)
#     db.add(db_colors)
#     db.commit()
#     db.refresh(db_colors)
#     return db_colors

# @app.put("/colors")
# def update_item(old:str, new: str, id: int, color: str):
#     if old in colors:
#         index = colors.index(old)
#         colors[index] = new
#         return{"message":"Обновлено","item": new}

# @app.delete("/colors")
# def delete_item(item: str):
#     if item in colors:
#         colors.remove(item)
#         return{"message": "цвет не выбран","item":item}
    
# drives = []

# @app.get("/drives", response_model=list[DrivesOut])
# def list_drives(db: Session = Depends(get_db)):
#     return db.query(Drives).all()

# @app.post("/drives", response_model=DrivesOut)
# def add_drives(drives: DrivesCreate, db: Session = Depends(get_db)):
#     db_drives = Drives(**drives.dict)
#     db.add(db_drives)
#     db.commit()
#     db.refresh(db_drives)
#     return db_drives

# @app.put("/drives")
# def update_item(old:str, new: str, id: int, drive: str):
#     if old in Drives:
#         index = drives.index(old)
#         Drives[index] = new
#         return{"message":"Обновлено","item": new}

# @app.delete("/drives")
# def delete_item(item: str):
#     if item in Drives:
#         drives.remove(item)
#         return{"message": "двигатель не выбран","item":item}
    
# engines = []

# @app.get("/engines", response_model=list[EnginesOut])
# def list_engines(db: Session = Depends(get_db)):
#     return db.query(Engines).all()

# @app.post("/engines", response_model=EnginesOut)
# def add_engines(engines: EnginesCreate, db: Session = Depends(get_db)):
#     db_engines = Engines(**engines.dict)
#     db.add(db_engines)
#     db.commit()
#     db.refresh(db_engines)
#     return db_engines

# @app.put("/engines")
# def update_item(old:str, new: str, id: int, engine: str):
#     if old in engines:
#         index = engines.index(old)
#         engines[index] = new
#         return{"message":"Обновлено","item": new}

# @app.delete("/engines")
# def delete_item(item: str):
#     if item in engines:
#         engines.remove(item)
#         return{"message": "двигатель удален","item":item}
    
# @app.get("/contacts")
# def get_contacts():
#     return {
#         "tel": "8 800 555 35 34",
#         "email": "aaa@aaa.aaa",
#         "VK": "auto"
#     }

from datetime import date
from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from BaseModel import CarsCreate, CarsOut
from database import get_db
from models import (
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
@app.get("/cars", response_model=List[CarsOut])
def list_cars(db: Session = Depends(get_db)):
    return db.query(Car).all()

@app.post("/cars", response_model=CarsOut)
def create_car(car: CarsCreate, db: Session = Depends(get_db)):
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