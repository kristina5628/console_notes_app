# 1. Напишите программу, которая запрашивает у пользователя текст и записывает его в новый 
# файл user_input.txt.
# 2. Реализуйте функционал добавления текста в существующий файл, не удаляя его предыдущее 
# содержимое.
import os
import sys

def add_text():
    f = open("user_input.txt", "a", encoding='utf-8')
    text = input("Введите какой-нибудь текст: ")
    f.write(text + "\n")
        
def main():    
    if not os.path.exists("user_input.txt") or os.path.getsize("user_input.txt") == 0:
        print("Файл с текстом пустой!")
    else:
        print("Ваш текст: ")
        with open("user_input.txt", "r") as f:
            
            for line in f:
                print(line, end='')
    try:
        opr = int(input("Нажмите 1, чтобы перейти к добавлению текста или 2, чтобы выйти: "))
        match opr:
            case 1:
                add_text()
                main()
            case 2:
                sys.exit()
    except ValueError:
        print("Произошла ошибка. Попробуйте снова!")
        main()

main()