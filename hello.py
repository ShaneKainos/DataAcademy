from fastapi import FastAPI
from math_functions import add
import random

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World", "value": str(add(random.randint(0, 10), random.randint(11, 30)))}