from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from sqlalchemy import select, func, desc
from fastapi import HTTPException
import json
from db.models.req import ProfileReq, ProfileReqBack

from db.utils.user import get_user_by_id, get_user_by_id_with_prof_req
from db.utils.profile import get_profile_by_user_id, get_profile_by_user_id_with_quiz, get_profile_by_id_with_quiz, get_profile_by_id

from typing import List


async def create_request_from_profile(current_user_id: int, user_id: int, session: AsyncSession):
    profile = await get_profile_by_user_id(current_user_id, session)
    user = await get_user_by_id(user_id, session)
    req = ProfileReq(profile_id=profile.id, user=user)
    session.add(req)
    await session.commit()
    return 'ok'


async def create_request_back_to_profile(profile_id: int, user_id: int, session: AsyncSession):
    profile = await get_profile_by_id(profile_id, session)
    req = ProfileReqBack(profile=profile, user_id=user_id)
    session.add(req)
    await session.commit()
    return 'ok'


async def get_req_from_profile(user_id: int, session: AsyncSession):
    return (await session.execute(select(ProfileReq).filter(ProfileReq.user_id == user_id))).scalars().all()


async def answer_on_request_from_profile(req_id: int, user_id: int, session: AsyncSession, answer: bool):
    req = (await session.execute(select(ProfileReq).filter(ProfileReq.id == req_id))).scalar_one_or_none()
    if answer:
        profile = await get_profile_by_id(req.profile_id, session)
        answer = ProfileReqBack(profile=profile, user_id=user_id)
        session.add(answer)
    else:
        await req.delete()
    await session.commit()
    return 'ok'


async def get_answers_on_req_from_user_profile(profile_id: int, session: AsyncSession):
    return (await session.execute(select(ProfileReqBack).filter(ProfileReqBack.profile_id == profile_id))).scalars().all()






