import json
import sys_setting
from datetime import date, timedelta, datetime
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
        
    def add_task(self):
        pass
def creat_addedTask():
    pass           
 
def create_task():
    os.system('clear')
    text_task = input("Введите задачу: ")
    print("Нажмите 'd', если нужно добавить подзадачу\nНажмите 'f' если нужно добавить дедлайн")
    add_to_task = None
    deadline = None
    key = sys_setting.get_key()
    if key == 'd':
        add_to_task = creat_addedTask()
    if key == 'f':
        deadline = input("Введите дату дедлайна (в формате: гггг-мм-дд): ")
    
    task1 = Planner(id=None, 
                    date = date.today(), 
                    time_date = datetime.now(),
                    task = text_task,
                    is_done=False,
                    add_to_task=add_to_task if add_to_task else "none",
                    deadline=deadline if deadline else "none")
    task1.add_task()
        
   
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
    