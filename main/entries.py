import csv
import os.path
from logs.conf import BOOKS
from main.errorlog import errorlog

class Book:
    
    def __init__(self, name: str = "", author: str = "", current: int = 0, total: int = 1):
        self._name : str = name
        self._author : str = author
        self._current_page : int = current if current >= 0 else 0
        self._total_pages : int = total if total > 0 else 1
    
    def __error__(self, _message: str, _exception: Exception):
        errorlog(os.path.basename(__file__), _message)
        raise _exception
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, new_name: str):
        self._name = new_name
    
    @property
    def author(self) -> str:
        return self._author
    
    @author.setter
    def author(self, new_author: str):
        self._author = new_author

    @property
    def total_pages(self) -> int:
        return self._total_pages
    
    @total_pages.setter
    def total_pages(self, new_total_pages):
        try:
            new_total_pages = int(new_total_pages)
        except ValueError:
            _err_message = f"Incompatible Type: assigning {type(new_total_pages)} to type {type(self._total_pages)}"
            self.__error__(_err_message, TypeError(_err_message))
        if new_total_pages < self._current_page or new_total_pages == 0:
            _err_message = "Invalid Value: total pages must be greater than 0 and less than current pages"
            self.__error__(_err_message, ValueError(_err_message))
        self._total_pages = new_total_pages
    
    @property
    def current_page(self) -> int:
        return self._current_page
    
    @current_page.setter
    def current_page(self, new_current_page):
        try:
            new_current_page = int(new_current_page)
        except ValueError:
            _err_message = f"Incompatible Type: assigning {type(new_current_page)} to type {type(self._current_page)}"
            self.__error__(_err_message, TypeError(_err_message))
        if new_current_page < 0 or new_current_page > self._total_pages:
            _err_message = "Invalid Value: current page number must be at least 0 and less than or equal to total pages"
            self.__error__(_err_message, ValueError(_err_message))
        self._current_page = new_current_page
    
    def to_str(self, _adhere_to_size: int = 30) -> str:
        if len(self._name) > 100 or _adhere_to_size > 100:
            return f"{self._name:160}{self._author:60}{self._current_page:8d}{self._total_pages:8d}"
        if len(self._name) > 65 or _adhere_to_size > 65:
            return f"{self._name:110}{self._author:50}{self._current_page:8d}{self._total_pages:8d}"
        if len(self._name) > 30 or _adhere_to_size > 30:
            return f"{self._name:70}{self._author:40}{self._current_page:8d}{self._total_pages:8d}"
        return f"{self._name:40}{self._author:30}{self._current_page:8d}{self._total_pages:8d}"
    
class BookEntries:

    def __init__(self):
        self._book_list : list[Book] = []
        with open(BOOKS, "r", newline='') as info:
            _books_csv = csv.reader(info, quotechar='|')
            for _book in _books_csv:
                if len(_book) != 4:
                    self._book_list.clear()
                    raise Exception("Info File Formatted Incorrectly.")
                self._book_list.append(Book(_book[0], _book[1], int(_book[2]), int(_book[3])))
    
    @property
    def book_list(self):
        return self._book_list
    
    def get_books(self) -> list[str]:
        _m = 0
        for _book in self._book_list:
            if len(_book._name) > _m:
                _m = len(_book._name)

        return [_book.to_str(_m) for _book in self._book_list]
    
    def find_book(self, name: str) -> Book:
        for book in self._book_list:
            if book.name == name:
                return book
        _err_message = f"{name} Book Does not Exist."
        errorlog(os.path.basename(__file__), _err_message)
        raise Exception(_err_message)
    
    def sort_list(self, selector: str):
        from main.sorts import sort
        self._book_list = sort(self._book_list, selector)

    def add_book(self, book: Book):
        self._book_list.append(book)
    
    def remove_book(self, book: Book):
        if book not in self._book_list:
            return
        self._book_list.remove(book)

    def clear_all(self):
        self._book_list.clear()
    
    def save_data(self):
        with open(BOOKS, "w", newline='') as _info:
            _books_csv = csv.writer(_info, quotechar='|')
            for _book in self._book_list:
                _books_csv.writerow([_book._name, _book._author, _book._current_page, _book._total_pages])