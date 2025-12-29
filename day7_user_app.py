users = []

def add_user(name, age):
    users.append({"name": name, "age": age})
def find_user(name):
    for user in users:
        if user["name"] == name:
            return user
    return None

def show_menu():
    print("1: ユーザー追加")
    print("2: ユーザー検索")
    print("3: 終了")

def main():
    while True:
        show_menu()
        choice = input("選択してください: ")

        if choice == "1":
            name = input("名前: ")
            age = int(input("年齢: "))
            add_user(name, age)

        elif choice == "2":
            name = input("検索する名前: ")
            user = find_user(name)
            if user:
                print(user)
            else:
                print("見つかりません")

        elif choice == "3":
            break

main()
