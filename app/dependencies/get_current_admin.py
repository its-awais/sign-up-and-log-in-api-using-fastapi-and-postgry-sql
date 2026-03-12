from fastapi import Depends,HTTPException
from app.models.User import User,Role
from app.dependencies.auth import get_current_user


async def get_current_admin(
    current_user: User = Depends(get_current_user)
):
    if  current_user.role != Role.admin:
        raise HTTPException(status_code=403, detail="admin privileges required")
    return current_user
    