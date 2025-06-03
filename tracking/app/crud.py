from sqlalchemy.orm import Session
from app import models, schemas

def create_tracking(db: Session, tracking: schemas.TrackingCreate):
    db_tracking = models.Tracking(**tracking.dict())
    db.add(db_tracking)
    db.commit()
    db.refresh(db_tracking)
    return db_tracking

def get_tracking_by_order(db: Session, order_id: int):
    return db.query(models.Tracking).filter(models.Tracking.order_id == order_id).first()

def update_tracking_status(db: Session, tracking_id: int, status: str):
    tracking = db.query(models.Tracking).filter(models.Tracking.id == tracking_id).first()
    if tracking:
        tracking.status = status
        db.commit()
        db.refresh(tracking)
    return tracking

