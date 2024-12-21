from main.entries import Book, BookEntries

def add(entries: BookEntries, name: str):
    book = Book(name)
    print("What is the Name of the Author?")
    book.author = input()
    print("How Many Pages Does the Book Have? (>0)")
    book.total_pages = input()
    print("How Many Pages Have Been Read? (>=0)")
    book.current_page = input()
    entries.add_book(book)
    show(entries, name)

def delete(entries: BookEntries, name: str):
    print(f"Are You Sure You Want to Delete {name}? (y/n)")
    if input()[0].lower() == 'y':
        entries.remove_book(entries.find_book(name))
    
def _show_all(entries: BookEntries):
    for book in entries.get_books():
        print(book)

def show(entries: BookEntries, name: str):
    if name == "all":
        _show_all(entries)
    else:
        print(entries.find_book(name).to_str())

def list_authors_or_books(entries: BookEntries, checkbooks: bool = True):
    for book in entries.book_list:
        print(book.name if checkbooks else book.author)

def sort_books(entries: BookEntries, selector: str):
    entries.sort_list(selector)

def read(entries: BookEntries, name: str):
    book = entries.find_book(name)
    print("How Many Total Pages Have Been Read? (>=0)")
    book.current_page = input()

def edit(entries: BookEntries, name: str):
    book = entries.find_book(name)
    print("Would You Like to Change the Name of the Book? (y/n)")
    if input()[0] == 'y':
        print("What is the Name of the Book?")
        book.name = input()
    print("Would You Like to Change the Author? (y/n)")
    if input()[0] == 'y':
        print("What is the Name of the Author?")
        book.author = input()
    print("Would You Like to Change the Total Number of Pages? (y/n)")
    if input()[0] == 'y':
        print("What is the Total Number of Pages?")
        book.total_pages = input()
    print("Would You Like to Change the Number of Pages Read? (y/n)")
    if input()[0] == 'y':
        print("What is the Number of Pages Read?")
        book.current_page = input()

def clear(entries: BookEntries):
    print("Are You Sure You Want to Clear All Data? (y/n)")
    if input()[0].lower() == 'y':
        entries.clear_all()