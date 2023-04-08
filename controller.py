import read_notes as rn
import add_notes as an
import delete_note as dn
import edit_notes as en
def start():
    while True:
        print("Введите номер действия:")
        print("1. Создать заметку")
        print("2. Просмотр всех заметок")
        print("3. Удаление заметки")
        print("4. Редактирование заметок")
        num = input()
        match num:
            case "1":
                an.add_notes()
                print("Заметка создана")
            case "2":
                notes = rn.read_notes()
                for note in notes:
                    print(f'{note["id"]}.{note["title"]}({note["created"]})')
                    print(note["body"])
            case "3":
                dn.delete_note()
                print("Заметка удалена")
            case "4":
                en.edit_note()
                print("Заметка изменена")