import csv
from datetime import datetime


# чтение заметок

def read_notes():
    notes = []
    with open("notesBook.csv", "r") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            row["id"] = int(row["id"])
            notes.append(row)
    return notes
