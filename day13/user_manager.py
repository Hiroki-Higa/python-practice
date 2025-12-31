class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, name: str, age: int):
        user = {"name": name, "age": age}
        self.users.append(user)
        return user
    
    def find_user(self, name: str):
        for user in self.users:
            if user["name"] == name:
                return user
            
        return None