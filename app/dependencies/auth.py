from fastapi import Depends,HTTPException,Request
from jwt import PyJWTError
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_async_session
from app.models.User import User
from sqlalchemy import select
from app.models.User import Role
from config import setting
import jwt
 
async def get_current_user(
    request:Request,
    db:AsyncSession = Depends(get_async_session)
    ):
  token = request.cookies.get("access_token")
  
  if not token:
    raise HTTPException(status_code=401, detail="Not authenticated")
  
  try:
    payload = jwt.decode(
      token,
      setting.SECRET_KEY,
      algorithms=[setting.ALGORITHM]
    )
  except PyJWTError:
    raise HTTPException(status_code=401, detail="Invalid Error")
  
  user_id = payload.get('user_id')
  
  
  result = await db.execute(select(User).where(User.id == user_id))
  user = result.scalar_one_or_none();
    
  if not user:
    raise HTTPException(status_code=404, detail= "user not found")
  
  
  return user