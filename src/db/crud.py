from pydantic import BaseModel
from db.db import SessionLocal

class User(BaseModel):
    user_id: int
    phone_number: str
    password: str
    about_me: str
    pin_chat_ids: list


# def find_user


def by_phone_number_spec(phone_number):
    return models.users.phone_number == phone_number


# def get_user


#def get_user_by_id


def register_user(phone_number: str, password: str, about_me: str):
    with SessionLocal.begin as (s):
        user = models.users(phone_number=phone_number, password=password,
          about_me=about_me,
          pin_chat_ids=[])
        s.add(user)
        s.commit()


def change_profile(username: str, new_about_me: str):
    with SessionLocal.begin as (s):
        s.querymodels.users.filter(models.users.phone_number == username).update({'about_me': new_about_me})
        s.commit()
