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
        return None
        


            