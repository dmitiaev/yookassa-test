import os
import uuid
from pprint import pprint

import requests

account_id = "285580"
secret_key = os.getenv("YOOKASSA_SECRET_KEY")

headers = {
    "Idempotence-Key": str(uuid.uuid4()),
    "Content-Type": "application/json",
}

json_data = {
    "amount": {
        "value": "100.00",
        "currency": "RUB",
    },
    "capture": True,
    "confirmation": {
        "type": "redirect",
        "return_url": "https://www.example.com/return_url",
    },
    "description": "№1",
}

response = requests.post(
    "https://api.yookassa.ru/v3/payments",
    headers=headers,
    json=json_data,
    auth=(account_id, secret_key),
)

print(response.json())
pprint(response.json())