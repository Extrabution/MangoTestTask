import datetime

import sqlalchemy
from pydantic import BaseModel
from db.database import SessionLocal
from db import models
import time


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


def get_user_by_username(username: str):
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


def get_user_chats(user_id) -> list:
    with SessionLocal.begin() as s:
        chats = s.execute(f"select chats.chat_id from chats where {user_id}=ANY(chats.members)")
        if not chats:
            return []
        chat_list = []
        for row in chats:
            chat_list.append(row.chat_id)
        return chat_list


def create_chat(data: list, chat_name: str):
    # data[members, name]
    with SessionLocal.begin() as s:
        chat = models.chats(members=data, name=chat_name, last_message_at=datetime.datetime.now())
        s.add(chat)
        s.flush()
        s.refresh(chat)
        return chat.chat_id


def get_pinned_chats(user_id):
    with SessionLocal.begin() as s:
        pin_chats = s.query(models.users.pin_chats_ids).filter(models.users.user_id == user_id).first()
        print(pin_chats)
        return pin_chats[0]


def pin_chat(user_id, chat_id):
    with SessionLocal.begin() as s:
        s.execute(f"update users set pin_chats_ids = array_append(pin_chats_ids, {chat_id}) where user_id={user_id}")
        s.commit()


def like(message_id, user_id):
    with SessionLocal.begin() as s:
        s.execute(f"""update messages set liked_by_ids = array_append(liked_by_ids, {user_id}) 
        where message_id={message_id} and not {user_id}= any(messages.liked_by_ids)""")
        s.commit()
    with SessionLocal.begin() as s:
        liked_by = s.query(models.messages.liked_by_ids, models.messages.chat_id).filter(models.messages.message_id == message_id).first()
        return liked_by[0], liked_by[1]


def get_chat_usernames_of_users(chat_id) -> list:
    with SessionLocal.begin() as s:
        chat_members = s.execute(f"""select users.phone_number 
                                     from users 
                                     where users.user_id = ANY((select chats.members 
                                                                from chats 
                                                                where chats.chat_id = {chat_id})::bigint[]);""")
        members_list = []
        for row in chat_members:
            members_list.append(row.phone_number)
        return members_list


def get_chat_history(chat_id, page_number):
    with SessionLocal.begin() as s:
        chat_history = s.execute(f"""select * from messages as m
                                     where m.chat_id = {chat_id}
                                     order by m.created_at desc
                                     limit 5 offset {(page_number - 1)*5}""")
        chat_history_arr = []
        for row in chat_history:
            temp = {"message_id": row.message_id, "chat_id": row.chat_id, "author_id": row.author_id,
                    "created_at": str(row.created_at), "message_type": row.message_type, "content": row.message_type ,
                    "liked_by_ids": row.liked_by_ids}
            chat_history_arr.append(temp)
        return chat_history_arr


def new_message(user_id, data: list) -> dict:
    # data[author_id, chat_id, message_type, content]
    with SessionLocal.begin() as s:
        message = models.messages(author_id=user_id, created_at=datetime.datetime.now(),
                                  chat_id=data[0], message_type=data[1], content=data[2],
                                  liked_by_ids=[])
        s.add(message)
        s.flush()
        s.refresh(message)
        return {"author_id": message.author_id, "message_id": message.message_id,
                "created_at": str(message.created_at), "chat_id": message.chat_id,
                "message_type": message.message_type, "content": message.content,
                "liked_by_ids": message.liked_by_ids}


def get_message_chat_id(message_id) -> int:
    with SessionLocal.begin() as s:
        chat_id = s.query(models.messages.chat_id).filter(models.messages.message_id == message_id).first()
        if chat_id is not None:
            return chat_id.chat_id
        else:
            return -1

