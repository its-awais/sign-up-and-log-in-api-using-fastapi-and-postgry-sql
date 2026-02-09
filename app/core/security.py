import jwt
from datetime import datetime,timedelta,timezone
from config import setting

def create_access_token(data:dict):
  # first thing we need to do is to copy the data
    to_encode = data.copy()

    # second step is to add the expiration time to the token
    expire = datetime.now(timezone.utc) + timedelta(minutes=setting.ACCESS_TOKEN_EXPIRE_MINUTES)
  
    # third step is to update the copy of the date with the expiration time that we mentined in env file which is 30 minutes secret key but its fine
    # and we use in update({}) this is because its expect the dictionary so we pass the dictionary with key exp and value 
    to_encode.update({"exp": expire})


    # fourth step is to create the jwt token
    encoded_jwt = jwt.encode(to_encode,setting.SECRET_KEY,algorithm=setting.ALGORITHM)

    return encoded_jwt




