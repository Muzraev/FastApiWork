from fastapi import FastAPI
from pydantic import BaseModel
from models import UserID
from models import UserAge
from models import Feedback

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

user_instance = UserID(name="Музраев Санджи", id=1)

@app.get("/users")
async def get_user():
    return user_instance

@app.post("/user")
async def check_adult(user: UserAge):
    is_adult = user.age >= 18
    return {"name": user.name, "age": user.age, "is_adult": is_adult}

feedbacks = []
@app.post("/feedback")
async def create_feedback(feedback: Feedback):
    feedbacks.append(feedback)
    return {"message": f"Спасибо, {feedback.name}! Ваш отзыв сохранён."}