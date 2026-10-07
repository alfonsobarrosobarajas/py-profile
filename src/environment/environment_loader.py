from dotenv import dotenv_values
import os


def load_environment():
    environment = os.getenv("ENVIRONMENT").casefold()
    env_file = f".env.{environment}"
    return dotenv_values(env_file)
