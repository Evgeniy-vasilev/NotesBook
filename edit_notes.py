import read_notes as rn
import recording as rec
from datetime import datetime


# Редактирование
def edit_note():
    notes = rn.read_notes()
    note_id = int(input("Введите id заметки:"))
    for note in notes:
        if note["id"] == note_id:
            note["title"] = input("Введите новый заголовок: ")
            note["text"] = input("Введите новый текст: ")
            note["updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            break
    else:
        print("Заметка не найдена")
    rec.recording(notes)
