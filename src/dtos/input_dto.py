from pydantic import BaseModel
from typing import Union


class SignInDTO(BaseModel):
    username: str
    password: str


class SignUpDTO(BaseModel):
    username: str
    password: str
    photo: str
    about_me: str


class UpdateProfileDTO(BaseModel):
    token: str
    new_about_me: Union[str, None]
    new_photo: Union[str, None]


