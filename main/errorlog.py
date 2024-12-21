import datetime
import os

def _txtmake(source: str, message: str) -> str:
    return f"{datetime.datetime.now()} - {source}: {message}\n"

def errorlog(source: str, message: str):
    from logs.conf import ERR, DEBUG
    if DEBUG and not os.path.isfile(ERR):
        raise FileNotFoundError("Error File not Created Properly")
    if DEBUG:
        with open(ERR, "a") as e:
            e.write(_txtmake(source, message))
    
def rotate(errfile: str, limit: int = 10):
    err_dir = os.path.dirname(errfile)
    err_files = [os.path.join(err_dir, i) for i in os.listdir(err_dir) if i.startswith("error")]
    err_files.sort(key=lambda x: os.path.getmtime(x))

    while len(err_files) > limit:
        os.remove(err_files[0])
        err_files.pop(0)