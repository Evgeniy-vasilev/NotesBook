import read_notes as rn
import recording as rec


# Удаление заметок по id
def delete_note():
    notes = rn.read_notes()
    note_id = int(input("Введите id заметки: "))
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            break
    else:
        print("Заметка не найдена!")
    rec.recording(notes)
