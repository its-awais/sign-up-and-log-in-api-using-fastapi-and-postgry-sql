import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy  import Column,String,Integer
from datetime import datetime
from sqlalchemy import DateTime
from app.database import Base

class User(Base):
    __tablename__= "users"
    id  = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
    name = Column(String,nullable=False)
    email = Column(String,nullable=False)
    password =Column(String,nullable=False)
    create_at = Column(DateTime, default=datetime.utcnow)
