

#ежедневник

#дата
#время
#Задача
#подпункты: задача
#Приоритет
from datetime import date
import sys
from auth import *
from note import *
from planner import *


data_auth = auth()
log = data_auth[0]
id_user = data_auth[1]

def start():
    try:
        os.system('clear')
        print(f"Добро пожаловать, {log}!")
        a = int(input("1) Ежедневник\n2) Заметки\n3) Выйти из программы\nВыберете, что вам нужно открыть: "))
        if a < 1 or a > 3:
            print("Нужно выбрать из двух программ!")
            start()
        match a:
            case 1:
                planner()
                start()
            case 2:  
                notes(id_user)
                start()
            case 3:
                while True:
                    ans = input("Вы уверены, что хотите выйти из программы? (да/нет, y/n, yes/no): ")
                    if ans == "да" or ans == "yes" or ans == "y":
                        sys.exit()
                    elif ans == "нет" or ans == "no" or ans == "n":
                        start()
                    else:
                        print("Введены неверные данные, попробуйте снова!")
                        continue
    except ValueError:
        print("Произошла ошибка. Введены неверные данные")
        input()
        start()
    
start()
            


        
#def updateNote():
    