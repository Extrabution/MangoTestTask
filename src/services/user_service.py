# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Jun 22 2022, 20:18:18) 
# [GCC 9.4.0]
# Embedded file name: /mnt/c/Users/Xtrabatya/Desktop/InnopolisITP/PythonProjects/MangoTestovoe/src/services/user_service.py
# Compiled at: 2023-02-01 04:13:50
# Size of source mod 2**32: 2650 bytes
from __future__ import annotations
from datetime import datetime, timedelta
from typing import Union
import jwt
from fastapi import HTTPException, status
from db import crud
import io, base64
from PIL import Image
from converters.user_converters import *
from config import *
from utils import pwd_context

def verify_password(password, hashed_password):
    print(password, hashed_password)
    print(get_password_hash(password))
    return     return pwd_context.verify(password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def authenticate_user(phone_number: 'str', password: 'str') -> 'User | None':
    user = crud.find_user(crud.by_phone_number_spec(phone_number))
    if not user:
        return
    else:
        return verify_password(password, user.password) or None
    return user


def create_access_token(data: 'dict', expires_delta: 'Union[timedelta, None]'=None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: 'str'):
    credentials_exception = HTTPException(status_code=(status.HTTP_401_UNAUTHORIZED),
      detail='Could not validate credentials',
      headers={'WWW-Authenticate': 'Bearer'})
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        phone_number = payload.get('sub')
        if phone_number is None:
            raise credentials_exception
    except:
        raise credentials_exception
    else:
        user = crud.get_user(phone_number)
        if user is None:
            raise credentials_exception
        return user


async def resize_photo(img, size):
    buffer = io.BytesIO()
    new_img = img.resize((size, size))
    new_img.save(buffer, format='jpeg')
    return buffer.getvalue()


async def convert_and_save_photo(photo: 'str', username: 'str'):
    print('Ргшдщ')
    photo = base64.b64decode(photo)
    img = Image.open(io.BytesIO(photo)).convert('RGB')
    with open(f"static/{username}_original.jpeg", 'wb') as (f):
        f.write(photo)
    with open(f"static/{username}_50.jpeg", 'wb') as (f):
        f.write(await resize_photo(img, 50))
    with open(f"static/{username}_100.jpeg", 'wb') as (f):
        f.write(await resize_photo(img, 100))
    with open(f"static/{username}_400.jpeg", 'wb') as (f):
        f.write(await resize_photo(img, 400))
# okay decompiling user_service.cpython-38.pyc
