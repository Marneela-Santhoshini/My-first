import requests
import time

url = "http://127.0.0.1:8000/stream"

messages = [
    "I was charged twice for the same transaction",
    "I already called yesterday but it was not resolved",
    "I need this issue fixed immediately"
]

for msg in messages:

    response = requests.post(url, json={"text": msg})

    print("Customer:", msg)
    print("Analysis:", response.json())
    print("----------------------------------")

    time.sleep(2)