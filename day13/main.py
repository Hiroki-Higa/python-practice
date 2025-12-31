from fastapi import FastAPI
from user_manager import UserManager

app = FastAPI()
manager = UserManager()

@app.post("/users")
def add_user(name: str, age: int):
    return manager.add_user(name, age)

@app.get("/users/{name}")
def get_user(name: str):
    user = manager.find_user(name)
    if user:
        return user
    return {"error": "User not found"}
