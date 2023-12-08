from starlette.requests import Request
from fastapi import FastAPI
import os

from src.initializers import webhookSet
from src.tgRequests import serializer

from const import BACK_PORT
from const import TG_ROUT

app = FastAPI()

async def onStartup():
    webhookSet()

app.add_event_handler("startup", onStartup)


@app.get("/")
def read_root():
    return {"Hello": "This is py-tgplate-fastapi"}

@app.post(f"/{TG_ROUT}")
async def receive_r(request: Request):
    r = await request.json()
    message = serializer(r)
    return 

if __name__ == "__main__":
    uvicorn_cmd = f"uvicorn main:app --host 0.0.0.0 --port {BACK_PORT} --reload"
    os.system(uvicorn_cmd)