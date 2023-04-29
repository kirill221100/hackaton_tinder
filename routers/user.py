from fastapi import APIRouter, Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from validation.user import EditTopics
from sqlalchemy.ext.asyncio import AsyncSession
from db.db_setup import get_session
from security.oauth import get_current_user
from db.utils.user import edit_topics, get_matching_users, get_user_topics

user_router = APIRouter()


@user_router.post('/edit-topics')
async def edit_topics_path(topics_data: EditTopics, user_data=Depends(get_current_user),
                           session: AsyncSession = Depends(get_session)):
    return await edit_topics(topics_data, user_data['id'], session)


@user_router.get('/get-matching-users')
async def get_matching_users_path(user_data=Depends(get_current_user), session: AsyncSession = Depends(get_session)):
    return await get_matching_users(user_data['id'], session)


@user_router.get('/get-user-topics')
async def get_user_topics_path(user_data=Depends(get_current_user), session: AsyncSession = Depends(get_session)):
    return await get_user_topics(user_data['id'], session)
