from models import User

class UserManager:
    def __init__(self):
        self.users: list[User] = []
    
    def add_user(self, user: User):
        self.users.append(user)
        return user
    
    def get_users(self):
        return self.users
    
    def find_user(self, name: str):
        for user in self.users:
            if user.name == name:
                return user
        return None