import sys
import os.path
from main.errorlog import errorlog

if len(sys.argv) < 2 or sys.argv[1] == "-h" or sys.argv[1] == "--help":
    err_message = "ERR: No Arguements Given"
    print(err_message)
    errorlog(os.path.basename(__file__), err_message)
    print("""
Usage: pybook
\t\tadd <book>
          
\t\tdel <book>
          
\t\tshow <book>
          
\t\t[books|authors]
          
\t\tsort [all|name|author|total pages|current page]

\t\tread <book>
          
\t\tedit <book>
          
\t\tgui

\t\tclear
    """)
    sys.exit(1)

from main.entries import BookEntries
from main.funcs import *

entries = BookEntries()

function_maps = {
    "add": add,
    "del": delete,
    "show": show,
    "sort": sort_books,
    "read": read,
    "edit": edit
}

count = 1
while count < len(sys.argv):
    if sys.argv[count] == "b" or sys.argv[count] == "books":
        list_authors_or_books(entries)
    elif sys.argv[count] == "a" or sys.argv[count] == "authors":
        list_authors_or_books(entries, False)
    elif sys.argv[count] == "g" or sys.argv[count] == "gui":
        from main.gui import run_gui
        run_gui(entries)
    elif sys.argv[count] == "clear":
        clear(entries)
    elif sys.argv[count] not in list(function_maps.keys()):
        err_message = f"ERR: Function '{sys.argv[count]}' is not Valid."
        print(err_message)
        errorlog(os.path.basename(__file__), err_message)
        sys.exit(1)
    else: 
        function_maps[sys.argv[count]](entries, " ".join(sys.argv[count+1:]))
        count = len(sys.argv)
    count += 1

entries.save_data()