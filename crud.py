from pydantic import BaseModel
from typing import Union

import models
from db import SessionLocal


class User(BaseModel):
    user_id: int
    phone_number: Union[str, None] = None
    password: Union[str, None] = None
    photo50: Union[str, None] = None
    photo100: Union[str, None] = None
    photo400: Union[str, None] = None
    photo_original: Union[str, None] = None


def get_user(phone_number: str):
    with SessionLocal.begin() as s:
        result = s.query(models.users).filter(models.users.phone_number == phone_number).first()
        if not result:
            return False
        user = User(user_id=result.user_id, phone_number=result.phone_number,
                    password=result.password, photo50=result.photo50,
                    photo100=result.photo100, photo400=result.photo400,
                    photo_original=result.photo_original)
    return user

def register_user(phone_number: str, password:str, photo50:str, photo100:str, photo400:str, photo_original:str):
    with SessionLocal.begin() as s:
        pass