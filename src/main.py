from datetime import date
from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String, Date, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel

# Инициализация базы данных
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Модель User
class User(Base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String)
    email = Column(String, unique=True, index=True)
    birth_date = Column(Date)
    inn = Column(Integer)
    citizenship = Column(String)
    password_hash = Column(String)
    driving_experience = Column(Integer, nullable=True)
    role = Column(String, default="USER")

# Модель Car
class Car(Base):
    __tablename__ = "car"
    
    id = Column(Integer, primary_key=True, index=True)
    # Добавьте остальные поля для Car

# Создание таблиц
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency для получения сессии БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic модели
class UserBase(BaseModel):
    full_name: str
    email: str
    birth_date: date
    inn: int
    citizenship: str
    password_hash: str
    driving_experience: int = None
    role: str = "USER"

class UserCreate(UserBase):
    pass

class UserOut(UserBase):
    id: int

    class Config:
        from_attributes = True  # Заменяем orm_mode в Pydantic v2

class CarCreate(BaseModel):
    pass  # Добавьте поля для Car

class CarOut(BaseModel):
    id: int
    
    class Config:
        from_attributes = True

# Users endpoints
@app.get("/users", response_model=List[UserOut])
def list_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@app.post("/users", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(**user.model_dump())
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
    
    for key, value in user_update.model_dump().items():
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
    db_car = Car(**car.model_dump())
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car

# Contacts
@app.get("/contacts")
def get_contacts():
    return {
        "tel": "8 800 555 35 34",
        "email": "aaa@aaa.aaa",
        "VK": "auto"
    }