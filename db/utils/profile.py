from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from sqlalchemy import select, func, desc
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from db.models.user import User
from db.models.profile import Profile
from db.models.topic import Topic
from db.utils.topic import get_topic, create_topic_no_commit
from validation.profile import ProfileValidation, ProfileEdit
from typing import List
from datetime import datetime


async def create_profile(profile_data: ProfileValidation, user_id: int, session: AsyncSession):
    user = (await session.execute(select(User).filter(User.id == user_id))).scalar_one()
    profile = Profile(user=user, name=profile_data.name, text=profile_data.text)
    session.add(profile)
    await session.flush()
    await session.refresh(profile)
    for topic in profile_data.topics:
        topic_db = await get_topic(topic, session)
        if not topic_db:
            topic_db = await create_topic_no_commit(topic, session)
        profile.topics.append(topic_db)
    await session.commit()
    return 'ok'


async def get_profile_by_id(profile_id: int, session: AsyncSession):
    return (await session.execute(select(Profile).filter(Profile.id == profile_id))).scalar_one_or_none()


async def get_profile_by_user_id(user_id: int, session: AsyncSession):
    return (await session.execute(select(Profile).filter(Profile.user_id == user_id))).scalar_one_or_none()


async def get_profile_by_user_id_with_user_req(user_id: int, session: AsyncSession):
    return (await session.execute(select(Profile).filter(Profile.user_id == user_id)
                                  .options(selectinload(Profile.user_reqs)))).scalar_one_or_none()


async def get_profile_by_id_with_quiz(profile_id: int, session: AsyncSession):
    return (await session.execute(select(Profile).filter(Profile.id == profile_id)
                                  .options(selectinload(Profile.quiz)))).scalar_one_or_none()


async def get_profile_by_user_id_with_quiz(user_id: int, session: AsyncSession):
    return (await session.execute(select(Profile).filter(Profile.user_id == user_id)
                                  .options(selectinload(Profile.quiz)))).scalar_one_or_none()


async def delete_profile(profile_id: int, user_data: dict, session: AsyncSession):
    profile = (await session.execute(select(Profile).filter(Profile.id == profile_id))).scalar_one_or_none()
    if user_data['id'] == profile.user_id:
        await session.delete(profile)
        await session.commit()
        return 'ok'
    raise HTTPException(status_code=400, detail='This is not your profile')


async def edit_profile(edit_data: ProfileEdit, user_id: int, session: AsyncSession):
    profile = await get_profile_by_user_id(user_id, session)
    if edit_data.text:
        profile.text = edit_data.text
    if edit_data.topics:
        await edit_profile_topics(profile, edit_data.topics, session)
    await session.commit()
    return 'ok'


async def update_last_time_read(user_id: int, session: AsyncSession):
    profile = await get_profile_by_user_id(user_id, session)
    profile.last_time_read = datetime.now()
    await session.commit()
    return 'ok'


async def get_matching_profiles(user_id: int, session: AsyncSession):
    profiles = (await session.execute(select(Profile, func.count(User.topics).label('qwerty'))
                                      .join(Profile, Topic.profiles)
                                      .filter(Profile.topics.any(User.topics),
                                              User.id == user_id,
                                              Profile.user_id != user_id).group_by(Profile).order_by(desc('qwerty'))))\
        .scalars().all()
    return profiles


async def edit_profile_topics(profile: Profile, topics_data: List[str], session: AsyncSession):
    list_names_topics = [i['name'] for i in jsonable_encoder(profile.topics)]
    for topic_name in topics_data:
        if topic_name not in list_names_topics:
            topic = await get_topic(topic_name, session)
            if not topic:
                topic = await create_topic_no_commit(topic_name, session)
            profile.topics.append(topic)
    for topic in profile.topics.copy():
        if topic.name not in topics_data:
            profile.topics.remove(topic)
    return 'ok'
