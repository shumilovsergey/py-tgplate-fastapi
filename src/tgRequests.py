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
    keys_to_find = [
        "message_id",
        "chat_id",
        "text",
        "first_name",
        "last_name",
        "username",
        "data",
        "photo",
        "voice",
        "video",
        "file_id"
    ]
    result_dict = find_values_in_json(r, keys_to_find) 
    print(result_dict)
    return

def find_values_in_json(json_obj, keys_to_find, result_dict=None):
    if result_dict is None:
        result_dict = {}

    if isinstance(json_obj, dict):
        for key, value in json_obj.items():
            if key in keys_to_find and key not in result_dict:
                result_dict[key] = value
            elif isinstance(value, (dict, list)):
                find_values_in_json(value, keys_to_find, result_dict)
    elif isinstance(json_obj, list):
        for item in json_obj:
            find_values_in_json(item, keys_to_find, result_dict)

    return result_dict
