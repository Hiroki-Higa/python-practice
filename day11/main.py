from user_manager import UserManager

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
            print("ユーザーを追加しました")

        elif choice =="2":
            name = input("検索する名前: ")
            user = manager.find_user(name)
            
            if user:
                print(user)
            else:
                print("ユーザーが見つかりません")
        
        elif choice == "3":
            print("終了します")
            break

        else:
            print("正しい番号を選んでください")
            

if __name__ == "__main__":
    main()
