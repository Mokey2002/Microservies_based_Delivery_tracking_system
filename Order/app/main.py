from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, crud, database

app = FastAPI()


models.Base.metadata.create_all(bind=database.engine)
USER_SERVICE_URL = "http://user-service:8000/users/"

def validate_user(user_id: int):
    response = requests.get(f"{USER_SERVICE_URL}{user_id}")
    if response.status_code != 200:
        raise HTTPException(status_code=400, detail="User does not exist")
        
        
@app.post("/orders/", response_model=schemas.Order)
def create_order(order: schemas.OrderCreate, db: Session = Depends(database.get_db)):
    validate_user(order.user_id)
    return crud.create_order(db, Order)
    
    
@app.get("/orders/{order_id}", response_model=schemas.Order)
def read_order(order_id: int, db: Session = Depends(database.get_db)):
    db_Order = crud.get_order(db, order_id)
    if db_Order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_Order

