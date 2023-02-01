# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Jun 22 2022, 20:18:18) 
# [GCC 9.4.0]
# Embedded file name: /mnt/c/Users/Xtrabatya/Desktop/InnopolisITP/PythonProjects/MangoTestovoe/src/dtos/user_dto.py
# Compiled at: 2023-02-01 02:16:53
# Size of source mod 2**32: 319 bytes
from pydantic import BaseModel

class PhotosDTO(BaseModel):
    p50: str
    p100: str
    p400: str
    original: str


class UserDTO(BaseModel):
    user_id: int
    about_me: str
    username: str
    photos: PhotosDTO


class UserWithTokensDTO(UserDTO):
    access_token: str
    token_type: str
# okay decompiling user_dto.cpython-38.pyc
