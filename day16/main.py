from fastapi import FastAPI, HTTPException, status
from user_manager import UserManager
from models import User

app = FastAPI()
manager = UserManager()

@app.post("/users")
def create_user(user: User):
    manager.add_user(user.name, user.age)
    return user

@app.get("/users/{name}")
def get_user(name: str):
    user = manager.find_user(name)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.put("/users/{name}")
def update_user(name: str, user: User):
    updated = manager.update_user(name, user.age)
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return updated

@app.delete("/users/{name}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(name: str):
    deleted = manager.delete_user(name)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    
@app.put("/test")
def test_put():
    return {"ok": True}