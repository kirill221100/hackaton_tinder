from fastapi import APIRouter, Depends
from validation.profile import ProfileValidation
from validation.profile import ProfileEdit
from sqlalchemy.ext.asyncio import AsyncSession
from db.db_setup import get_session
from security.oauth import get_current_user
from db.utils.profile import create_profile, get_profile_by_id, delete_profile, edit_profile, get_matching_profiles, get_profile_by_user_id
from db.utils.profile import get_matching_profiles

request_router = APIRouter()