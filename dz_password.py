password = "qwerty"
password_user = input("Введите пароль: ")
while password_user == password:
    password_user = input("Введите пароль: ")
    print("Верный пароль")
    break
