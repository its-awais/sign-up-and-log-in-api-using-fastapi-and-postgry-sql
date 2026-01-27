import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy  import Column,String,Integer
from datetime import datetime,UTC
from sqlalchemy import DateTime
from app.database import Base
time_now = datetime.now(UTC)
class User(Base):
    __tablename__= "users"
    id  = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
    name = Column(String,nullable=False)
    email = Column(String,nullable=False,unique=True)
    password =Column(String,nullable=False)
    gender = Column(String, nullable=False)
    created_at = Column(DateTime, default=time_now)
