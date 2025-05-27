# from sqlalchemy import create_engine, Column, Integer,String,Boolean, ForeignKey, Date, Float
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker, relationship



# Base = declarative_base()

# class User(Base):
#     _tablename__ = "users"

#     id = Column(Integer, primary_key=True, index=True)
#     FIO = Column(String, index=True)
#     email = Column(String, unique=True, index=True)
#     birthday = Column(Date, index=True)
#     INN = Column(Integer, unique=True, index=True)
#     citizenship = Column(String, index=True)
#     password = Column(String, index=True)


# class Order(Base):
#     __tablename__ = "order"

#     id = Column(Integer, primary_key=True, index=True)
#     The_beginning_of_the_lease = Column(Date, index=True)
#     end_of_lease = Column(Date, index=True)
#     place = Column(String, index=True)
#     final_price = Column(Float, index=True)
#     user_id = Column(Integer, ForeignKey("users.id"))
#     cars_id = Column(Integer, ForeignKey("cars.id"))

#     user = relationship("User")
#     cars = relationship("Cars")

# class Cars(Base):
#     __tablename__ = "cars"

#     id = Column(Integer, primary_key=True, index=True)
#     name_car = Column(String, index=True)
#     price = Column(Float, index=True)
#     year = Column(Integer, index=True)
#     box = Column(String, index=True)
#     body_type = Column(String, index=True)
#     salon = Column(String,index=True)
#     tank_capacity = Column(Float, index=True)
#     cruise_control = Column(Boolean, index=True)
#     maximum_speed = Column(Float, index=True)
#     fuel_consumption = Column(Float, index=True)
#     colors_id = Column(Integer, ForeignKey("colors.id"))
#     engines_id = Column(Integer,ForeignKey("engines.id"))
#     drives_id = Column(Integer,ForeignKey("drives.id"))
#     fuels_id = Column(Integer, ForeignKey("fuels.id"))

#     colors = relationship("Colors")
#     engines = relationship("Engines")
#     drives = relationship("Drives")
#     fuels = relationship("Fuels")

# class Fuels(Base):
#     __tablename__ = "fuels"

#     id = Column(Integer, primary_key=True, index=True)
#     fuel = Column(String, index=True)


# class Colors(Base):
#     __tablename__ = "colors"

#     id = Column(Integer, primary_key=True, index=True)
#     color = Column(String, index=True)


# class Drives(Base):
#     __tablename__ = "drivers"

#     id = Column(Integer, primary_key=True, index=True)
#     drive = Column(String, index=True)


# class Engines(Base):
#     __tablename__ = "engines"

#     id = Column(Integer, primary_key=True, index=True)
#     engine = Column(String, index=True)


from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey, Date, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "users"  # Исправлено на двойное подчеркивание

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)  # Было FIO
    email = Column(String, unique=True, nullable=False)
    birth_date = Column(Date, nullable=False)  # Было birthday
    inn = Column(Integer, unique=True, nullable=False)  # Было INN
    citizenship = Column(String, nullable=False)
    password_hash = Column(String, nullable=False)  # Было password

    orders = relationship("Order", back_populates="user")

class FuelType(Base):
    __tablename__ = "fuel_types"  # Приведено к единому стилю

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, nullable=False, index=True)  # Было fuel

class ColorType(Base):
    __tablename__ = "color_types"  # Приведено к единому стилю

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, nullable=False, index=True)  # Было color

class DriveType(Base):
    __tablename__ = "drive_types"  # Исправлено с drivers

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, nullable=False, index=True)  # Было drive

class EngineType(Base):
    __tablename__ = "engine_types"  # Приведено к единому стилю

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, nullable=False, index=True)  # Было engine

class TransmissionType(Base):
    __tablename__ = "transmission_types"  # Новая таблица для коробки передач

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, nullable=False, index=True)

class InteriorType(Base):
    __tablename__ = "interior_types"  # Новая таблица для салона

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, nullable=False, index=True)

class BodyType(Base):
    __tablename__ = "body_types"  # Новая таблица для типа кузова

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, nullable=False, index=True)

class Car(Base):  # Переименовано с Cars для единообразия
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)  # Было name_car
    price = Column(Float, nullable=False)
    year = Column(Integer, nullable=False)
    transmission_id = Column(Integer, ForeignKey("transmission_types.id"), nullable=False)  # Было box
    body_type_id = Column(Integer, ForeignKey("body_types.id"), nullable=False)
    interior_id = Column(Integer, ForeignKey("interior_types.id"), nullable=False)  # Было salon
    fuel_tank_capacity = Column(Float, nullable=False)  # Было tank_capacity
    cruise_control = Column(Boolean, default=False)
    max_speed = Column(Integer, nullable=False)  # Было maximum_speed
    fuel_consumption = Column(Float, nullable=False)
    color_id = Column(Integer, ForeignKey("color_types.id"))
    engine_id = Column(Integer, ForeignKey("engine_types.id"))
    drive_id = Column(Integer, ForeignKey("drive_types.id"))
    fuel_type_id = Column(Integer, ForeignKey("fuel_types.id"))

    transmission = relationship("TransmissionType")
    body_type = relationship("BodyType")
    interior = relationship("InteriorType")
    color = relationship("ColorType")
    engine = relationship("EngineType")
    drive = relationship("DriveType")
    fuel_type = relationship("FuelType")
    orders = relationship("Order", back_populates="car")

class Order(Base):
    __tablename__ = "orders"  # Исправлено на множественное число

    id = Column(Integer, primary_key=True, index=True)
    start_date = Column(Date, nullable=False)  # Было The_beginning_of_the_lease
    end_date = Column(Date, nullable=False)  # Было end_of_lease
    location = Column(String, nullable=False)  # Было place
    total_price = Column(Float, nullable=False)  # Было final_price
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    car_id = Column(Integer, ForeignKey("cars.id"), nullable=False)  # Было cars_id

    user = relationship("User", back_populates="orders")
    car = relationship("Car", back_populates="orders")  # Было cars