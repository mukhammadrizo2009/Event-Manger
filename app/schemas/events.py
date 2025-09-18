from datetime import datetime
import enum
from pydantic import BaseModel, Field

class EventTypes(str , enum.Enum):
    CONSERT = "Consert"
    WEDDIMG = "Wedding"
    CONFERENCE = "Conference"
    WORKSHOP = "Workshop"
    SEMINAR = "Seminar"
    OTHER = "Other"
    
class EventStatus(str, enum.Enum):
    DRAFT = "Draft"
    PUBLISHED = "Published"
    ONGOING = "Ongoing"
    COMPLETED = "Completed"
    CANCELED = "Canceled"
    
class EventBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=128)
    description: str | None = Field()
    address: str | None = Field()
    event_type: EventTypes
    status: EventStatus
    start_date: datetime
    end_date: datetime
    venue_id: int
    organizer_id: int
    
class EventCreate(EventBase):
    pass

class EventUpdate(BaseModel):
    name: str | None = Field(None, min_length=3, max_length=128)
    description: str | None = Field(None, max_length=255)
    event_type: EventTypes | None = Field(None)
    status: EventStatus | None = Field(None)
    
class EventOut(EventBase):
    id: int
    created_at: datetime | None = None
    updated_at: datetime | None = None
    
    class Config:
        from_attributes = True