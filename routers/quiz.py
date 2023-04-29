from fastapi import APIRouter, Depends
from validation.quiz import QuizValidation
from sqlalchemy.ext.asyncio import AsyncSession
from db.db_setup import get_session
from security.oauth import get_current_user
from db.utils.user import edit_topics, get_matching_users, get_user_topics, get_user_by_id, edit_contacts, edit_about
from db.utils.quiz import create_quiz, get_quiz_by_profile_id, get_profile_by_user_id_with_quiz, get_quiz_by_user_id

quiz_router = APIRouter()


@quiz_router.post('/create-quiz')
async def create_quiz_path(quiz: QuizValidation, user=Depends(get_current_user),
                           session: AsyncSession = Depends(get_session)):
    return await create_quiz(quiz, user['id'], session)


@quiz_router.get('/get-quiz-by-profile-id')
async def get_quiz_by_profile_id_path(profile_id: int,
                                      session: AsyncSession = Depends(get_session)):
    return await get_quiz_by_profile_id(profile_id, session)


@quiz_router.get('/get-quiz-of-current-user')
async def get_quiz_by_user_id_path(user_id: int,
                                   session: AsyncSession = Depends(get_session)):
    return await get_quiz_by_user_id(user_id, session)
