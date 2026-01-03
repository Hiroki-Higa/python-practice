from fastapi import FastAPI, HTTPException, status
from models import User, UserResponse
from user_manager import UserManager

app = FastAPI()
manager = UserManager()

@app.post(
        "/users",
        response_model=UserResponse,
        status_code=status.HTTP_201_CREATED
)
def create_user(user: User):
    manager.add_user(user.name, user.age)
    return UserResponse(name=user.name, age=user.age)

@app.get(
    "/users/{name}",
    response_model=UserResponse
)
def get_user(name: str):
    user = manager.find_user(name)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user

@app.put(
    "/users/{name}",
    response_model=UserResponse
)
def update_user(name: str, user: User):
    updated = manager.update_user(name, user.age)
    if not updated:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return updated

@app.delete(
    "/users/{name}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_user(name: str):
    deleted = manager.delete_user(name)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )