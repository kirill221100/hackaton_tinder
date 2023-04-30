from fastapi import APIRouter, Depends
from validation.user import EditTopics
from sqlalchemy.ext.asyncio import AsyncSession
from db.db_setup import get_session
from security.oauth import get_current_user
from db.utils.user import edit_topics, get_matching_users, get_user_topics, get_user_by_id, edit_contacts, edit_about

user_router = APIRouter()


@user_router.get('/get-user-by-id/{user_id}')
async def get_user_by_id_path(user_id: int,
                              session: AsyncSession = Depends(get_session)):
    return await get_user_by_id(user_id, session)


@user_router.get('/get-current-user')
async def get_current_user_path(user_data=Depends(get_current_user), session: AsyncSession = Depends(get_session)):
    return await get_user_by_id(user_data['id'], session)


@user_router.put('/edit-topics')
async def edit_topics_path(topics_data: EditTopics, user_data=Depends(get_current_user),
                           session: AsyncSession = Depends(get_session)):
    return await edit_topics(topics_data, user_data['id'], session)


@user_router.put('/edit-contact')
async def edit_contacts_path(contacts_data: str, user_data=Depends(get_current_user),
                             session: AsyncSession = Depends(get_session)):
    return await edit_contacts(user_data['id'], contacts_data, session)


@user_router.put('/edit-about')
async def edit_about_path(about: str, user_data=Depends(get_current_user),
                          session: AsyncSession = Depends(get_session)):
    return await edit_about(user_data['id'], about, session)


@user_router.get('/get-matching-users')
async def get_matching_users_path(user_data=Depends(get_current_user), session: AsyncSession = Depends(get_session)):
    return await get_matching_users(user_data['id'], session)


@user_router.get('/get-user-topics')
async def get_user_topics_path(user_data=Depends(get_current_user), session: AsyncSession = Depends(get_session)):
    return await get_user_topics(user_data['id'], session)
