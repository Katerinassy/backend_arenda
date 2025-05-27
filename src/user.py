from sqlalchemy import create_engine, Column, Integer,String,Boolean, ForeignKey, Date, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

# class User(Base):
#     _tablename__ = "users"

#     id = Column(Integer, primary_key=True, index=True)
#     FIO = Column(String, index=True)
#     email = Column(String, unique=True, index=True)
#     birthday = Column(Date, index=True)
#     INN = Column(Integer, unique=True, index=True)
#     citizenship = Column(String, index=True)
#     password = Column(String, index=True)

class User(Base):
    __tablename__ = "users"  # Исправлено на двойное подчеркивание

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)  # Переименовано FIO → full_name
    email = Column(String, unique=True, nullable=False)
    birth_date = Column(Date, nullable=False)  # Переименовано birthday → birth_date
    inn = Column(Integer, unique=True, nullable=False)  # Переименовано INN → inn
    citizenship = Column(String, nullable=False)
    password_hash = Column(String, nullable=False)  # Переименовано password → password_hash

    orders = relationship("Order", back_populates="user")  # Добавлена связь с Order