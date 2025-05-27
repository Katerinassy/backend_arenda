from sqlalchemy import create_engine, Column, Integer,String,Boolean, ForeignKey, Date, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()


# class Order(Base):
#     __tablename__ = "order"

#     id = Column(Integer, primary_key=True, index=True)
#     The_beginning_of_the_lease = Column(Date, index=True)
#     end_of_lease = Column(Date, index=True)
#     place = Column(String, index=True)
#     final_price = Column(Float, index=True)
#     user_id = Column(Integer, ForeignKey("users_types.id"))
#     cars_id = Column(Integer, ForeignKey("cars_types.id"))

#     user = relationship("User")
#     cars = relationship("Cars")

class Order(Base):
    __tablename__ = "orders"  # Изменил на множественное число для соответствия

    id = Column(Integer, primary_key=True, index=True)
    The_beginning_of_the_lease = Column(Date, index=True)
    end_of_lease = Column(Date, index=True)
    place = Column(String, index=True)
    final_price = Column(Float, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))  # Упростил название таблицы
    car_id = Column(Integer, ForeignKey("cars.id"))    # Изменил на car_id вместо cars_id

    user = relationship("User")
    car = relationship("Car", back_populates="orders")  # Соответствует связи в Car