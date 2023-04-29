from db.models.user import User
from db.models.topic import Topic
from db.models.profile import Profile
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from sqlalchemy import select, func, join, desc
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from validation.user import EditTopics
from db.utils.profile import get_profile_by_user_id
from db.utils.topic import get_topic, create_topic_no_commit, get_topic_with_users


async def edit_topics(topics_data: EditTopics, user_id: int, session: AsyncSession):
    user = (await session.execute(select(User)
                                  .filter(User.id == user_id).options(selectinload(User.topics)))).scalar_one_or_none()
    list_names_topics = [i['name'] for i in jsonable_encoder(user.topics)]
    for topic_name in topics_data.topics:
        if topic_name not in list_names_topics:
            topic = await get_topic(topic_name, session)
            if not topic:
                topic = await create_topic_no_commit(topic_name, session)
            user.topics.append(topic)
    for topic in user.topics.copy():
        if topic.name not in topics_data.topics:
            user.topics.remove(topic)
    await session.commit()
    return 'ok'


async def get_matching_users(user_id: int, session: AsyncSession):
    #profile = await get_profile_by_user_id(user_id, session)
    users = (await session.execute(select(User, func.count(Profile.topics).label('qwerty'))
                                   .join(User, Topic.users)
                                   .options(selectinload(User.topics))
                                   .filter(User.topics.any(Profile.topics),
                                           Profile.user_id == user_id,
                                           User.id != user_id).group_by(User).order_by(desc('qwerty'))))\
        .scalars().all()
    return users


async def get_user_topics(user_id: int, session: AsyncSession):
    return (await session.execute(select(User).filter(User.id == user_id).options(selectinload(User.topics)))).scalar_one_or_none().topics
