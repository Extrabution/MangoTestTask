import time

import socketio
from asyncio import run

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTY3NTY1MTcyNX0.e8IQ-ycBVEca3GDqxWndK2ivdSHlV4Pj5hmbnEcQ6ew"
sio = socketio.Client(logger=False)


@sio.on("new_chat_created")
def new_chat_created(data):
    print("New chat id: ", data)


@sio.on("view_chats_list")
def view_chats_list(data):
    print("User chats: ", data)


@sio.on("user_pin_chats")
def user_pin_chats(data):
    print("User's pinned chats", data)


@sio.on("new_message")
def new_message(data):
    print(f"{data['content']} from {data['author_id']} at {data['created_at']} to {data['chat_id']}. "
          f"Message type {data['message_type']}, liked by {data['liked_by_ids']}")


@sio.on("liked_by")
def liked_by(data):
    print(f"Message {data[1]} in chat {data[2]} liked by {data[0]}")


@sio.on("chat_history")
def chat_history(data):
    print(f"History: \n {data}")


async def main():

    sio.connect('http://localhost:8000/', socketio_path="ws/socket.io",
                      headers={"Authorization": f"Bearer {token}"})

    sio.emit('send_message', [1, 1, "text", "Hello!"])
    sio.emit('view_chats')
    #sio.emit('like', 2)
    #sio.emit('pin_chat', 10)
    sio.emit('pin_chats')
    #sio.emit("new_chat", [[1, 2], "1,2 chat"])
    sio.emit("get_chat_history", [1, 1])
    sio.emit("get_chat_history", [1, 2])
    sio.emit("get_chat_history", [1, 3])

    # sio.disconnect()

run(main())
