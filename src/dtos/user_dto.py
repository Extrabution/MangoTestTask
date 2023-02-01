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


class UserWithTokenDTO(UserDTO):
    access_token: str
    token_type: str
