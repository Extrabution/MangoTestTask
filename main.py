from fastapi import FastAPI, Depends, status, HTTPException, Form
import uvicorn
from multiprocessing import cpu_count, freeze_support
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from passlib.context import CryptContext
from typing import Union
import jwt
import socketio
import crud
from db import SessionLocal, engine


app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
sio = socketio.AsyncServer(async_mode='asgi', logger=True, engineio_logger=True)
app_sio = socketio.ASGIApp(sio, app, socketio_path="/socket")
sio.attach(app, socketio_path="socket")

#app.mount("/", app_sio)

SECRET_KEY = "c50282a35faaef90486277d0ceea7635391ba3b55ba1a5157c1f680785c05e91"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Token(BaseModel):
    access_token: str
    token_type: str


class User(BaseModel):
    user_id: int
    phone_number: Union[str, None] = None
    password: Union[str, None] = None
    photo50: Union[str, None] = None
    photo100: Union[str, None] = None
    photo400: Union[str, None] = None
    photo_original: Union[str, None] = None


def verify_password(password, hashed_password):
    print(password, hashed_password)
    print(get_password_hash(password))
    return pwd_context.verify(password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def authenticate_user(phone_number: str, password: str):
    user = crud.get_user(phone_number)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        phone_number: str = payload.get("sub")
        if phone_number is None:
            raise credentials_exception
    except:
        raise credentials_exception

    user = crud.get_user(phone_number)
    if user is None:
        raise credentials_exception
    return user


@sio.event
async def connect(sid, environ, auth):
    print(f"{sid}I'm connected!")


@sio.on("register")
async def register(sid, data):
    print(f"register {sid}", data)


@app.get("/")
async def index():
    return "Hello!"


@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    print(access_token_expires)
    access_token = create_access_token(
        data={"sub": user.phone_number}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/signup")
async def login_for_access_token(username: str = Form(), password: str = Form()):
    user = crud.get_user(username)
    if user:
        return {"Success": False, "detail": "User already exists"}



def start_server(host="127.0.0.1",
                 port=8000,
                 num_workers=4,
                 loop="asyncio",
                 reload=False):
    uvicorn.run("main:app",
                host=host,
                port=port,
                workers=num_workers,
                loop=loop,
                reload=reload)


if __name__ == "__main__":
    freeze_support()
    num_workers = int(cpu_count() * 0.75)
    start_server(num_workers=1, reload=False, host="127.0.0.1")