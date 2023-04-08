import read_notes as rn
from datetime import datetime

# Фильтр по дате
def filter():
    from_date = datetime.strptime(input("Введите дату/время в формате ГГГГ-ММ-ДД ЧЧ:ММ (например, 2022-01-01 12:00): "),
                                  "%Y-%m-%d %H:%M")
    notes = rn.read_notes()
    notes_filter = [note for note in notes if datetime.strptime(note["created"], "%Y-%m-%d %H:%M:%S") >=
                    from_date or note["updated"] and datetime.strptime(note["updated"], "%Y-%m-%d %H:%M:%S") >=
                    from_date]
    return notes_filter
