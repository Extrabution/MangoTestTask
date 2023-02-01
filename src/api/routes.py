from __future__ import annotations
from fastapi import Form
from services.user_service import *
from dtos.user_dto import *
from converters.user_converter import *


def register(app):
    @app.get('/')
    async def index():
        return 'Hello!'

    @app.post('/signin', response_model=UserWithTokensDTO)
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

    @app.post('/signup', response_model=UserWithTokensDTO)
    async def signup(username=Form(), password=Form(), photo=Form(), about_me=Form()):
        user = crud.get_user(username)
        if user:
            return {'access_token': '', 'token_type': ''}
        crud.register_user(phone_number=username, password=(get_password_hash(password)), about_me=about_me)
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(data={'sub': username},
                                           expires_delta=access_token_expires)
        print(username, password, access_token)
        await convert_and_save_photo(photo, username)
        return {**{'access_token':access_token,  'token_type':'bearer'}, **(convert_user_to_dto(user))}

    @app.put('/profile')
    async def edit_profile(token: str = Form(), new_about_me: str = Form(), new_photo: str = Form()):
        user = await get_current_user(token)
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail='Invalid or expired token',
                                headers={'WWW-Authenticate': 'Bearer'})
        crud.change_profile(user.phone_number, new_about_me)
        await convert_and_save_photo(new_photo, user.phone_number)
        return {'Status': 'Success'}

    @app.get('/user{user_id}', response_model=UserDTO)
    async def get_user(user_id):
        user = crud.get_user_by_id(user_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='User not found')
        return convert_user_to_dto(user)
