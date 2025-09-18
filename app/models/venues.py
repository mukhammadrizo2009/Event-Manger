import enum
from sqlalchemy import (
    Column,
    String,
    CheckConstraint,
    Enum
)
from sqlalchemy.orm import relationship
from .base import BaseModel

class VenueTypes(str, enum.Enum):
    ONLINE = "Online"
    OFFLINE = "Offline"
    HYBRID = "Hybrid"
    
class Venues(BaseModel):
    __tablename__ = "venues"
    
    name = Column(String(100), unique=True , nullable=False)
    location = Column(String(255), nullable=True)
    venue_type = Column(Enum(VenueTypes), default=VenueTypes.OFFLINE, nullable=False)
    
    events = relationship("Events", back_populates="venue")
    
    __table_args__ = (
        CheckConstraint("char_lenght(name) >= 3" , name="venue_name_min_lenght"),
    )