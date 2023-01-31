import asyncio

import requests
import socketio

sio = socketio.AsyncClient()

@sio.event
async def connect():
    print("I'm connected!")

@sio.event
async def connect_error(data):
    print("The connection failed!")

@sio.event
async def disconnect():
    print("I'm disconnected!")


@sio.on("register")
async def register(data):
    print(f"ahui from me", data)


async def main():
    user_data = {"phone": "+79195609843", "password": "password"}
    await sio.connect('http://localhost:8000/socket')
    print('my sid is', sio.sid)
    for i in range(1):
        await sio.emit(event='register', data={'data': user_data})



if __name__ == "__main__":
    asyncio.run(main())

