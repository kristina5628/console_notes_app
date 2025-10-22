# Напишите функцию is_prime, которая определяет, является ли число простым, и
# возвращает True или False соответственно.
def is_prime(number):
    is_primery = True

    for i in range(2, number):
        if number % i == 0:
            is_primery = False
            break
    print(is_primery)
                
a = int(input("Введите число: "))
is_prime(a)
