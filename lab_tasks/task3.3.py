import sys
import os

def read_files(oper):
    try:
        f = open("example.txt", "r")
        match oper:
            case 1:
                print("Вывод содержимого на экран в одну строку:")
                print(f.read())
            case 2:
                print("Построчный вывод:")
                for line in f:
                    print(line, end='')
            case 3:
                print("Вывод всего содержимого файла в список")
                file = f.readlines()
                for i in file:
                    print(i)
            case 4:
                print("Вывод второй строчки:")
                file = f.readlines()
                print(file[1])
            case 5:
                sys.exit()
    except FileNotFoundError:
        print("Файла не существует!")
            
    
def choose_operation():
    while True:
        a = int(input("1)Вывод всё содержимое файла\n2)Построчный вывод\n3)Вывод всего содержимого файла в список\n4) Вывод второй строчки\n5) Выход\nВыбере нужную операцию:"))
        if a < 1 or a > 5:
            print("Ошибка! Такой операции нет.")
            choose_operation()
        read_files(a)
            
    
def write_info():
    print("Запись текста в файл.")
    try:
        with open("example.txt", "w") as f:
            f.write("Первая строчка какого-то текста\n")
            f.write("Вторая строчка какого-то текста\n")
            f.write("Третья строчка какого-то текста\n")

        choose_operation()
    except FileNotFoundError:
        print("Файла не существует!")    
    
write_info()