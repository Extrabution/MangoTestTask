from sqlalchemy import Column, Integer, String


from db import Base


class users(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    phone_number = Column(String, unique=True)
    password = Column(String)
    photo50 = Column(String)
    photo100 = Column(String)
    photo400 = Column(String)
    photo_original = Column(String)



