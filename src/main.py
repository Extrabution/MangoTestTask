# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Jun 22 2022, 20:18:18) 
# [GCC 9.4.0]
# Embedded file name: /mnt/c/Users/Xtrabatya/Desktop/InnopolisITP/PythonProjects/MangoTestovoe/src/main.py
# Compiled at: 2023-02-01 03:21:58
# Size of source mod 2**32: 1098 bytes
from __future__ import annotations
from fastapi import FastAPI
import uvicorn
from multiprocessing import cpu_count, freeze_support
from fastapi.staticfiles import StaticFiles
from api.routes import register
from api.websocket_events import register_ws
import socketio
app = FastAPI()
app.mount('/static', StaticFiles(directory='../static'), name='static')
sio = socketio.AsyncServer(async_mode='asgi', logger=True, engineio_logger=True)
app_sio = socketio.ASGIApp(sio, app)
app.mount('/ws', app_sio)
register(app)
register_ws(sio)

def main():
    freeze_support()
    num_workers = int(cpu_count() * 0.75)
    start_server(num_workers=1, reload=False, host='127.0.0.1')


def start_server(host='127.0.0.1', port=8000, num_workers=4, loop='asyncio', reload=False):
    uvicorn.run('main:app', host=host,
      port=port,
      workers=num_workers,
      loop=loop,
      reload=reload)


if __name__ == '__main__':
    main()
# okay decompiling main.cpython-38.pyc
