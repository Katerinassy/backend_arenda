from datetime import datetime
from sqlalchemy import DateTime, create_engine, Column, Integer,String,Boolean, ForeignKey, Date, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    car_id = Column(Integer, ForeignKey("cars.id"), nullable=False)
    status = Column(String, default="pending")
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    address = Column(String, nullable=False)
    total_price = Column(float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="orders")
    car = relationship("Car", back_populates="orders")