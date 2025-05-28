# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, DateTime, Integer, String, Date, Enum, create_engine
# from sqlalchemy.sql import func
# from src.type import Base
# from sqlalchemy.orm import relationship
# import enum

# class UserRole(enum.Enum):
#     ADMIN = "admin"
#     USER = "user"
    
# engine = create_engine("sqlite:///./your_db_file.db", echo=True, future=True)

# class User(Base):
#     __tablename__ = "user"

#     id = Column(Integer, primary_key=True, index=True)
#     role = Column(Enum(UserRole), default=UserRole.USER, nullable=False)
#     full_name = Column(String, nullable=False)
#     birth_date = Column(Date, nullable=False)
#     driving_experience = Column(Integer, nullable=True)
#     citizenship = Column(String, nullable=True)
#     inn = Column(String, nullable=True)
#     email = Column(String, unique=True, index=True, nullable=False)
#     password_hash = Column(String, nullable=False)
#     created_at = Column(DateTime, server_default=func.now())

    # orders = relationship("Order", back_populates="user")
    
 
import enum
from sqlalchemy import Column, Integer, String, Date, DateTime, Enum
from sqlalchemy.sql import func
from src.type import Base  # Единый Base
from sqlalchemy.orm import relationship

class UserRole(enum.Enum):
    ADMIN = "admin"
    USER = "user"

class User(Base):
    __tablename__ = "user"

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

    # orders = relationship("Order", back_populates="user")  # если есть связь с заказами
