import sqlite3

NAME_OF_DB = "books.db"

def connect():
    db = sqlite3.connect(NAME_OF_DB)
    cursor = db.cursor()
    pass
    db.close()

