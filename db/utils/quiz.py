from sqlalchemy.ext.asyncio import AsyncSession
from db.models.quiz import Quiz
from db.utils.profile import get_profile_by_user_id, get_profile_by_user_id_with_quiz, get_profile_by_id_with_quiz
from validation.quiz import QuizValidation


async def create_quiz(quiz_data: QuizValidation, user_id: int, session: AsyncSession):
    profile = await get_profile_by_user_id(user_id, session)
    quiz = Quiz(profile=profile, questions=[i.dict() for i in quiz_data.questions])
    session.add(quiz)
    await session.commit()
    return 'ok'


async def get_quiz_by_user_id(user_id: int, session: AsyncSession):
    profile = await get_profile_by_user_id_with_quiz(user_id, session)
    return profile.quiz


async def get_quiz_by_profile_id(profile_id: int, session: AsyncSession):
    profile = await get_profile_by_id_with_quiz(profile_id, session)
    return profile.quiz
