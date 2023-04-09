import read_notes as rn
import recording as rec
from datetime import datetime


# Создание заметок
def add_notes():
    notes = rn.read_notes()
    max_id = max([note["id"] for note in notes]) if notes else 0
    new_note = {
        "id": max_id + 1,
        "title": input("Введите название заметки: "),
        "text": input("Введите текст заметки: "),
        "created": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "updated": ""
    }
    notes.append(new_note)
    rec.recording(notes)
    print("Заметка создана!")
