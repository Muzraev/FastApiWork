from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Автопелоад действительно работает"}

class Numbers(BaseModel):
    num1: float
    num2: float

@app.post("/calculate")
async def calculate(nums: Numbers):
    return {"result": nums.num1 + nums.num2}