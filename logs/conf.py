import datetime
from os.path import dirname, isfile
from main.errorlog import rotate

# PyBook Package Location
PYBOOK_PATH = dirname(dirname(__file__))

date = datetime.date.today()

## PyBook Log File Locations

# Export files
global BOOKS, ERR

# CSV with All Data
BOOKS = f"{PYBOOK_PATH}/logs/books.csv"

# Error Reports
ERR = f"{PYBOOK_PATH}/logs/error/error.{date}"

if not isfile(ERR):
    open(ERR, "x").close()
    err_file_limit = 10
    rotate(ERR, err_file_limit)