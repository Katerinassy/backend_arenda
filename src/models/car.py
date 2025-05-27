from sqlalchemy import create_engine, Column, Integer,String,Boolean, ForeignKey, Date, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

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
#     colors_id = Column(Integer, ForeignKey("colors_types.id"))
#     engines_id = Column(Integer,ForeignKey("engines_types.id"))
#     drives_id = Column(Integer,ForeignKey("drives_types.id"))
#     fuels_id = Column(Integer, ForeignKey("fuels_types.id"))
#     colors = relationship("Colors")
#     engines = relationship("Engines")
#     drives = relationship("Drives")
#     fuels = relationship("Fuels")

class Car(Base):
    tablename = "cars"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    engine_id = Column(Integer, ForeignKey("engine_types.id"), nullable=False)
    drive_id = Column(Integer, ForeignKey("drive_types.id"), nullable=False)
    transmission_id = Column(Integer, ForeignKey("transmission_types.id"), nullable=False)
    interior_id = Column(Integer, ForeignKey("interior_types.id"), nullable=False)
    fuel_tank_capacity = Column(float, nullable=False)
    fuel_type_id = Column(Integer, ForeignKey("fuel_types.id"), nullable=False)
    cruise_control = Column(Boolean, default=False)
    body_type_id = Column(Integer, ForeignKey("body_types.id"), nullable=False)
    max_speed = Column(Integer, nullable=False)
    fuel_consumption = Column(float, nullable=False)
    price = Column(float, nullable=False)
    url_image = Column(String, nullable=True)

    engine = relationship("EngineType")
    drive = relationship("DriveType")
    transmission = relationship("TransmissionType")
    interior = relationship("InteriorType")
    fuel_type = relationship("FuelType")
    body_type = relationship("BodyType")
    orders = relationship("Order", back_populates="car")
    
class FuelType(Base):
    __tablename__ = "fuel_types"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, index=True)


class DriveType(Base):
    __tablename__ = "drive_types"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, index=True)


class EngineType(Base):
    __tablename__ = "engine_types"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, index=True)