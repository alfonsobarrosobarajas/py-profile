from fastapi import FastAPI
from src.controller.profile_controller import profile_router

app = FastAPI()


app.include_router(profile_router)
