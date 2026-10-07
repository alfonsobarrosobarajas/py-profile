from pydantic import BaseModel, Field

# Request classes


class UserProfileRq(BaseModel):
    user_name: str = Field(min_length=2, max_length=20)
    user_rol: list[UserRolRq]


class UserRolRq(BaseModel):
    rol: str = Field(min_length=2, max_length=20)


# Response classes
class UserProfileRs(BaseModel):
    user_name: str = Field(min_length=2, max_length=20)
    user_rol: list[UserRolRs]


class UserRolRs(BaseModel):
    rol: str = Field(min_length=2, max_length=20)
