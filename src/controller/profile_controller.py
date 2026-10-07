from fastapi import APIRouter
from src.constants.constants import PROFILE_API_TAG, PROFILE_API_URL
from src.model.profile_model import UserProfileRq
from src.service.profile_service import create_profile

profile_router = APIRouter(
    prefix=PROFILE_API_URL,
    tags=[PROFILE_API_TAG]
)


@profile_router.get("")
async def find_all():
    return []


@profile_router.post("")
async def create_user(user_profile_rq: UserProfileRq):
    return await create_profile(user_profile_rq=user_profile_rq)
