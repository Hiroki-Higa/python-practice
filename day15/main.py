from fastapi import FastAPI, HTTPException
from models import User
from user_manager import UserManager

app = FastAPI()
manager = UserManager()

@app.post("/users")
def add_user(user: User):
    manager.add_user(user)
    return {"message": "ユーザーを追加しました"}

@app.get("/users")
def get_users():
    return manager.get_users()

@app.get("/users/{name}")
def get_user(name: str):
    user = manager.find_user(name)
    if not user:
        raise HTTPException(status_code=404, detail="ユーザーが見つかりません")
    return user