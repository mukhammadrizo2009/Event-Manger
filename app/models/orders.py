import enum
from sqlalchemy import (
    Column,
    Float,
    Enum,
    Integer,
    ForeignKey
)
from sqlalchemy.orm import relationship
from .base import BaseModel

class OrderTypes(str, enum.Enum):
    ONLINE = "Online"     
    OFFLINE = "Offline"  
    VIP = "VIP"             
    STANDARD = "Standard" 
    
class Orders(BaseModel):
    __tablename__ = "orders"
    
    order_type = Column(Enum(OrderTypes) , default=OrderTypes.OFFLINE , nullable=False)
    price = Column(Float)
    quantity = Column(Integer)
    event_id = Column(Integer , ForeignKey('events.id'))
    
    order = relationship("Orders" , back_populates="orders")