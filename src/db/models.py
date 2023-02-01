from sqlalchemy import Column, Integer, String, ARRAY
from db.database import Base


class users(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    phone_number = Column(String, unique=True)
    password = Column(String)
    about_me = Column(String)
    pin_chats_ids = Column(ARRAY(Integer))

