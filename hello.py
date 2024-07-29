from fastapi import FastAPI
from math_functions import subtract
import random

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World", "value": str(add(random.randint(0, 10), random.randint(11, 30)))}

@app.get("/subtract")
async def root():
    num1 = random.randint(10, 20)
    num2 = random.randint(0, 10)
    return {"message": "Subtracting " + num1 + " - " + num2, "value": str(subtract(num1 - num2))}