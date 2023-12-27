from starlette.requests import Request
from fastapi import FastAPI, status
import os

from src.initializers import webhookSet
from src.initializers import logs_create
from src.tgRequests import serializer
from src.tgRequests import send_message

from const import BACK_PORT
from const import TG_ROUT
from const import INLINE

app = FastAPI()

async def onStartup():
    webhookSet()
    logs_create()

app.add_event_handler("startup", onStartup)

@app.post(f"/{TG_ROUT}", status_code=status.HTTP_200_OK)
async def receive_r(request: Request):
    r = await request.json()
    message = serializer(r)
    print(message)
    send_message(
        chat_id=message.chat_id,
        text = "qq",
        reply_markup=INLINE
    )

    m = serializer(r)
    return 

if __name__ == "__main__":
    uvicorn_cmd = f"uvicorn main:app --host 0.0.0.0 --port {BACK_PORT} --reload"
    os.system(uvicorn_cmd)
