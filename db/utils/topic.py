from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import selectinload
from sqlalchemy import select
from db.models.topic import Topic


async def create_topic(topic: str, session: AsyncSession):
    try:
        topic_db = Topic(name=topic)
        session.add(topic_db)
        await session.commit()
        return 'ok'
    except IntegrityError:
        raise HTTPException(status_code=409, detail='Topic already exists')


async def create_topic_no_commit(topic: str, session: AsyncSession):
    topic_db = Topic(name=topic)
    session.add(topic_db)
    await session.flush()
    await session.refresh(topic_db)
    return topic_db



async def get_topic(topic: str, session: AsyncSession):
    return (await session.execute(select(Topic).filter(Topic.name == topic))).scalar_one_or_none()


async def get_topic_with_users(topic: str, session: AsyncSession):
    return (await session.execute(
        select(Topic).filter(Topic.name == topic).options(selectinload(Topic.users)))).scalar_one_or_none()


async def get_topic_with_profiles(topic: str, session: AsyncSession):
    return (await session.execute(
        select(Topic).filter(Topic.name == topic).options(selectinload(Topic.profiles)))).scalar_one_or_none()