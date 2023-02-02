from sqlalchemy import Column, Integer, String, ARRAY, TIMESTAMP
from db.database import Base


class users(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    phone_number = Column(String, unique=True)
    password = Column(String)
    about_me = Column(String)
    pin_chats_ids = Column(ARRAY(Integer))


class chats(Base):
    __tablename__ = "chats"
    chat_id = Column(Integer, primary_key=True, index=True)
    members = Column(ARRAY(Integer))
    name = Column(String)
    last_message_at = Column(TIMESTAMP)


class messages(Base):
    __tablename__ = "messages"
    message_id = Column(Integer, primary_key=True, index=True)
    chat_id = Column(Integer)
    author_id = Column(Integer)
    created_at = Column(TIMESTAMP)
    message_type = Column(String)
    content = Column(String)
    liked_by_ids = Column(ARRAY(Integer))
