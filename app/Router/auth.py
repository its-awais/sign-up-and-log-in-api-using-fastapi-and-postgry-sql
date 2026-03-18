from fastapi import APIRouter,Depends,HTTPException  # depend automatically call the function without needing us
from argon2 import PasswordHasher
from app.database import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.User import User,Role
from sqlalchemy import select
from app.Schema.User import UserCreate,UserResponse
from app.utils.varification_email import generate_token
from app.utils.email import send_verification_email
router = APIRouter(prefix="/auth", tags=["Auth"])
ph = PasswordHasher()
@router.post("/signUp",response_model= UserResponse)
async def signUp(
    user_data: UserCreate,  # remember cannot use "-"
    db: AsyncSession=Depends(get_async_session)
   ):
  result = await db.execute(select(User).where(User.email == user_data.email.lower()))
  existing_user = result.scalar_one_or_none()
  if existing_user:
    raise HTTPException(status_code=400,detail="user already exist")
  hashed_password = ph.hash(user_data.password)
  token = generate_token()
  USER = User(name= user_data.name, email= user_data.email.lower(), password= hashed_password,gender=user_data.gender.value, role=Role.user,varification_token= token,is_verified = False)
  try:
    db.add(USER)
    await db.commit()
    await db.refresh(USER)
    await send_verification_email(USER.email, token)
    return UserResponse.model_validate(USER) 
  except Exception as e:
    await db.rollback() # so we use rollback, becasue if something change or in our db it rollback and tell user error 
    raise HTTPException(status_code=500, detail=f"something went Wrong {str(e)}")
       
 
   
