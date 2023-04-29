from fastapi import APIRouter, Depends
from validation.profile import ProfileValidation
from validation.profile import ProfileEdit
from sqlalchemy.ext.asyncio import AsyncSession
from db.db_setup import get_session
from security.oauth import get_current_user
from db.utils.profile import create_profile, get_profile_by_id, delete_profile, edit_profile, get_matching_profiles, get_profile_by_user_id
from db.utils.profile import get_matching_profiles
from db.utils.req import create_request_from_profile, get_req_from_profile, answer_on_request_from_profile, get_answers_on_req_from_user_profile

request_router = APIRouter()


@request_router.get('/request-to-user-by-id/{user_id}')
async def request_from_profile_to_user_by_id_path(user_id: int, current_user=Depends(get_current_user),
                                     session: AsyncSession = Depends(get_session)):
    return await create_request_from_profile(current_user['id'], user_id, session)


@request_router.get('/get-req-from-profile')
async def get_req_from_profile_path(current_user=Depends(get_current_user),
                                    session: AsyncSession = Depends(get_session)):
    return await get_req_from_profile(current_user['id'], session)


@request_router.get('/answer-on-req-from-profile')
async def answer_on_req_from_profile_path(req_id: int, answer: bool, current_user=Depends(get_current_user),
                                    session: AsyncSession = Depends(get_session)):
    return await answer_on_request_from_profile(req_id, current_user['id'], session, answer)



@request_router.get('/get-answers-on-req-from-user-profile')
async def get_answers_on_req_from_user_profile_path(profile_id: int,
                                    session: AsyncSession = Depends(get_session)):
    return await get_answers_on_req_from_user_profile(profile_id, session)
