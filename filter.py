import read_notes as rn
from datetime import datetime


# Фильтр по дате
def filter():
    date = datetime.strptime(input("Введите дату/время в формате ГГГГ-ММ-ДД ЧЧ:ММ:CC: "), "%Y-%m-%d %H:%M:%S")
    notes = rn.read_notes()
    notes_filter = []

    for note in notes:
        if datetime.strptime(note["created"], "%Y-%m-%d %H:%M:%S") == date or \
                note["updated"] and datetime.strptime(note["updated"], "%Y-%m-%d %H:%M:%S") == date:
                    notes_filter.append(note)

    if len(notes_filter) == 0:
        print("Заметок не найдено!")

    return notes_filter
