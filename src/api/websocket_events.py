import socketio
from services.user_service import get_current_user
wb_clients = {} # sio: username


def register_ws(sio):

    @sio.event
    async def connect(sid, environ, auth):
        print(str(sid))
        print(auth, environ["HTTP_AUTHORIZATION"])
        wb_clients[str(sid)] = await get_current_user(environ["HTTP_AUTHORIZATION"].split()[1])
        print(f"{sid}I'm connected!")

    @sio.event
    def disconnect(sid):
        del wb_clients[str(sid)]
        print('disconnected ', sid)

    @sio.on('send_message')
    async def send_message(sid, data):
        print(f"message from {sid} to {data[0]}", data[1])

    @sio.on('pin_chats')
    async def pin_chats(sid):
        pass

    @sio.on("view_chats")
    async def view_chats(sid):
        pass

    @sio.on("new_chat")
    async def new_chat(sid, users: list):
        pass

    @sio.on("like")
    async def like(sid, message_id):
        pass




