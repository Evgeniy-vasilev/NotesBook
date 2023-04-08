import csv
from datetime import datetime


# запись в файл

def recording(notes):
    with open("notesBook.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "title", "text", "created", "updated"], delimiter=";")
        writer.writeheader()
        for note in notes:
            writer.writerow(note)
