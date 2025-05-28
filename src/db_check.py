from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from src.type import Base 

DATABASE_URL = "sqlite:///./example.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Создание таблиц (если необходимо)
Base.metadata.create_all(bind=engine)


inspector = inspect(engine)
print("Существующие таблицы:", inspector.get_table_names()) 

# Dependency для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()