from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    item_name = Column(String, index=True)
    amount = Column(Float)
    status = Column(String, default="pending")

