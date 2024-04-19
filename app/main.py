"""
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}



"""
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

user_name = None

class User(BaseModel):
    name: str


@app.get("/")
def root():
    return{ "message": "Hello Bosman!"}

@app.get("/home")
def home():
    return { "message": "Bye Bosman!" }

#####여기까지 저번주########


@app.post("/user/")
async def receive_user(user: User):
    global user_name
    user_name = user.name
    return {"message": "User name received"}


@app.get("/user/")
async def get_user():
    return {"user_name": user_name}

@app.put("/user/")
async def receive_user(user: User):
    global user_name
    user_name = user.name
    return {"message": "User name changed"}


@app.delete("/user/")
async def del_user():
    global user_name
    user_name = "DELETED"
    return {"message": "User name deleted"}

"""

from fastapi import FastAPI

import requests

app = FastAPI()

@app.get("/")
def root():
    URL = "https://bigdata.kepco.co.kr/openapi/v1/powerUsage/industryType.do?year=2020&month=11&metroCd=11&cityCd=110&bizCd=C&apiKey=ergT0Yyea577o2lLp4COXsCi6x0dVh8yvr5bTQ6P&returnType=json"

    contents = requests.get(URL).text

    return {"message": contents}

@app.get("/home")
def home():
    return {"message": "Home!"}