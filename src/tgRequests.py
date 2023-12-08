from const import TG_URL
import json
import requests
from pydantic import BaseModel
from pydantic import ValidationError

from const import INLINE


class Message(BaseModel):
    chat_id: str 
    message_id: str 
    first_name: str = None
    last_name: str = None
    username: str = None
    text: str = None
    file_id: str = None

def send_message(chat_id, text, reply_markup=None):
    url = f'{TG_URL}/sendMessage'
    data = {
        'chat_id': chat_id,
        'text': text,
        'reply_markup': json.dumps(reply_markup) if reply_markup else None
    }
    response = requests.post(url, data=data)
    return response.json()

def send_file(chat_id, file_id, text=None, reply_markup=None):
    url = f'{TG_URL}/sendFile'
    data = {
        'chat_id': chat_id,
        'text': text if text else None,
        'file_id': file_id,
        'reply_markup': json.dumps(reply_markup) if reply_markup else None
    }
    response = requests.post(url, data=data)
    return response.json()

def serializer(r):
    print(r)

    send_message(
        chat_id=r["message"]["chat"]["id"],
        text="qq",
        reply_markup=INLINE
    )




    # rJson = {}



    # try:
    #     message = Message(**rJson)
    #     print(message)

    # except ValidationError as e:
    #     print(e)

    return