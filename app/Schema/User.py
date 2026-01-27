from pydantic import BaseModel,Field,field_validator,EmailStr,ConfigDict
from datetime import datetime
from uuid import UUID
from enum import Enum
import re

PASSWORD_REGEX = re.compile(
    r"^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,12}$"
)
class Gender(str,Enum):
    male = "male"
    female = "female"

class UserCreate(BaseModel):
    name: str = Field(
        min_length=3,
        max_length=12,
        example="John01"
    )
    email:EmailStr= Field(
        example="john0101@gmail.com"
    )
    password: str = Field(
        min_length=8,
        max_length=12,
        example="john@0101 incldue special charcter to"
    )
    gender: Gender

    @field_validator("name")
    def validate_name(cls,value):
        if not re.search(r"[A-Z]",value):
            raise ValueError("password must contain atleast one uppercase letter")
        return value
    
    @field_validator("password")
    def validate_password(cls,value):
        if not PASSWORD_REGEX.match(value):
            raise ValueError(
                "Password must contain uppercase, number, and special character" 
            )
        return value


class UserResponse(BaseModel):
     id : UUID 
     name : str
     email : str
     gender: str
     
     model_config = ConfigDict(from_attributes=True)