from datetime import datetime
import enum
from pydantic import BaseModel, Field

class VenueTypes(str, enum.Enum):
    ONLINE = "Online"
    OFFLINE = "Offline"
    HYBRID = "Hybrid"
    
class VenueBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=100)
    location: str | None = Field(None, max_length=255)
    venue_type: VenueTypes
    
class VenueCreate(VenueBase):
    pass

class VenueUpdate(BaseModel):
    name: str | None = Field(None, min_length=3 , max_length=100)
    location: str | None = Field(None, max_length=255)
    venue_type: VenueTypes | None = Field(None)
    
class VenueOut(VenueBase):
    id: int
    created_at: datetime | None = None
    updated_at: datetime | None = None
    
    class Config:
        from_attributes = True