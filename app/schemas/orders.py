from datetime import datetime
import enum
from pydantic import BaseModel , Field , EmailStr

class OrderTypes(str, enum.Enum):
    ADMIN = "Admin"
    ORGANIZER = "Organizer"
    USER = "User"
    
class OrderBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    full_name: str = Field(..., min_length=3, max_length=100)
    user_type: OrderTypes
    
class OrderCreate(OrderBase):
    hashed_password: str = Field(..., min_length=6)
    
class OrderUpdate(BaseModel):
    email: EmailStr | None = None
    full_name: str | None = Field(None, min_length=3, max_length=100)
    password: str | None = Field(None, min_length=6)
    user_types: OrderTypes | None = Field(None)
    
class OrdersOut(OrderBase):
    id: int
    created_at: datetime | None = None
    updated_at: datetime | None = None
    
    class Config:
        from_attributes = True