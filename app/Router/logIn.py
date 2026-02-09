from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from argon2 import PasswordHasher
from app.models.User import User
from app.Schema.User import UserLogin,LoginResponse
from app.core.security import create_access_token
from sqlalchemy import select
from app.database import get_async_session
from argon2.exceptions import VerifyMismatchError
from fastapi.responses import JSONResponse
ph = PasswordHasher()
# Define the router for logIn
router = APIRouter(prefix="/auth",tags=["Auth"])
@router.post("/logIn",response_model=LoginResponse)
async def logIn(user_data: UserLogin, db: AsyncSession = Depends(get_async_session)):
    result = await db.execute(select(User).where(User.email == user_data.email))
    existing_user = result.scalar_one_or_none()
    # we already get the user from the database and we just need to verify the password that user provided with the hashed password
    if not existing_user:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    try:
        ph.verify(existing_user.password, user_data.password)
    except VerifyMismatchError:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
   # this is step 5 to create a token after successful login

    access_token = create_access_token({
        "user_id":str(existing_user.id),
        "email":existing_user.email
    })
    response =  JSONResponse(content= {"message": "log in successfully"})
    response.set_cookie(key="access_token", value= access_token, httponly=True)
    return response
    
          