from src.model.profile_model import UserProfileRq
from src.database.database_connection import get_database_connection


async def create_profile(user_profile_rq: UserProfileRq):
    user_profile_dict = user_profile_rq.model_dump()
    created_id = await get_database_connection("user_profile").insert_one(user_profile_dict)
    return {"id": str(created_id.inserted_id)}
