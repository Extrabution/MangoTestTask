# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Jun 22 2022, 20:18:18) 
# [GCC 9.4.0]
# Embedded file name: /mnt/c/Users/Xtrabatya/Desktop/InnopolisITP/PythonProjects/MangoTestovoe/src/converters/user_converters.py
# Compiled at: 2023-02-01 03:20:09
# Size of source mod 2**32: 544 bytes
from db.crud import User
from config import base_url

def convert_user_to_dto(user: User):
    return {'user_id':user.user_id,  'username':user.phone_number, 
     'about_me':user.about_me, 
     'photos':{'p50':f"{base_url}static/{user.phone_number}_50.jpeg", 
      'p100':f"{base_url}static/{user.phone_number}_100.jpeg", 
      'p400':f"{base_url}static/{user.phone_number}_400.jpeg", 
      'original':f"{base_url}static/{user.phone_number}_original.jpeg"}}
# okay decompiling user_converters.cpython-38.pyc
