from sqlalchemy import create_engine, Column, Integer,String,Boolean, ForeignKey, Date, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Car(Base):
    __tablename__ = "car"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    engine_id = Column(Integer, ForeignKey("engine_types.id"), nullable=False)
    drive_id = Column(Integer, ForeignKey("drive_types.id"), nullable=False)
    transmission_id = Column(Integer, ForeignKey("transmission_types.id"), nullable=False)
    interior_id = Column(Integer, ForeignKey("interior_types.id"), nullable=False)
    fuel_tank_capacity = Column(Float, nullable=False)
    fuel_type_id = Column(Integer, ForeignKey("fuel_types.id"), nullable=False)
    cruise_control = Column(Boolean, default=False)
    body_type_id = Column(Integer, ForeignKey("body_types.id"), nullable=False)
    max_speed = Column(Integer, nullable=False)
    fuel_consumption = Column(Float, nullable=False)
    price = Column(Float, nullable=False)
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