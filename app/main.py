from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "service2"}


@app.get("/service2")
def read_item():
    return {'service2': 'success'}
