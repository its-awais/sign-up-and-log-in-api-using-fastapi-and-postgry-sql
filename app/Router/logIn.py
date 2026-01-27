from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from argon2 import PasswordHasher
from app.models.User import User
from app.Schema.User import UserCreate,UserResponse
from sqlalchemy import select
from app.database import get_async_session
ph = PasswordHasher()
router = APIRouter(prefix="/auth/logIn",tags=["Auth/logIn"])
@router.post("/",response_model=UserResponse)
async def logIn(user_data: UserCreate, db: AsyncSession = Depends(get_async_session)):
    result = await db.execute(select(User).where(User.email == user_data.email))
    existing_user = result.scalar_one_or_none()
    if not existing_user:
        raise HTTPException(status_code=401, detail="please sign up first does not exist")
     
    hashed_password = ph.hash(user_data.password)
    USER = User(name=user_data.email, password=user_data.hashed_password)
    db.add(USER)
    await db.commit()
    await db.refresh(USER)
    return UserResponse.model_validate(USER)
    

          