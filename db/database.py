import sqlite3
from db.codes import EXIT_CODE
from main.entries import Book

NAME_OF_DB = "books.db"
DB : sqlite3.Connection
DB_CURSOR : sqlite3.Cursor

def connect() -> EXIT_CODE:
    DB = sqlite3.connect(NAME_OF_DB)
    if DB is None:
        return EXIT_CODE.FAIL
    DB_CURSOR = DB.cursor()

    if (DB_CURSOR.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='books'")).fetchone() is None:
        DB_CURSOR.execute("CREATE TABLE books (id PRIMARY INTEGER KEY, name TEXT, author TEXT, total_pages INTEGER, pages_read INTEGER)")

    return EXIT_CODE.SUCCESS

def add(book : Book) -> EXIT_CODE:
    cmd = "INSERT INTO books VALUES (?, ?, ?, ?, ?)"
    # TODO format data properly and execute command with proper exit code
        
    res = DB_CURSOR.execute(cmd)
    DB.commit()
    if res is None:
        return EXIT_CODE.IO_ERROR # ! Make sure this is the correct error

    return EXIT_CODE.SUCCESS

def __get_all() -> dict[str, tuple[str | int]]:
    res = DB_CURSOR.execute("SELECT * FROM books ORDER BY name").fetchall()
    ret = {}
    for row in res:
        ret[row[1]] = row
    
    return ret

def get(data: str | int) -> dict[str, tuple[str | int]]:
    if data == "ALL":
        return __get_all()
    
    ret = {}
    if type(data) == str:
        res = DB_CURSOR.execute("SELECT * FROM books WHERE name='(?)'", data).fetchall()
        res.append(DB_CURSOR.execute("SELECT * FROM books WHERE author='(?)'", data).fetchall())
    elif type(data) == int:
        res = DB_CURSOR.execute("SELECT * FROM books WHERE total_pages='(?)'", str(data)).fetchall()
        res.append(DB_CURSOR.execute("SELECT * FROM books WHERE pages_read='(?)'", str(data)).fetchall())
    else:
        return {}
    
    for row in res:
        ret[row[1]] = row

    return ret

def remove(book: Book) -> EXIT_CODE:
    res = DB_CURSOR.execute("") # TODO Insert code to delete an entry from the database with error checking

    return EXIT_CODE.SUCCESS
