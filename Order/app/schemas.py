from pydantic import BaseModel

class OrderBase(BaseModel):
    user_id: int
    item_name: str
    amount: float

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id: int
    status: str
    class Config:
        orm_mode = True

