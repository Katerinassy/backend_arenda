from sqlalchemy import create_engine, Column, Integer,String,Boolean, ForeignKey, Date, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class UserType(Base):
    __tablename__ = "user_types"
    id = Column(Integer, primary_key=True, index=True)
    FIO = Column(String, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    birthday = Column(Date, index=True, nullable=False)
    INN = Column(Integer, unique=True, index=True, nullable=False)
    citizenship = Column(String, index=True, nullable=False)
    password = Column(String, index=True, nullable=False)


class OrderType(Base):
    __tablename__ = "order_types"
    id = Column(Integer, primary_key=True, index=True)
    The_beginning_of_the_lease = Column(Date, index=True, nullable=False)
    end_of_lease = Column(Date, index=True, nullable=False)
    place = Column(String, index=True, nullable=False)
    final_price = Column(Float, index=True, nullable=False)


class CarsType(Base):
    __tablename__ = "cars_types"
    id = Column(Integer, primary_key=True, index=True)
    name_car = Column(String, index=True, nullable=False)
    price = Column(Float, index=True, nullable=False)
    year = Column(Integer, index=True, nullable=False)
    box = Column(String, index=True, nullable=False)
    body_type = Column(String, index=True, nullable=False)
    salon = Column(String,index=True, nullable=False)
    tank_capacity = Column(Float, index=True, nullable=False)
    cruise_control = Column(Boolean, index=True, nullable=False)
    maximum_speed = Column(Float, index=True, nullable=False)
    fuel_consumption = Column(Float, index=True, nullable=False)


class FuelsType(Base):
    __tablename__ = "fuels_types"
    id = Column(Integer, primary_key=True, index=True)
    fuel = Column(String, index=True, nullable=False)


class ColorsType(Base):
    __tablename__ = "colors_types"
    id = Column(Integer, primary_key=True, index=True)
    color = Column(String, index=True, nullable=False)


class DrivesType(Base):
    __tablename__ = "drives_types"
    id = Column(Integer, primary_key=True, index=True)
    drive = Column(String, index=True, nullable=False)

class EnginesType(Base):
    __tablename__ = "engines_types"
    id = Column(Integer, primary_key=True, index=True)
    engine = Column(String, index=True, nullable=False)