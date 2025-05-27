from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, Integer, String, Date, Enum
from sqlalchemy.sql import func
from src.models import Base
from sqlalchemy.orm import relationship
import enum

class UserRole(enum.Enum):
    ADMIN = "admin"
    USER = "user"

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    role = Column(Enum(UserRole), default=UserRole.USER, nullable=False)
    full_name = Column(String, nullable=False)
    birth_date = Column(Date, nullable=False)
    driving_experience = Column(Integer, nullable=True)
    citizenship = Column(String, nullable=True)
    inn = Column(String, nullable=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    orders = relationship("Order", back_populates="user")