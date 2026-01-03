from pydantic import BaseModel, Field

class User(BaseModel):
    name: str = Field(..., min_length=1, max_length=20)
    age: int = Field(..., ge=0, le=120)

class UserResponse(BaseModel):
    name: str
    age: int