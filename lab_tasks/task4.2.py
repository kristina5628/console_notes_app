# 1. Создайте модуль my_module.py, который содержит минимум одну
# функцию. Например, функция может принимать два аргумента и
# возвращать их сумму.
# 2. Импортируйте my_module в другой файл Python и вызовите функцию,
# определённую в модуле.
from my_module import *

print("Калькулятор\n1) Сложение\n2) Вычитание\n3) Умножение\n4) Деление\n\
5) Нахождение факториала\n6) Нахождение квадратного корня")
opr = int(input("Выберете операцию, которую хотите совершить: "))
if opr == 5 or opr == 6:
    num = int(input("Введите число: "))
    match opr:
        case 5:
            result = factorial(num)
            print(f"Результат: {result}")
        case 6:
            result = sqwr(num)
            print(f"Результат: {result}")
elif opr >= 1 or opr <= 4:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    match opr:
        case 1:
            result = sum(num1, num2)
            print(f"Результат: {result}")
        case 2:
            result = difference(num1, num2)
            print(f"Результат: {result}")
        case 3:
            result = multiplication(num1, num2)
            print(f"Результат: {result}")
        case 4:
            result = division(num1, num2)
            print(f"Результат: {result}")
else:
    print("Данная операция не найдена!")
    