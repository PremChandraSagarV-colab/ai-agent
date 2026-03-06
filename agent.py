import requests
import os
import datetime

TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

time = datetime.datetime.now().strftime("%H:%M:%S")

message = f"AI cloud agent woke up at {time}"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

requests.post(url, data={
    "chat_id": CHAT_ID,
    "text": message
})
