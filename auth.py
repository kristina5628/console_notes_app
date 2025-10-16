import sys
import json
import os
import termios
import tty

def MaskPassword(prompt="Пароль: "):
    print(prompt, end='', flush=True)
    password = ''
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        while True:
            ch = sys.stdin.read(1)
            if ch in ['\r', '\n']:
                print()
                break
            elif ch == '\x7f':
                if len(password) > 0:
                    password = password[:-1]
                    print('\b \b', end='', flush=True)
            elif ch == '\x03':
                raise KeyboardInterrupt
            else:
                password += ch
                print('*', end='', flush=True)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return password

def auth():
    print("_______Авторизация_______")
    print("Ещё не зарегистрированы? Введите 0 чтобы перейти к регистации!")
    login = input("Введите логин: ")
    if login == "0":
        return registrate()
    password = MaskPassword("Введите свой пароль: ")
    if password == "0":
        return registrate()
    try:    
        with open("notes.json", 'r') as f:
            user = json.load(f)
        us = user["users"]
    
        for i in us:
            if i["login"] == login and i["password"] == password:
                log = login
                id_user = i["id"]
                return log, id_user
        else:
            print("Логин или пароль введены неверно! Попробуйте снова")
            input()
            return auth()
    except FileNotFoundError:
        print("Вы не зарегестрированы! Зарегестрируйтесь!")
        input()
        return registrate()

def CheckLogin(login):
    with open("notes.json", "r") as f:
        user = json.load(f)
    us = user["users"]
    
    for i in us:
        if login == i["login"]:
            print("Пользователь с таким логином уже существует!")
            input()
            registrate()
    
def registrate():
    os.system('clear')
    print("_______Регистрация_______")
    print("Введите 0 чтобы вернуться к авторизации!")
    login = input("Введите логин: ")
    if login == "0":
        return auth()
    CheckLogin(login)
    password = MaskPassword("Введите свой пароль: ")
    if password == "0":
        return auth()
    elif len(password) < 8:
        print("Пароль должен содержать больше 8 символов")
        input()
        registrate()
    
    if not os.path.exists("notes.json") or os.path.getsize == 0:
        try:
            user = {"users": [], "notes": []}
            with open("notes.json", 'w', encoding="utf-8") as f:
                json.dump(user, f, ensure_ascii=False, indent=4)
        except FileNotFoundError:
            print("Произошла ошибка, попробуйте снова!")
            input()
            return registrate()
    
    with open("notes.json", "r") as f:
        user = json.load(f)
        
    us = user["users"]
    if us:
        id_last_user = us[-1]["id"] + 1
    else:
        id_last_user = 1
          
    user_bd = {"id": id_last_user, "login": login, "password": password}
    
    us.append(user_bd)
    with open("notes.json", 'w', encoding='utf-8') as f:
        json.dump(user, f, ensure_ascii=False, indent=4)
        
    print("Поздравляю! Вы успешно зарегестрированы)")
    return auth()
    