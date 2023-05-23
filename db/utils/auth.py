from db.models.user import User
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from fastapi import HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from validation.user import RegistrationUser
from security import password, jwt


async def create_user(reg_data: RegistrationUser, session: AsyncSession):
    user = await session.execute(select(User).filter(User.username == reg_data.username))
    if not user.scalar():
        new_user = User(username=reg_data.username, hashed_password=password.hash_pass(reg_data.password))
        session.add(new_user)
        await session.commit()
        return jwt.create_token({'id': new_user.id, 'profile_id': None, 'username': reg_data.username})
    raise HTTPException(status_code=409, detail='Username already exists')


async def login_user(login_data: OAuth2PasswordRequestForm, session: AsyncSession):
    user = (await session.execute(select(User).filter(User.username == login_data.username).options(selectinload(User.profile)))).scalar_one_or_none()
    if user:
        if password.verify_pass(login_data.password, user.hashed_password):
            return jwt.create_token({'id': user.id, 'profile_id': user.profile.id, 'username': user.username})
        raise HTTPException(status_code=401, detail="Wrong username or password")
    raise HTTPException(status_code=404, detail="User doesn't exist")
