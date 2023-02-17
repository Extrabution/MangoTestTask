from __future__ import annotations

from datetime import timedelta

from services.user_service import authenticate_user, create_access_token, \
    convert_and_save_photo, get_password_hash, get_current_user
from dtos.user_dto import UserWithTokenDTO, UserDTO
from converters.user_converters import convert_user_to_dto
from dtos.input_dto import SignInDTO, SignUpDTO, UpdateProfileDTO
from config import ACCESS_TOKEN_EXPIRE_MINUTES
from fastapi import HTTPException, status
import db.crud as crud

def register(app):
    @app.get('/')
    async def index():
        return 'Hello!'

    @app.post('/signin', response_model=UserWithTokenDTO)
    async def signin(data : SignInDTO):
        user = authenticate_user(data.username, data.password)
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail='Incorrect username or password',
                                headers={'WWW-Authenticate': 'Bearer'})
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(data={'sub': user.phone_number},
                                           expires_delta=access_token_expires)
        return {'access_token': access_token, 'token_type': 'bearer',
                **convert_user_to_dto(user)}

    @app.post('/signup', response_model=UserWithTokenDTO)
    async def signup(data: SignUpDTO):
        user = crud.get_user_by_username(data.username)
        if user:
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                detail='Phone number is already in use')
        crud.register_user(phone_number=data.username, password=(get_password_hash(data.password)),
                           about_me=data.about_me)
        user = crud.get_user_by_username(data.username)
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(data={'sub': data.username},
                                           expires_delta=access_token_expires)
        convert_and_save_photo(data.photo, data.username)
        return {'access_token': access_token,  'token_type': 'bearer', **(convert_user_to_dto(user))}

    @app.put('/profile')
    async def edit_profile(data: UpdateProfileDTO):
        print(data)
        user = await get_current_user(data.token)
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail='Invalid or expired token',
                                headers={'WWW-Authenticate': 'Bearer'})
        if data.new_photo is not None:
            convert_and_save_photo(data.new_photo, user.phone_number)
        if data.new_about_me is not None:
            crud.change_profile(user.phone_number, data.new_about_me)
        return {'Status': 'Success'}

    @app.get('/user{user_id}', response_model=UserDTO)
    async def get_user(user_id):
        user = crud.get_user_by_id(user_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='User not found')
        return convert_user_to_dto(user)
