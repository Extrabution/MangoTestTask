from pydantic import BaseModel
from db.database import SessionLocal
from db import models


class User(BaseModel):
    user_id: int
    phone_number: str
    password: str
    about_me: str
    pin_chats_ids: list


def find_user(spec):
    with SessionLocal.begin() as s:
        user = s.query(models.users).filter(spec).first()
        if not user:
            return None
        return User(user_id=user.user_id, phone_number=user.phone_number,
                    about_me=user.about_me, pin_chats_ids=user.pin_chats_ids,
                    password=user.password)


def get_user_by_id(user_id):
    return find_user(models.users.user_id == user_id)


def get_user(username: str):
    return find_user(models.users.phone_number == username)


def register_user(phone_number: str, password: str, about_me: str):
    with SessionLocal.begin() as s:
        user = models.users(phone_number=phone_number, password=password,
                            about_me=about_me,
                            pin_chats_ids=[])
        s.add(user)
        s.commit()


def change_profile(username: str, new_about_me: str):
    with SessionLocal.begin() as s:
        s.query(models.users).filter(models.users.phone_number == username).update({'about_me': new_about_me})
        s.commit()
