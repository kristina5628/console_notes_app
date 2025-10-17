from datetime import date, datetime
import json
import os

class Notes:
    def __init__(self, id, date_create, update_date, title, text_note, tags, us_id):
        self.id = id
        self.date_create = date_create
        self.update_date = update_date
        self.title = title
        self.text_note = text_note
        self.tags = tags
        self.us_id = us_id 
        
    def add_information(self):
        
        if not os.path.exists("notes.json") or os.path.getsize("notes.json") == 0:
            try:
                notes = {"notes": []}
                with open("notes.json", "w", encoding="utf-8") as f:
                    json.dump(notes, f, ensure_ascii=False, indent=4)
            except FileNotFoundError:
                print("Произошла ошибка, попробуйте снова!")
        else:
            with open("notes.json", "r") as f:
                notes = json.load(f)
            
            note = notes["notes"]
            if note:
                id_last_note = note[-1]["id"] + 1
            else:
                id_last_note = 1
            self.id = id_last_note
            
            newNote = {"id": self.id, "date_create": self.date_create, "update_date": self.update_date, "title": self.title, "text_note": self.text_note, "tags": self.tags, "user_id": self.us_id}
            note.append(newNote)
            
            with open("notes.json", "w", encoding="utf-8") as f:
                json.dump(notes, f, ensure_ascii=False, indent=4)
            
            print("Заметка добавлена!")    
    
    def AddEditNote(self):
        with open("notes.json", "r") as f:
            nots = json.load(f)
        note = nots["notes"]
        for i in note:
            if self.id == i["id"]:
                index = self.id - 1        
        if str(self.title) != "None":
            note[index]["title"] = self.title
            note[index]["update_date"] = self.update_date
        elif str(self.text_note) != "None":
            note[index]["text_note"] = self.text_note
            note[index]["update_date"] = self.update_date
        elif str(self.tags) != "None":
            note[index]["tags"] = self.tags
            note[index]["update_date"] = self.update_date
        else:
            print("Произошла ошибка! Попробуйте снова!")
            input()
            notes()
        with open("notes.json", "w", encoding="utf-8") as f:
            json.dump(nots, f, ensure_ascii=False, indent=4)
        
def AddTag():
    tags = {}
    i = 1
    while True:
        name_tag = input(f"Введите тег №{i} (Введите '0' чтобы закончить ввод): ")
        if name_tag == "0":
            break
        tags[f"tag{i}"] = name_tag
        i+=1
    return tags     
        
def CreateNote(id_user):
    os.system('clear')
    title = input("Введите заголовок заметки: ")
    text_note = input("Введите текст заметки: ")
    tags = AddTag()
    note1 = Notes(None, f"{date.today()}", "none", title, text_note, tags, id_user)
    note1.add_information()
    
def EditNote(id_user):
    with open("notes.json", "r") as f:
        note = json.load(f)
    notes1 = note["notes"]
    count = 0
    for i in notes1:
        if id_user == i["user_id"]:
            print(f'id: {i["id"]}\nДата создания: {i["date_create"]}\nДата обновления: {i["update_date"]}\nЗаголовок: {i["title"]}\nТекст заметки: {i["text_note"]}\nТеги: {i["tags"]}\n----------------------')
            count+=1
        else:
            continue
    else:
        if count == 0:
            print("У вас пока нет заметок!")
    id_note = int(input("Введите id заметки, которую вы хотите изменить: "))
    
    for j in notes1:
        if id_note == j["id"]:
            print(f'Изменение данной заметки:\nid: {j["id"]}\nДата создания: {j["date_create"]}\nДата обновления: {j["update_date"]}\nЗаголовок: {j["title"]}\nТекст заметки: {j["text_note"]}\nТеги: {j["tags"]}\n----------------------')
            print(f"1) Изменить текст заголовка\n2) Изменить текст заметки\n3) Изменить теги\n4) Вернуться назад")
            choice = int(input("Выбере, что нужно сделать с заметкой: "))
            match choice:
                case 1:
                    title = input("Введите новый заголовок заметки: ")
                    editNote = Notes(id_note, j["date_create"], str(date.today()), title, "None", "None", id_user)
                    editNote.AddEditNote()
                case 2:
                    text_note = input("Введите новый текст заметки: ")
                    editNote = Notes(id_note, j["date_create"], str(date.today()), "None", text_note, "None", id_user)
                    editNote.AddEditNote()
                case 3:
                    tags = AddTag()
                    editNote = Notes(id_note, j["date_create"], str(date.today()), "None", "None", tags, id_user)
                    editNote.AddEditNote()
                case 4:
                    return notes(id_user)
    else:
        print("Такого id нет!")
    
def DeleteNote(id_user):
    with open("notes.json", "r") as f:
        note = json.load(f)
    
    list_note = note["notes"]
    count = 0
    for i in list_note:
        if id_user == i["user_id"]:
            print(f'id: {i["id"]}\nДата создания: {i["date_create"]}\nДата обновления: {i["update_date"]}\nЗаголовок: {i["title"]}\nТекст заметки: {i["text_note"]}\nТеги: {i["tags"]}\n----------------------')
            count+=1        
        else:
            continue
    else:
        if count == 0:
            print("У вас пока нет заметок!")
    id_note = int(input("Введите id заметки, которую хотите удалить: "))
    found = False
    for index, j in enumerate(list_note):
        if id_note == j["id"]:
            found = True
            print("Вы уверены, что хотите удалить данную заметку? (y/n):")
            print(f'Удаление данной заметки:\nid: {j["id"]}\nДата создания: {j["date_create"]}\nДата обновления: {j["update_date"]}\nЗаголовок: {j["title"]}\nТекст заметки: {j["text_note"]}\nТеги: {j["tags"]}\n----------------------')
            ans = input("Ваш ответ:")
            if ans.lower() == "y":
                del list_note[index]
                with open("notes.json", "w", encoding="utf-8") as f:
                    json.dump(note, f, ensure_ascii=False, indent=4)
                print("Заметка удалена!")
            elif ans.lower() == "n":
                print("Удаление отменено!")
                input()
                notes()
                
    if not found:
        print("Заметка с таким id не найдена!")
        input()
    
    
    
def notes(id_user):
    print("Приложение 'Заметки' открыто\nЗаметки:")
    with open("notes.json", "r") as f:
        note = json.load(f)
    notes1 = note["notes"]
    count = 0
    for i in notes1:
        if id_user == i["user_id"]:
            print(f'id: {i["id"]}\nДата создания: {i["date_create"]}\nДата обновления: {i["update_date"]}\nЗаголовок: {i["title"]}\nТекст заметки: {i["text_note"]}\nТеги: {i["tags"]}\n----------------------')
            count+=1
        else:
            continue
    else:
        if count == 0:
            print("У вас пока нет заметок!")
    a = int(input("1) Создать заметку\n2) Изменить заметку\n3) Удалить заметку\n4) Вернуться в меню\nВыбере действие: "))
    match a:
        case 1:
            CreateNote(id_user)
            return id_user
        case 2:
            EditNote(id_user)
            return id_user
        case 3:
            DeleteNote(id_user)
            return id_user
        case 4:
            return id_user