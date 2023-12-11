import os
import uuid
from pprint import pprint

from yookassa import Configuration, Payment

Configuration.account_id = "285580"
Configuration.secret_key = os.getenv("YOOKASSA_SECRET_KEY")

idempotence_key = str(uuid.uuid4())
response = Payment.create({
    "capture": True,
    "amount": {
        "value": "500.00",
        "currency": "RUB"
    },
    "payment_method_data": {
        "type": "bank_card"
    },
    "confirmation": {
        "type": "redirect",
        "return_url": "https://www.example.com/return_url"
    },
    "description": "Заказ №72",
    "receipt": {
        "customer": {
            "email": "user@example.com"
        },
        "items": [
            {
                "description": "Топ трикотажный",
                "quantity": "1.00",
                "amount": {
                    "value": "500.00",
                    "currency": "RUB"
                },
                "vat_code": "4",
                "payment_mode": "full_payment",
                "payment_subject": "marked",
                "mark_mode": "0",
                "mark_code_info":
                    {
                        "gs_1m": "DFGwNDY0MDE1Mzg2NDQ5MjIxNW9vY2tOelDFuUFwJh05MUVFMDYdOTJXK2ZaMy9uTjMvcVdHYzBjSVR3NFNOMWg1U2ZLV0dRMWhHL0UrZi8ydkDvPQ=="
                    },
                "measure": "piece"
            }
        ]
    }
}, idempotence_key)

pprint(response.json())