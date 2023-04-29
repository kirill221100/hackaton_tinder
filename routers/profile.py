from fastapi import APIRouter, Depends
from validation.profile import ProfileValidation
from validation.profile import ProfileEdit
from sqlalchemy.ext.asyncio import AsyncSession
from db.db_setup import get_session
from security.oauth import get_current_user
from db.utils.profile import create_profile, get_profile_by_id, delete_profile, edit_profile, get_matching_profiles, get_profile_by_user_id
from db.utils.profile import get_matching_profiles

profile_router = APIRouter()


@profile_router.post('/create-profile')
async def create_profile_path(profile_data: ProfileValidation, user_data=Depends(get_current_user),
                              session: AsyncSession = Depends(get_session)):
    return await create_profile(profile_data, user_data['id'], session)


@profile_router.get('/get-profile-by-id/{profile_id}')
async def get_profile_by_id_path(profile_id: int, session: AsyncSession = Depends(get_session)):
    return await get_profile_by_id(profile_id, session)


@profile_router.patch('/edit-profile')
async def edit_profile_path(edit_data: ProfileEdit, user=Depends(get_current_user),
                            session: AsyncSession = Depends(get_session)):
    return await edit_profile(edit_data, user['id'], session)


@profile_router.get('/get-matching-profiles')
async def get_matching_profiles_path(user_data=Depends(get_current_user), session: AsyncSession = Depends(get_session)):
    return await get_matching_profiles(user_data['id'], session)


@profile_router.delete('/delete-profile-by-id/{profile_id}')
async def delete_profile_path(profile_id: int, user_data=Depends(get_current_user),
                              session: AsyncSession = Depends(get_session)):
    return await delete_profile(profile_id, user_data, session)


@profile_router.get('/get-profile-of-current-user')
async def get_profile_of_current_user_path(user=Depends(get_current_user), session: AsyncSession = Depends(get_session)):
    return await get_profile_by_user_id(user['id'], session)


# @profile_router.get('/req_to_user/{user_id}')
# async def req_to_user_path(user_id: int, current_user=Depends(get_current_user), session: AsyncSession = Depends(get_session)):
#     return await req_to_user(user_id, current_user['id'], session)
