from fastapi import APIRouter, Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from validation.user import RegistrationUser
from sqlalchemy.ext.asyncio import AsyncSession
from db.db_setup import get_session
from db.utils.auth import create_user, login_user

auth_router = APIRouter()


@auth_router.post('/registration')
async def registration_path(user: RegistrationUser, session: AsyncSession = Depends(get_session)):
    token = await create_user(user, session)
    return {'access_token': token, 'token_type': 'bearer'}


@auth_router.post('/login')
async def login_path(user: OAuth2PasswordRequestForm = Depends(), session: AsyncSession = Depends(get_session)):
    return {'access_token': await login_user(user, session), 'token_type': 'bearer'}
