from services.user_service import get_current_user, user_allowed_to_chat
from db import crud


wb_clients = {}  # sio: username


def register_ws(sio):

    @sio.event
    async def connect(sid, environ, auth):
        global wb_clients
        user = await get_current_user([value for (name, value) in environ['asgi.scope']['headers'] if name == b'authorization'][0])
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
        :param data: List of parameters  [chat_id, message_type, content]
        """
        global wb_clients
        user = crud.get_user_by_username(wb_clients[str(sid)])
        chats = crud.get_user_chats(user.user_id)
        print(chats, user.user_id)
        if data[0] not in chats:
            return "Denied"
        message = crud.new_message(user.user_id, data)
        # TODO: затестить на 2 клиентах
        members = crud.get_chat_usernames_of_users(message["chat_id"])
        sids = []
        for phone_number in members:
            try:
                sids.append(list(wb_clients.keys())[list(wb_clients.values()).index(phone_number)])
            except:
                pass
        for sid in sids:
            await sio.emit("new_message", message,
                           room=sid)
        return "OK"

    @sio.on('pin_chats')
    async def pin_chats(sid, x):
        # TODO Убрать x
        global wb_clients
        user = crud.get_user_by_username(wb_clients[str(sid)])
        await sio.emit("user_pin_chats", crud.get_pinned_chats(user.user_id), room=sid)

    @sio.on('pin_chat')
    async def pin_chat(sid, chat_id):
        global wb_clients
        user = crud.get_user_by_username(wb_clients[str(sid)])
        chats = crud.get_user_chats(user.user_id)
        if int(chat_id) not in chats:
            return "Denied"
        crud.pin_chat(user.user_id, int(chat_id))
        return "OK"

    @sio.on("view_chats")
    async def view_chats(sid, x):
        global wb_clients
        user = crud.get_user_by_username(wb_clients[str(sid)])
        await sio.emit("view_chats_list", crud.get_user_chats(user.user_id), room=sid)

    @sio.on("new_chat")
    async def new_chat(sid, data):
        """
        :param sid:
        :param data: [members, chat_name]
        """
        # принимать номера телефонов, конверить в id, продолжать логику
        global wb_clients
        member_ids = []
        for member in data[0]:
            print(member)
            member_ids.append(crud.get_user_by_username(member).user_id)
        user = crud.get_user_by_username(wb_clients[str(sid)])
        if user.user_id not in member_ids:
            member_ids.append(user.user_id)
        new_chat_id = crud.create_chat(member_ids, data[1])
        # TODO: затестить на 2 клиентах
        members = crud.get_chat_usernames_of_users(new_chat_id)
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
        print(message_id)
        user = crud.get_user_by_username(wb_clients[str(sid)])
        chat_id = crud.get_message_chat_id(int(message_id))
        if chat_id is None:
            print(3)
            return "Denied"
        if not user_allowed_to_chat(user.user_id, chat_id):
            print(4)
            return "Denied"
        liked_by, chat_id = crud.like(int(message_id), user.user_id)
        print(liked_by, chat_id)
        # TODO: затестить на 2 клиентах
        members = crud.get_chat_usernames_of_users(chat_id)
        sids = []
        for phone_number in members:
            try:
                sids.append(list(wb_clients.keys())[list(wb_clients.values()).index(phone_number)])
            except:
                pass
        for sid in sids:
            await sio.emit("liked_by", [liked_by, int(message_id), chat_id],
                           room=sid)
        return "OK"

    @sio.on("get_chat_history")
    async def get_chat_history(sid, data):
        """
        :param data: [chat_id, page]
        :return: OK| Denied
        """
        global wb_clients
        user = crud.get_user_by_username(wb_clients[str(sid)])
        chats = crud.get_user_chats(user.user_id)
        print(chats)
        if data[0] not in chats:
            return "Denied"
        history = crud.get_chat_history(data[0], data[1] if data[1] != 0 else 1)
        await sio.emit("chat_history", history)
        return 'OK'
