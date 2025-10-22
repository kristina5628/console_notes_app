# 1. Создайте текстовый файл example.txt и заполните его несколькими строками текста.
# 2. Напишите функцию на Python, которая открывает файл example.txt в режиме чтения 
# и выводит его содержимое на экран.
# 3. Используйте разные методы чтения файла: чтение всего файла сразу, построчное чтение, 
# реализуйте выбор типа чтения в принимаемых аргументах функции.
import sys

def read_files(oper):
    f = open("example.txt", "r")
    match oper:
        case 1:
            print("Вывод содержимого:")
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
            
    
def choose_operation():
    while True:
        a = int(input("1)Вывести всё содержимое файла\n2)Построчный вывод\n" \
        "3)Вывод всего содержимого файла в список\n4) Вывод второй строчки\n5) " \
        "Выход\nВыбере нужную операцию:"))
        if a < 1 or a > 5:
            print("Ошибка! Такой операции нет.")
            choose_operation()
        read_files(a)
            
    
def write_info():
    print("Запись текста в файл.")
    with open("example.txt", "w+") as f:
        f.write("Первая строчка какого-то текста\n")
        f.write("Вторая строчка какого-то текста\n")
        f.write("Третья строчка какого-то текста\n")

    choose_operation()
    
write_info()