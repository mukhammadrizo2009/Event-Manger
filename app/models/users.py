import enum
from sqlalchemy import (
    Column,
    String,
    Text,
    CheckConstraint,
    Enum
)
from sqlalchemy.orm import relationship
from .base import BaseModel

class UserTypes(str, enum.Enum):
    ADMIN = "Admin"
    ORGANIZER = "Organizer"
    USER = "User"
    
class Users(BaseModel):
    __tablename__ = "users"
    
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    full_name = Column(String(100), nullable=False)
    hashed_password = Column(Text, nullable=False)
    user_type = Column(Enum(UserTypes), default=UserTypes.USER , nullable=False)
    
    events = relationship("Events" , back_populates="organizer")
    
    __table_args__ = (
        CheckConstraint("char_lenght(username) >= 3", name="username_min_lenght"),
        CheckConstraint("char_lenght(full_name) >= 3", name="full_name_min_lenght"),
    ) 