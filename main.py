from fastapi import FastAPI
app =FastAPI()
from starlette.responses import PlainTextResponse

@app.get("/ping", response_class=PlainTextResponse, status_code=200)
async def get_ping():
    return "pong"

@app.get("/health")
async def get_health():
    return "Ok"