def read_files():
    f = open("Task_example.txt", "r")
    print(f.readlines())
    

f = open("Task_example.txt", "a+")
f.write("Какой-то текст\n")
f.write("Какой-то текст2\n")
f.write("Какой-то текст3\n")
read_files()