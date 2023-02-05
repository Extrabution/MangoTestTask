from __future__ import annotations
from fastapi import Form
from services.user_service import *
from dtos.user_dto import *
from converters.user_converters import *
from typing import Union


def register(app):
    @app.get('/')
    async def index():
        return 'Hello!'

    @app.post('/signin', response_model=UserWithTokenDTO)
    async def signin(username: str = Form(), password: str = Form()):
        user = authenticate_user(username, password)
        if not user:
            raise HTTPException(status_code=(status.HTTP_401_UNAUTHORIZED),
                                detail='Incorrect username or password',
                                headers={'WWW-Authenticate': 'Bearer'})
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        print(access_token_expires)
        access_token = create_access_token(data={'sub': user.phone_number},
                                           expires_delta=access_token_expires)
        print('!!!!!!')
        return {'access_token': access_token, 'token_type': 'bearer',
                **convert_user_to_dto(user)}

    @app.post('/signup', response_model=UserWithTokenDTO)
    async def signup(username=Form(), password=Form(), photo=Form(), about_me=Form()):
        user = crud.get_user_by_username(username)
        if user:
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                detail='Phone number is already in use')
        crud.register_user(phone_number=username, password=(get_password_hash(password)), about_me=about_me)
        user = crud.get_user_by_username(username)
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(data={'sub': username},
                                           expires_delta=access_token_expires)
        print(username, password, access_token)
        convert_and_save_photo(photo, username)
        return {'access_token': access_token,  'token_type': 'bearer', **(convert_user_to_dto(user))}

    @app.put('/profile')
    async def edit_profile(token: str = Form(), new_about_me: str = Form(), new_photo: str = Form()):
        # токен через хедер
        user = await get_current_user(token)
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail='Invalid or expired token',
                                headers={'WWW-Authenticate': 'Bearer'})
        if new_photo != "None":
            convert_and_save_photo(new_photo, user.phone_number)
        if new_about_me != "None":
            crud.change_profile(user.phone_number, new_about_me)
        return {'Status': 'Success'}

    @app.get('/user{user_id}', response_model=UserDTO)
    async def get_user(user_id):
        user = crud.get_user_by_id(user_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='User not found')
        return convert_user_to_dto(user)
