import json
import os

class UserManager:
    def __init__(self, filename="users.json"):
        self.filename = filename
        self.users = []
        self.load_users()
    
    def load_users(self):
        if not os.path.exists(self.filename):
            self.users = []
            return
        
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                self.users = json.load(f)
        except json.JSONDecodeError:
            print("データファイルが壊れています。空で起動します。")
            self.users = []

    def save_users(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.users, f, ensure_ascii=False, indent=2)
    
    def add_user(self, name, age):
        self.users.append({"name": name, "age": age})
        self.save_users()
    
    def find_user(self, name):
        for user in self.users:
            if user["name"] == name:
                return user
        return None

def show_menu():
    print("1: ユーザー追加")
    print("2: ユーザー検索")
    print("3: 終了")

def main():
    manager = UserManager()

    while True:
        show_menu()
        choice = input("選択してください: ")

        if choice == "1":
            name = input("名前: ")

            try:
                age = int(input("年齢: "))
            except ValueError:
                print("年齢は数字で入力してください")
                continue

            manager.add_user(name, age)

        elif choice == "2":
            name = input("検索する名前: ")
            user = manager.find_user(name)

            if user:
                print(user)
            else:
                print("見つかりません")
        
        elif choice == "3":
            print("終了します")
            break

        else:
            print("1~3を選択してください")

main()