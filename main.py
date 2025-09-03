from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

app =FastAPI()
from starlette.responses import PlainTextResponse, JSONResponse


@app.get("/ping", response_class=PlainTextResponse, status_code=200)
async def get_ping():
    return "pong"

@app.get("/health")
async def get_health():
    return "Ok"

class Characteristic(BaseModel):
    ram_memory: int
    rom_memory: int

class Phone(BaseModel):
    id: str
    brand: str
    model: str
    characteristics: Characteristic

phones_db: List[Phone] = []
@app.post("/phones", response_class=JSONResponse, status_code=201)
async def post_phone(phone: Phone):
    phones_db.append(phone)
    return phone

@app.get("/phones")
async def get_phones():
    return phones_db


@app.get("/phones/{id}")
async def get_phone(id: str):
    for phone in phones_db:
        if phone.id == id:
            return phone
    return {"error": "le phone comportant l'id fourni n'existe pas"}



