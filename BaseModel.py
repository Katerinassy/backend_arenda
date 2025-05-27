# from pydantic import BaseModel, EmailStr,HttpUrl
# from datetime import datetime
# from typing import Optional,List

# class User(BaseModel):
#     id:int
#     FIO:str
#     email:EmailStr
#     birthday:datetime
#     INN: int
#     citizenship: str
#     password: str


# class UserOut(BaseModel):
#     id:int
#     FIO:str
#     email:EmailStr
#     birthday:datetime
#     INN: int
#     citizenship: str

# class UserCreate(BaseModel):
#     id:int
#     FIO:str
#     email:EmailStr
#     birthday:datetime
#     INN: int
#     citizenship: str

# incoming_data = {
#     "id": "54651654",
#     "FIO": "Bob",
#     "birthday": "",
#     "email": "bob@example.com",
#     "INN": "",
#     "citizenship": "",
#     "password": ""
# }

# user = User(**incoming_data)
# print(user)

# class Order(BaseModel):
#     id: int
#     the_beginning_of_the_lease: datetime
#     end_of_lease: datetime
#     place: str
#     final_price: float
#     user_id: int
#     cars_id: int

# class OrderOut(BaseModel):
#     id: int
#     the_beginning_of_the_lease: datetime
#     end_of_lease: datetime
#     place: str
#     final_price: float

# class OrderCreate(BaseModel):
#     id: int
#     the_beginning_of_the_lease: datetime
#     end_of_lease: datetime
#     place: str
#     final_price: float

# class Cars(BaseModel):
#     id: int
#     name_car: str
#     price: float
#     year: int
#     box: str
#     body_type: str
#     salon: str
#     tank_capacity: float
#     cruise_control: bool
#     maximum_speed: float
#     fuel_consumption: float
#     colors_id: int
#     engines_id: int
#     drives_id: int
#     fuels_id: int

# class CarsOut(BaseModel):
#     id: int
#     name_car: str
#     price: float
#     year: int
#     box: str
#     body_type: str
#     salon: str
#     tank_capacity: float
#     cruise_control: bool
#     maximum_speed: float
#     fuel_consumption: float
#     colors_id: int
#     engines_id: int
#     drives_id: int
#     fuels_id: int

# class CarsCreate(BaseModel):
#     id: int
#     name_car: str
#     price: float
#     year: int
#     box: str
#     body_type: str
#     salon: str
#     tank_capacity: float
#     cruise_control: bool
#     maximum_speed: float
#     fuel_consumption: float
#     colors_id: int
#     engines_id: int
#     drives_id: int
#     fuels_id: int

# class Fuels(BaseModel):
#     id: int
#     fuel: str


# class FuelsOut(BaseModel):
#     id: int
#     fuel: str

# class FuelsCreate(BaseModel):
#     id: int
#     fuel: str

# class Colors(BaseModel):
#     id: int
#     color: str

# class ColorsOut(BaseModel):
#     id: int
#     color: str

# class ColorsCreate(BaseModel):
#     id: int
#     color: str

# class Drives(BaseModel):
#     id: int
#     drive: str

# class DrivesOut(BaseModel):
#     id: int
#     drive: str

# class DrivesCreate(BaseModel):
#     id: int
#     drive: str

# class Engines(BaseModel):
#     id: int
#     engine: str

# class EnginesOut(BaseModel):
#     id: int
#     engine: str

# class EnginesCreate(BaseModel):
#     id: int
#     engine: str

# class UserFull(BaseModel):
#     id: int
#     FIO: str
#     email:EmailStr
#     birthday:datetime
#     INN: int
#     citizenship: str
#     password: str

# user_full = UserFull(
#     id=123,
#     FIO="",
#     email="ivan.petrov@example.com",
#     birthday="",
#     INN="",
#     citizenship="",
#     password=""
# )

# print(user_full)

# class OrderFull(BaseModel):
#     id: int
#     The_beginning_of_the_lease: datetime
#     end_of_lease: datetime
#     place: str
#     final_price: float
#     user_id: int
#     cars_id: int
#     user: User
#     cars: Cars

# order_full = OrderFull(
#     id="",
#     The_beginning_of_the_lease="",
#     end_of_lease="",
#     place="",
#     final_price="",
#     user_id="",
#     cars_id="",
#     user={
#         "id": "54651654",
#         "FIO": "Bob",
#         "birthday": "",
#         "email": "bob@example.com",
#         "INN": "",
#         "citizenship": "",
#         "password": ""
#     },
#     cars={
#         "id": "",
#         "name_car": "",
#         "price": "",
#         "year": "",
#         "box": "",
#         "body_type": "",
#         "salon": "",
#         "tank_capacity": "",
#         "cruise_control": "",
#         "maximum_speed": "",
#         "fuel_consumption": "",
#         "colors_id": "",
#         "engines_id": "",
#         "drives_id": "",
#         "fuels_id": ""
#     }
# )

# print(order_full)

# class CarsFull(BaseModel):
#     id: int
#     name_car: str
#     price: float
#     year: int
#     box: str
#     body_type: str
#     salon: str
#     tank_capacity: str
#     cruise_control : bool
#     maximum_speed: float
#     fuel_consumption : float
#     colors_id :int
#     engines_id :int
#     drives_id : int
#     fuels_id :int
#     colors: Colors
#     engines: Engines
#     drives: Drives
#     fuels: Fuels

# cars_full = CarsFull(
#     id="",
#     name_car="",
#     price="",
#     year="",
#     box="",
#     body_type="",
#     salon="",
#     tank_capacity="",
#     cruise_control="",
#     maximum_speed="",
#     fuel_consumption="",
#     colors={
#         "id": "",
#         "color": ""
#     },
#     engines={
#         "id": "",
#         "engine": ""
#     },
#     drives={
#         "id": "",
#         "drive": ""
#     }, 
#     fuels={
#         "id": "",
#         "fuel": ""
#     }
# )

# print(cars_full)


# class ColorFull(BaseModel): 
#     id: int
#     color: str

# color_full = ColorFull(
#     id="",
#     color=""
# )

# print(color_full)

# class FuelFull(BaseModel):
#     id: int
#     fuel: str


# class DriveFull(BaseModel):
#     id: int
#     drive: str

# drive_full = DriveFull(
#     id="",
#     drive=""
# )

# print(drive_full)

# class EngineFull(BaseModel):
#     id: int
#     engine:str

# engine_full = EngineFull(
#     id="",
#     engine=""
# )

from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

# User models
class UserBase(BaseModel):
    id: int
    FIO: str
    email: EmailStr
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
