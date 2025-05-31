from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, crud, database

app = FastAPI()


models.Base.metadata.create_all(bind=database.engine)

@app.post("/orders/", response_model=schemas.Orders)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    return crud.create_user(db, Order)
    
    
@app.get("/orders/{order_id}", response_model=schemas.Orders)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    db_Order = crud.get_Order(db, order_id)
    if db_Order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_Order

