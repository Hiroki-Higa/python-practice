import json
import os

class UserManager:
    def __init__(self, filename="users.json"):
        self.filename = filename
        self.users = []
        self.load_users()

    def load_users(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as f:
                self.users = json.load(f)

    def save_users(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.users, f, ensure_ascii=False, indent=2)
    
    def add_user(self, name, age):
        user = {"name": name, "age": age}
        self.users.append(user)
        self.save_users()
        return user
    
    def find_user(self, name):
        for user in self.users:
            if user["name"] == name:
                return user
        return None
            
