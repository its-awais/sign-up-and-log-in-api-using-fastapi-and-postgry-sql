from fastapi import HTTPException,Depends,APIRouter
from app.models.User import User,Role
from app.database import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_async_session
from app.dependencies.get_current_admin import get_current_admin
from sqlalchemy import select
import uuid


router = APIRouter(prefix="/admin", tags=["admin"])

@router.patch("/users/{id}")
async def promote_user(
    id: uuid.UUID,
    db: AsyncSession = Depends(get_async_session),
    current_admin: User = Depends(get_current_admin)
):
    result = await db.execute(select(User).where(User.id == id))
    user = result.scalar_one_or_none()
    
    if not user:
        raise HTTPException(status_code=404,detail="user not found")
    
    
    if user.role == Role.admin:
        raise HTTPException(status_code=400, detail="user is already an admin")
    
    
    user.role = Role.admin
    await db.commit()
    await db.refresh(user)
    
    
    return {"message": f"${user.name} is promoted to an admin"}
    