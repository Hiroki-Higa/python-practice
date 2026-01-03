import json
from pathlib import Path
from models import User

DATA_FILE = Path("users.json")

class UserManager:
    def __init__(self):
        self.users = []
        self.load()

    def load(self):
        if DATA_FILE.exists():
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                self.users = json.load(f)
    
    def save(self):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json,dump(self.users, f, ensure_ascii=False, indent=2)
    
    def add_user(self, user: User):
        self.users.append(user.dict())
        self.save()

    def get_usser(self):
        return self.users
    
    def find_user(self, name: str):
        for user in self.users:
            if user["name"] == name:
                return user
   
    def update_user(self, name, age):
        for user in self.users:
            if user["name"] == name:
                user["age"] = age
                self.save()
                return user
    
        return None
    
    def delete_user(self, name):
        for user in self.users:
            if user["name"] == name:
                self.users.remove(user)
                self.save()
                return True
        return False
        