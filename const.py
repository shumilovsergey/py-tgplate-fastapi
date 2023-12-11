from dotenv import load_dotenv
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

INLINE= {
    "inline_keyboard" :  [
        [
            {'text': '◀', 'callback_data': json.dumps({"menu":"menu"})}
        ]
    ]
}

