import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy  import Column,String,Integer,DateTime
from app.database import Base
class User(Base):
    __tablename__= "users"
    id  = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
    name = Column(String,nullable=False)
    email = Column(String,nullable=False,unique=True)
    password =Column(String,nullable=False)
    gender = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True),server_default=func.now())
