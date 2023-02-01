# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Jun 22 2022, 20:18:18) 
# [GCC 9.4.0]
# Embedded file name: /mnt/c/Users/Xtrabatya/Desktop/InnopolisITP/PythonProjects/MangoTestovoe/src/api/websocket_events.py
# Compiled at: 2023-02-01 03:06:28
# Size of source mod 2**32: 248 bytes
import socketio

def register_ws(sio):

    @sio.event
    async def connect(sid, environ, auth):
        print(f"{sid}I'm connected!")

    @sio.on('register')
    async def register(sid, data):
        print(f"register {sid}", data)
# okay decompiling websocket_events.cpython-38.pyc
