# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Jun 22 2022, 20:18:18) 
# [GCC 9.4.0]
# Embedded file name: /mnt/c/Users/Xtrabatya/Desktop/InnopolisITP/PythonProjects/MangoTestovoe/src/db/models.py
# Compiled at: 2023-02-01 04:03:21
# Size of source mod 2**32: 360 bytes
from sqlalchemy import Column, Integer, String, ARRAY
from db.db import Base

class users(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, index=True)
    phone_number = Column(String, unique=True)
    password = Column(String)
    about_me = Column(String)
    pin_chat_ids = Column(ARRAY(Integer))
# okay decompiling models.cpython-38.pyc
