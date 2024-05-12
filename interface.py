from note_function import *

def interface():
    while True:
        print("1. Создать заметку")
        print("2. Вывести список всех заметок")
        print("3. Вывести одну заметку")
        print("4. Вывести список заметок с фильтром по дате")
        print("5. Редактировать заметку")
        print("6. Удалить заметку")
        print("7. Выход")

        choice = input("Введите номер команды: ")

        if choice == "1":
            note = create_note()
            save_note_to_file(note)
            print("Заметка сохранена.\n")
        elif choice == "2":
            notes = read_notes_from_file()
            print("Список всех заметок:")
            print_notes(notes)
        elif choice == "3":
            print_one_note()
        elif choice == "4":
            notes = read_notes_from_file()
            print_filtered_by_date(notes)
        elif choice == "5":
            edit_note()
        elif choice == "6":
            delete_note()
        elif choice == "7":
            break
        else:
            print("Неверный номер команды. Пожалуйста, повторите ввод.")