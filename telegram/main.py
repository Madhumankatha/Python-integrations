from fastapi import FastAPI, Request
from Telegram import Telegram

app = FastAPI()

telegram = Telegram("<TOKEN>","<CHANNEL_NAME>")

@app.get("/")
def read_root(request: Request):
    telegram.sendMessage("<Message>")
    return {"hello": "hello"}

