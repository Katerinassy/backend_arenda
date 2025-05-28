from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# User models
class UserBase(BaseModel):
    id: int
    FIO: str
    email: str
    birthday: datetime
    INN: int
    citizenship: str

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    pass

# Car models
class CarBase(BaseModel):
    id: int
    name: str
    year: int
    engine_id: int
    drive_id: int
    transmission_id: int
    interior_id: int
    fuel_tank_capacity: float
    fuel_type_id: int
    cruise_control: bool
    body_type_id: int
    max_speed: int
    fuel_consumption: float
    price: float
    url_image: Optional[str] = None

class CarCreate(CarBase):
    pass

class CarOut(CarBase):
    engine: str
    drive: str
    transmission: str
    interior: str
    fuel_type: str
    body_type: str

# Order models
class OrderBase(BaseModel):
    id: int
    the_beginning_of_the_lease: datetime
    end_of_lease: datetime
    place: str
    final_price: float
    user_id: int
    car_id: int

class OrderCreate(OrderBase):
    pass

class OrderOut(OrderBase):
    user: UserOut
    car: CarOut

# Auxiliary models
class EngineType(BaseModel):
    id: int
    name: str

class DriveType(BaseModel):
    id: int
    name: str

class TransmissionType(BaseModel):
    id: int
    name: str

class InteriorType(BaseModel):
    id: int
    name: str

class FuelType(BaseModel):
    id: int
    name: str

class BodyType(BaseModel):
    id: int
    name: str

# Example usage
incoming_data = {
    "id": 1,
    "FIO": "John Doe",
    "email": "johndoe@example.com",
    "birthday": "1980-01-01T00:00:00",
    "INN": 1234567890,
    "citizenship": "USA",
    "password": "securepassword123"
}

user = UserCreate(**incoming_data)
print(user)
