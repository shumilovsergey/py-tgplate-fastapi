import json
import requests

from const import TG_URL
from const import TG_WEBHOOK_URL
from const import TG_ROUT

def webhookSet():
    data = {"url":TG_WEBHOOK_URL + "/"+ TG_ROUT}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(TG_URL +"/setWebhook", data=json.dumps(data), headers=headers)

    if response.status_code == 200:
        print("200. Response:")
        print(response.json())
    else:
        print(f"{response.status_code}. Response:")
        print(response.json())
    return

def logs_create():
    with open("logs.json", 'w') as json_file:
        json.dump({}, json_file)
