from dotenv import load_dotenv
from pydantic import BaseModel
import os
import json


#LOAD DOT ENV
load_dotenv()
TG_APP = os.getenv("TG_APP")
TG_TOKEN = os.getenv("TG_TOKEN")
TG_WEBHOOK_URL = os.getenv("TG_WEBHOOK_URL")
TG_ROUT = os.getenv("TG_ROUT")
BACK_PORT = os.getenv("BACK_PORT")

#HARDCODE CONSTS
TG_URL = f"https://api.telegram.org/bot{TG_TOKEN}"

#KEYBOARDS
INLINE_APP = {
    'inline_keyboard': [
        [
            {'text': 'Магазинчик Шумилова', 'url': 'https://t.me/sh_musicGym_bot/shop24x7'}
        ]
    ]
}

from typing import Any
from dataclasses import dataclass
import json
@dataclass
class Message:
    message_id: int
    id: int
    first_name: str
    last_name: str
    username: str
    text: str

    @staticmethod
    def from_dict(obj: Any) -> 'Message':
        _message_id = int(obj.get("message_id"))
        _id = int(obj.get("id"))
        _first_name = str(obj.get("first_name"))
        _last_name = str(obj.get("last_name"))
        _username = str(obj.get("username"))
        _text = str(obj.get("text"))
        return Message(_message_id, _id, _first_name, _last_name, _username, _text)
