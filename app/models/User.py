import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy  import Column,String,Integer,DateTime,Enum  # and this enum would do like restrict the value inside the database so it cannot used by anyone 
from enum import Enum as pyEnum  #they are used to restrict the value
from app.database import Base
class Role(str,pyEnum):
    user = "user"
    admin = "admin"
    

class User(Base):
    __tablename__= "users"
    id  = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
    name = Column(String,nullable=False)
    email = Column(String,nullable=False,unique=True)
    password =Column(String,nullable=False)
    role = Column(Enum(Role), nullable=False, default=Role.user)
    gender = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True),server_default=func.now())
