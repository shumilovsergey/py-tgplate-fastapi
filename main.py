from starlette.requests import Request
import json
from fastapi import FastAPI, status
from types import SimpleNamespace
import os

from src.initializers import webhookSet
from src.tgRequests import serializer
from src.tgRequests import send_message
from src.tgRequests import inline_keyboard_generator

from const import BACK_PORT
from const import TG_ROUT
from const import Message


app = FastAPI()

async def onStartup():
    webhookSet()

app.add_event_handler("startup", onStartup)

@app.post(f"/{TG_ROUT}", status_code=status.HTTP_200_OK)
async def receive_r(request: Request):
    r = await request.json()
    m = serializer(r)



    
    return 

if __name__ == "__main__":
    uvicorn_cmd = f"uvicorn main:app --host 0.0.0.0 --port {BACK_PORT} --reload"
    os.system(uvicorn_cmd)