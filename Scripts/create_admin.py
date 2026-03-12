import asyncio
from argon2 import PasswordHasher
from app.database import session_maker
from app.models.User import User,Role
from sqlalchemy import select
ph = PasswordHasher()

async def  create_admin():
    async with session_maker() as db:
        get_admin_email = "awaisahmed123334444@gmail.com"
        existing = await db.execute(select(User).where(User.email == get_admin_email))
        existing_user = existing.scalar_one_or_none()
        if existing_user:
             print("admin already exist")
             return
         
        admin_user = User(
            name = "Awais",
            email = get_admin_email,
            password = ph.hash("Awais@admin0101"),
            gender="male",
            role = Role.admin
        ) 
        db.add(admin_user) 
        await db.commit()
        await db.refresh(admin_user)
        print("admin created successfully")      
        
if __name__ == "__main__":
    asyncio.run(create_admin()) 