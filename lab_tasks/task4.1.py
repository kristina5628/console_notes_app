# 1. Импортируйте модуль math и используйте функцию sqrt() для вычисления
# квадратного корня.
# 2. Используйте модуль datetime для отображения текущей даты и времени.
import math
from datetime import datetime

date = datetime.now()
print(f"Сегодня: {date}\n")
print("Нахождение квадратного корня:")
num = int(input("Введите число: "))
result = math.sqrt(num)

print(f"Квадратный корень из числа {num} равен {result}")