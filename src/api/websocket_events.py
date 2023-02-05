from services.user_service import get_current_user
from db import crud


wb_clients = {}  # sio: username


def register_ws(sio):

    @sio.event
    async def connect(sid, environ, auth):
        global wb_clients
        user = await get_current_user(environ["HTTP_AUTHORIZATION"].split()[1])
        wb_clients[str(sid)] = user.phone_number
        print(wb_clients)
        print(f"{sid}I'm connected!")

    @sio.event
    def disconnect(sid):
        global wb_clients
        del wb_clients[str(sid)]
        print('disconnected ', sid)

    @sio.on('send_message')
    async def send_message(sid, data):
        """
        :param sid:
        :param data: List of parameters  [author_id, chat_id, message_type, content]
        """
        global wb_clients
        message = crud.new_message(data)
        # TODO: затестить на 2 клиентах
        members = crud.get_chat_users(message["chat_id"])
        sids = []
        for phone_number in members:
            try:
                sids.append(list(wb_clients.keys())[list(wb_clients.values()).index(phone_number)])
            except:
                pass
        for sid in sids:
            await sio.emit("new_message", message,
                           room=sid)

    @sio.on('pin_chats')
    async def pin_chats(sid):
        global wb_clients
        user = crud.get_user_by_username(wb_clients[str(sid)])
        await sio.emit("user_pin_chats", crud.get_pinned_chats(user.user_id), room=sid)

    @sio.on('pin_chat')
    async def pin_chat(sid, chat_id):
        global wb_clients
        user = crud.get_user_by_username(wb_clients[str(sid)])
        crud.pin_chat(user.user_id, chat_id)

    @sio.on("view_chats")
    async def view_chats(sid):
        global wb_clients
        user = crud.get_user_by_username(wb_clients[str(sid)])
        await sio.emit("view_chats_list", crud.get_user_chats(user.user_id), room=sid)

    @sio.on("new_chat")
    async def new_chat(sid, data):
        """
        :param sid:
        :param data: List of parameters  [members, chat_name]
        """
        global wb_clients
        new_chat_id = crud.create_chat(data)
        # TODO: затестить на 2 клиентах
        members = crud.get_chat_users(new_chat_id)
        sids = []
        for phone_number in members:
            try:
                sids.append(list(wb_clients.keys())[list(wb_clients.values()).index(phone_number)])
            except:
                pass
        for sid in sids:
            await sio.emit("new_chat_created", new_chat_id,
                           room=sid)

    @sio.on("like")
    async def like(sid, message_id):
        global wb_clients
        user = crud.get_user_by_username(wb_clients[str(sid)])
        liked_by, chat_id = crud.like(message_id, user.user_id)
        print(liked_by, chat_id)
        # TODO: затестить на 2 клиентах
        members = crud.get_chat_users(chat_id)
        sids = []
        for phone_number in members:
            try:
                sids.append(list(wb_clients.keys())[list(wb_clients.values()).index(phone_number)])
            except:
                pass
        for sid in sids:
            await sio.emit("liked_by", [liked_by, message_id, chat_id],
                           room=sid)

    @sio.on("get_chat_history")
    async def like(sid, data):
        history = crud.get_chat_history(data[0], data[1] if data[1] != 0 else 1)
        await sio.emit("chat_history", history)
