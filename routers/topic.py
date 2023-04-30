from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from db.db_setup import get_session
from db.utils.topic import create_topic, get_topic, get_topic_with_profiles, get_topic_with_users

topic_router = APIRouter()


@topic_router.post('/create-topic/{topic}')
async def create_topic_path(topic: str, session: AsyncSession = Depends(get_session)):
    return await create_topic(topic, session)


@topic_router.get('/get-topic/{topic_name}')
async def get_topic_path(topic_name: str, session: AsyncSession = Depends(get_session)):
    return await get_topic(topic_name, session)


@topic_router.get('/get-topic-with-profiles/{topic_name}')
async def get_topic_with_profiles_path(topic_name: str, session: AsyncSession = Depends(get_session)):
    return await get_topic_with_profiles(topic_name, session)


@topic_router.get('/get-topic-with-users/{topic_name}')
async def get_topic_with_users_path(topic_name: str, session: AsyncSession = Depends(get_session)):
    return await get_topic_with_users(topic_name, session)
