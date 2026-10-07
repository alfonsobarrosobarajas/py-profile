from motor.motor_asyncio import AsyncIOMotorClient
from environment.environment_loader import load_environment

env = load_environment()
MONGODB_URL = env["mongodb_url"]


def get_database_connection():
    client = AsyncIOMotorClient(MONGODB_URL)
    database = client.user_profile
