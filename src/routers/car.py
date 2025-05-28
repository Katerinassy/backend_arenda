from fastapi import APIRouter
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from src.database import get_db
from src.models.car import Car
from src.schema.carschema import CarResponse
from routers import car

router = APIRouter()

@router.get("/{id}", response_model=CarResponse)
def get_car(id: int, db: Session = Depends(get_db)):
    car = db.query(Car).filter(Car.id == id).first()
    if not car:
        raise HTTPException(status_code=404, detail="He HaWденo")
    return car

app = FastAPI()
app.include_router(car.router, prefix="/car", tags=["car"])