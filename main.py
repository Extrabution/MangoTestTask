from fastapi import FastAPI
import uvicorn
from multiprocessing import cpu_count, freeze_support
from pydantic import BaseModel
import socketio


app = FastAPI()
sio = socketio.AsyncServer()
app_sio = socketio.ASGIApp(sio)
app.mount("/", app_sio)

class Client:
    abc = 123




@sio.event
async def connect():
    print("I'm connected!")

@app.get("/")
async def index():
    return {"Hello!"}


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
    start_server(num_workers=num_workers, reload=False, host="127.0.0.1")