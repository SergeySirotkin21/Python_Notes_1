import json
import datetime

# Создание новой заметки
def create_note():
    note_id = input("Введите идентификатор заметки: ")
    note_title = input("Введите заголовок заметки: ")
    note_text = input("Введите текст заметки: ")
    note_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"id": note_id, "title": note_title, "text": note_text, "date": note_date}

# Сохранение заметки в файл
def save_note_to_file(note):
    with open("notes.json", "a") as file:
        file.write(json.dumps(note) + "\n")

# Чтение заметок из файла
def read_notes_from_file():
    notes = []
    with open("notes.json", "r") as file:
        for line in file:
            notes.append(json.loads(line))
    return notes

# Вывод списка всех заметок на экран
def print_notes(notes):
    for note in notes:
        print("Id: ", note["id"])
        print("Заголовок: ", note["title"])
        print("Дата/время: ", note["date"])
        print("Текст: ", note["text"])
        print("---------------")

# Вывод одной заметки на экран
def print_one_note():
    note_id = input("Введите идентификатор заметки для вывода: ")
    notes = read_notes_from_file()
    check = False

    for note in notes:
        if note["id"] == note_id:
            print("Id: ", note["id"])
            print("Заголовок: ", note["title"])
            print("Дата/время: ", note["date"])
            print("Текст: ", note["text"])
            print("Заметка выведена.\n")
            check = True
    if check == False:
        print("Не существует заметки с указанным идентификатором.\n")

# Вывод списка заметок с фильтром по дате
def print_filtered_by_date(notes):
    filtered_notes = []
    start_date = input("Введите начальную дату в формате ГГГГ-ММ-ДД: ")
    final_date = input("Введите конечную дату в формате ГГГГ-ММ-ДД: ")
    date = []
    for note in notes:
        date = ("".join([note["date"]]))
        if (date[:10] >= start_date) and (date[:10] <= final_date):
            filtered_notes.append(note)
    if filtered_notes == []:
        print("Нет заметок за указанный период.\n")
    else:
        print("Список заметок:")
        print_notes(filtered_notes)
        
# Редактирование заметки
def edit_note():
    note_id = input("Введите идентификатор заметки для редактирования: ")
    check = False

    notes = read_notes_from_file()
    for i, note in enumerate(notes):
        if note["id"] == note_id:
            notes[i] = create_note()
            print("Заметка отредактирована.\n")
            check = True
    if check == False:
        print("Не существует заметки с указанным идентификатором.")

    with open("notes.json", "w") as file:
        for note in notes:
            file.write(json.dumps(note) + "\n")

# Удаление заметки
def delete_note():
    note_id = input("Введите идентификатор заметки для удаления: ")
    check = False
    notes = read_notes_from_file()

    for i, note in enumerate(notes):
        if note["id"] == note_id:
            del notes[i]
            print("Заметка удалена.\n")
            check = True
    
    if check == False:
        print("Не существует заметки с указанным идентификатором.\n")
    
    with open("notes.json", "w") as file:
        for note in notes:
            file.write(json.dumps(note) + "\n")