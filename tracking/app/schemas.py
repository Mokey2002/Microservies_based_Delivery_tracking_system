from pydantic import BaseModel
from datetime import datetime

class TrackingBase(BaseModel):
    order_id: int
    status: str = "pending"

class TrackingCreate(TrackingBase):
    pass

class TrackingUpdate(BaseModel):
    status: str

class Tracking(TrackingBase):
    id: int
    last_updated: datetime
    class Config:
        orm_mode = True

