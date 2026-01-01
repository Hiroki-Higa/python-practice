from fastapi import FastAPI, HTTPException
from models import User
from user_manager import UserManager

app = FastAPI()
manager = UserManager()

@app.post("/users")
def create_user(user: User):
    return manager.add_user(user)

@app.get("/users")
def get_users():
    return manager.get_users()

@app.get("/users/{name}")
def get_user(name: str):
    user = manager.find_user(name)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
