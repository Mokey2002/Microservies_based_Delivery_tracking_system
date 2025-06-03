from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.database import Base

class Tracking(Base):
    __tablename__ = "trackings"
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, index=True)
    status = Column(String, default="pending")
    last_updated = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

