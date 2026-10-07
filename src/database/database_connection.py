from motor.motor_asyncio import AsyncIOMotorClient
from src.environment.environment_loader import load_environment

env = load_environment()
MONGODB_URL = env["mongodb_url"]


def get_database_connection(collection: str) -> AsyncIOMotorClient:
    client = AsyncIOMotorClient(MONGODB_URL)
    return client.user_profile.get_collection(collection)
