import time

import socketio
from asyncio import run


async def main():
    sio = socketio.Client(logger=True)
    sio.connect('http://localhost:8000/', socketio_path="ws/socket.io",
                      headers={"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTY3NTMwMjAzN30.dEDd_dsCiT9I4It-s6wyw9ava8U4Yxw-1GGbGa5Uu8w"})

    sio.emit('send_message', ["Hello!",1])
    sio.disconnect()

run(main())