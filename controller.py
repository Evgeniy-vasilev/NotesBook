import read_notes as rn
import add_notes as an
import delete_note as dn
import edit_notes as en
import filter as f


# Контроллер
def start():
    while True:
        print()
        print("Добро пожаловать в программу Заметки!")
        print("1. Создать заметку")
        print("2. Просмотр всех заметок")
        print("3. Удаление заметки")
        print("4. Редактирование заметок")
        print("5. Фильтр по дате")
        print("6. Выход")
        num = input("Введите номер действия: ")
        match num:
            case "1":
                an.add_notes()
            case "2":
                notes = rn.read_notes()
                for note in notes:
                    print(f'{note["id"]}.{note["title"]}({note["created"]}, {note["updated"]})')
                    print(note["text"])
            case "3":
                dn.delete_note()
            case "4":
                en.edit_note()
            case "5":
                f.filter()
            case "6":
                print("До встречи!")
                break
