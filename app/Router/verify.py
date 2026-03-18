from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends,APIRouter,HTTPException
from app.database import get_async_session
from sqlalchemy import select
from app.models.User import User

router = APIRouter(prefix="/auth", tags=["Auth"])
@router.get("/verify-email/{token}")
async def verify_email(token: str,  db: AsyncSession = Depends(get_async_session)):
    result = await db.execute(select(User).where(User.varification_token == token))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=400, detail="invalid token")
    
    if  user.is_verified:
        raise HTTPException(status_code=400, detail="Already verified")
    user.is_verified = True
    user.varification_token = None
    
    db.add(user)
    await db.commit()
    return {"message": "verified successfully"}
    
        
