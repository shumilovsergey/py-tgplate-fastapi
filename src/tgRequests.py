from const import TG_URL
import json
import requests

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