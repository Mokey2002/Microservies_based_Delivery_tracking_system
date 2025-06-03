from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import requests
from app import models, schemas, crud, database

app = FastAPI()
models.Base.metadata.create_all(bind=database.engine)

ORDER_SERVICE_URL = "http://order-service:8000/orders/"

def validate_order(order_id: int):
    response = requests.get(f"{ORDER_SERVICE_URL}{order_id}")
    if response.status_code != 200:
        raise HTTPException(status_code=400, detail="Invalid order_id")

@app.post("/trackings/", response_model=schemas.Tracking)
def create_tracking(tracking: schemas.TrackingCreate, db: Session = Depends(database.get_db)):
    validate_order(tracking.order_id)
    return crud.create_tracking(db, tracking)

@app.get("/trackings/order/{order_id}", response_model=schemas.Tracking)
def read_tracking(order_id: int, db: Session = Depends(database.get_db)):
    tracking = crud.get_tracking_by_order(db, order_id)
    if not tracking:
        raise HTTPException(status_code=404, detail="Tracking not found")
    return tracking

@app.put("/trackings/{tracking_id}", response_model=schemas.Tracking)
def update_tracking(tracking_id: int, update: schemas.TrackingUpdate, db: Session = Depends(database.get_db)):
    tracking = crud.update_tracking_status(db, tracking_id, update.status)
    if not tracking:
        raise HTTPException(status_code=404, detail="Tracking not found")
    return tracking

