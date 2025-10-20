# Напишите функцию greet, которая принимает имя пользователя в качестве
# аргумента и выводит приветствие с этим именем.
print("Задание №1")

def greet(name):
    print(f"Привет {name}!")
    
a = input("Введите ваше имя: ")
greet(a)

# Создайте функцию square, которая возвращает квадрат переданного ей числа.
print("Задание №2")

def square(number):
    print(f"Квадрат числа {number} равен ", number**2)
    
num = int(input("Введите число: "))
square(num)

print("Задание №3")

def max_of_two(x, y):
    if x > y or x == y:
        print(f"Самое большое число: {x}")
    elif y > x:
        print(f"Самое большое число: {y}")
        
def main():
    try:
        num1 = int(input("Введите первое число: "))
        num2 = int(input("Введите второе число: "))
        max_of_two(num1, num2)
    except ValueError:
        print("Произошла ошибка! Должны быть введены числа!")
        main()
        
main()
