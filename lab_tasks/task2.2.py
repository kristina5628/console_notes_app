# Напишите функцию describe_person, принимающую имя и возраст человека, и
# печатающую эту информацию в читаемом виде. Сделайте возраст опциональным
# аргументом со значением по умолчанию 30.

def describe_person(name, age=30):
    print(f"Привет, {name}!\nВаш возраст: {age} лет.")
    
name = input("Введите ваше имя: ")
age = input("Введите ваш возраст: ")
if not age:
    describe_person(name)
else:
    describe_person(name, age)