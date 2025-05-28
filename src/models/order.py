from datetime import datetime
from sqlalchemy import DateTime, create_engine, Column, Integer,String,Boolean, ForeignKey, Date, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True, index=True)
    # user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    car_id = Column(Integer, ForeignKey("car.id"), nullable=False)
    status = Column(String, default="pending")
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    address = Column(String, nullable=False)
    total_price = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # user = relationship("User", back_populates="order")
    car = relationship("Car", back_populates="order")