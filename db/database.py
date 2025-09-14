import sqlite3
from db.codes import EXIT_CODE

NAME_OF_DB = "books.db"
DB : sqlite3.Connection
DB_CURSOR : sqlite3.Cursor

def connect() -> sqlite3.Cursor | EXIT_CODE:
    DB = sqlite3.connect(NAME_OF_DB)
    if DB is None:
        return EXIT_CODE.FAIL
    DB_CURSOR = DB.cursor()

    return DB_CURSOR

def add(cmd: str) -> EXIT_CODE:
    banned_sql_keywords = [
        "from",
        "select",
        "table",
        "where",
        "not", # * fill in with more as you find them
    ]
    for word in banned_sql_keywords:
        if word in cmd:
            return EXIT_CODE.INVALID_CMD
        
    DB_CURSOR = DB.execute(cmd)
    if DB_CURSOR is None:
        return EXIT_CODE.IO_ERROR # ! Make sure this is the correct error

    return EXIT_CODE.SUCCESS