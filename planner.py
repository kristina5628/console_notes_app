import json
import sys_setting
from datetime import date, timedelta
import os

class Planner:
    def __init__(self, id, date, time_date, task, is_done, add_to_task, deadline):
        self.id = id
        self.date = date
        self.time_date = time_date
        self.task = task
        self.add_to_task = add_to_task
        self.is_done = is_done
        self.deadline = deadline
        
#     def add_task(self):
        
def create_task():
    os.system('clear')
    text_task = input("Введите задачу: ")
    print("Нажмите 'd', если нужно добавить подзадачу\nНажмите 'f' если нужно добавить дедлайн")
    key = sys_setting.get_key()
    # if key == 'd':
        

def print_date(today_date):
    if today_date == date.today():
        print(f"____________{today_date} (сегодня)____________")
    else:
        print(f"____________{today_date}____________")

def planner():
    print("Приложение 'Ежедневник' открыто (чтобы выйти нажмите 'q')")
    today_date = date.today()
    print_date(today_date)
    
    while True:
        key = sys_setting.get_key()
        if key == '\x1b[D':
            today_date = today_date - timedelta(days=1)
            os.system('clear')
            print("Приложение 'Ежедневник' открыто (чтобы выйти нажмите 'q')")
            print_date(today_date)
        elif key == '\x1b[C':
            today_date = today_date + timedelta(days=1)
            os.system('clear')
            print("Приложение 'Ежедневник' открыто (чтобы выйти нажмите 'q')")
            print_date(today_date)
        elif key == 'q':
            break
    