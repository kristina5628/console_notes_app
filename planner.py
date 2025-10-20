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
        if not os.path.exists("notes.json") or os.path.getsize("notes.json") == 0:
            try:
                tasks = {"planner": []}
                with open("notes.json", "w", encoding='utf-8') as f:
                    json.dump(tasks, f, ensure_ascii=False, indent=4)
            except FileNotFoundError:
                print("Произошла ошибка, попробуйте снова!")
        else:
            with open("notes.json", "r") as f:
                tasks = json.load(f)
                
            task = tasks["planner"]
            if task:
                id_last_note = task[-1]["id"] + 1
            else:
                id_last_note = 1
            self.id = id_last_note
            
            newTask = {"id": self.id, "date": self.date, "time_date": self.time_date, "task": self.task, "add_to_task": self.add_to_task, "is_done": self.is_done, "deadline": self.deadline}
            task.append(newTask)
            
            with open("notes.json", "w", encoding="utf-8") as f:
                json.dump(tasks, f, ensure_ascii=False, indent=4)
                
            print("Задание на день добавлено!")
            
def create_addedTask():
    pass           
 
def create_task():
    os.system('clear')
    text_task = input("Введите задачу: ")
    print("Нажмите 'd', если нужно добавить подзадачу\nНажмите 'f' если нужно добавить дедлайн")
    add_to_task = None
    deadline = None
    key = sys_setting.get_key()
    if key == 'd':
        add_to_task = create_addedTask()
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

def init_notes_file():
    if not os.path.exists("notes.json"):
        task_structure = {
            "planner": []
        }
        with open("notes.json", "w", encoding='utf-9') as f:
            json.dump(task_structure, f, ensure_ascii=False, indent=4)
        
    
def show_tasks(today_date):
    init_notes_file()
    with open("notes.json", "r") as f:
        tasks = json.load(f)
    taskss = tasks["planner"]
    today_str = today_date.strftime("%Y-%m-%d")
    count = 0
    for i in taskss:
        if today_str == i.get["date",""]:
            print(f'Дата: {i.get["time_date"]}\nЗадача: {i.get["task"]}\nПодзадачи: {i.get["add_to_task"]}\nСделано: {i.get["is_done"]}\nДедлайн: {i.get["deadline"]}')
            count+=1

    if count == 1:
        print("У вас пока нет задач на день! (Доби своден:))")

def task_operation():
    print("1)Добавить задачу на день\n2)Изменить задачу\n3)Удалить задачу")
    try:
        a = int(input("Выберете, что хотите сделать с задачами: "))
        match a:
            case 1:
                create_task()
            case 2:
                pass
            case 3: 
                pass
    except ValueError:
        print("Введите пожалуйста число от 1 до 3!")                
            
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
            show_tasks(today_date)
            task_operation()
        elif key == '\x1b[C':
            today_date = today_date + timedelta(days=1)
            os.system('clear')
            print("Приложение 'Ежедневник' открыто (чтобы выйти нажмите 'q')")
            print_date(today_date)
            show_tasks(today_date)
            task_operation()
        elif key == 'q':
            break
    