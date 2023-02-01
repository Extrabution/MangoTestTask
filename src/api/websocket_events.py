import socketio


def register_ws(sio):

    @sio.event
    async def connect(sid, environ, auth):
        print(f"{sid}I'm connected!")

    @sio.on('register')
    async def register(sid, data):
        print(f"register {sid}", data)
