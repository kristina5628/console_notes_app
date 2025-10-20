def is_prime(number):
    
    for i in range(2, number):
        if number % i == 0:
            print("Число не является простым")
            break
    else:
        print("Число простое")
            
a = int(input("Введите число: "))
is_prime(a)
