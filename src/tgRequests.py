from const import TG_URL
import json
import requests
from datetime import datetime
from pydantic import BaseModel
from pydantic import ValidationError

from const import INLINE


class Message(BaseModel):
    chat_id: str 
    message_id: str 
    content_type: str
    content: str 
    user_name: str 
    first_name: str 
    last_name: str 
    date_time: str

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
    with open("logs.json", 'r') as json_file:
        existing_log = json.load(json_file)

    keys_to_find = [
        "message_id",
        "id",
        "text",
        "first_name",
        "last_name",
        "username",
        "data",
        "photo",
        "voice",
        "video",
        "video_note",
        "animation"
    ]
    result_dict = find_values_in_json(r, keys_to_find) 

    content = "None"
    content_type = "None"
    first_name = "None"
    last_name = "None"
    user_name = "None"

    if "photo" in result_dict:
        content = result_dict["photo"][0]["file_id"]
        content_type = "photo" 
    elif "voice" in result_dict:
        content = result_dict["voice"]["file_id"]
        content_type = "voice"
    elif "video" in result_dict:
        content = result_dict["video"]["thumbnail"]["file_id"]
        content_type = "video"
    elif "video_note" in result_dict:
        content = result_dict["video_note"]["thumbnail"]["file_id"]
        content_type = "video_note"
    elif "animation" in result_dict:
        content = result_dict["animation"]["thumbnail"]["file_id"]
        content_type = "animation"       
    elif "audio" in result_dict:
        content = result_dict["audio"]["file_id"]
        content_type = "audio"
    elif "data" in result_dict:
        content = result_dict["data"]
        content_type = "call_back"
    elif "text" in result_dict:
        content = result_dict["text"]
        content_type = "text"

    if "username" in result_dict:
        user_name = result_dict["username"]
    if "last_name" in result_dict:
        last_name = result_dict["last_name"]
    if "first_name" in result_dict:
        first_name = result_dict["first_name"]

    current_datetime = datetime.now()
    date_time = str(current_datetime.replace(microsecond=0))

    if "message_id" in result_dict and "id" in result_dict:
        message = {
            "message_id": str(result_dict["message_id"]),
            "chat_id": str(result_dict["id"]),
            "content_type": content_type,
            "content": content,
            "user_name": user_name,
            "last_name": last_name,
            "first_name": first_name,
            "date_time": date_time
        }

        message = Message(**message)
        return message
    else:
        new_log = {
            date_time : {"def_serializer": result_dict}
        }
        print(new_log)
        existing_log.update(new_log)
        with open("logs.json", 'w') as json_file:
            json.dump(existing_log, json_file, indent=2)

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
