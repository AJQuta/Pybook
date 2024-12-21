import dearpygui.dearpygui as dpg
import datetime
import os.path
from main.entries import Book, BookEntries
from main.errorlog import errorlog

class Gui:

    def __init__(self, entries: BookEntries):
        self._entries: BookEntries =  entries
        self._num_books = 0
        self._viewport_size = (800,400)
        self._window_size = (800,400)
        
        dpg.create_context()
        dpg.create_viewport(title="PyBook", width=self._viewport_size[0], height=self._viewport_size[1])

    def __show__(self):
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        
    def __destroy__(self):
        self._entries.save_data()
        dpg.destroy_context()

    def save(self):
        for index in range(self._num_books):
            _name = dpg.get_value(f"Name {index}")
            _author = dpg.get_value(f"Author {index}")
            _current_page = dpg.get_value(f"Current {index}")
            _total_pages = dpg.get_value(f"Total {index}")

            if _name == "" or _author == "":
                _err_message = f"Invalid Value: book name and author cannot be empty"
                print(_err_message)
                errorlog(os.path.basename(__file__), _err_message)
                continue

            if _total_pages <= 0 or _current_page < 0 or _current_page > _total_pages:
                _err_message = f"Invalid Value: total pages must be greater than 0, current page must be at least 0 and less than total pages."
                print(_err_message)
                errorlog(os.path.basename(__file__), _err_message)
                continue
            
            if index == len(self._entries.book_list):
                self._entries.add_book(Book())
            
            _book = self._entries.book_list[index]

            _book.name = _name
            _book.author = _author
            _book.total_pages = _total_pages
            _book.current_page = _current_page
            
            dpg.set_item_label(f"Group {index}", f"Book {index + 1}: {_book._name}")
            dpg.set_item_user_data(f"Delete {index}", _name)
        
        _date = f"{datetime.datetime.now().strftime("%m/%d/%Y - %H:%M:%S", )}"
        dpg.set_value("Updated", f"Last Updated: {_date}")
        
        self._entries.save_data()

    def add_book_with_fields(self, name = "", author= "", current = 0, total = 1, start_open: bool = False):
        index = self._num_books
        self._num_books += 1
        with dpg.collapsing_header(label = f"Book {index + 1}: {name}", parent="Edit", before="add_book", tag=f"Group {index}", default_open=start_open): 
            dpg.add_button(
                label="Delete",
                user_data=name,
                callback=lambda x: self.delete_book(dpg.get_item_user_data(x)),
                tag=f"Delete {index}"
            )
            dpg.add_input_text(
                label="Name", 
                default_value=name,
                tag=f"Name {index}"
            )
            dpg.add_input_text(
                label="Author", 
                default_value=author,
                tag=f"Author {index}"
            )
            dpg.add_input_int(
                label="Current Page", 
                default_value=current,
                min_value=0,
                tag=f"Current {index}"
                )
            dpg.add_input_int(
                label="Total Pages", 
                default_value=total,
                min_value=1,
                tag=f"Total {index}"
            )

    def add_book(self):
        self.add_book_with_fields(start_open=True)
    
    def create_fields(self):
        for _book in self._entries.book_list:
                self.add_book_with_fields(_book.name, _book.author, _book.current_page, _book.total_pages)

    def delete_book(self, name: str):
        if name != "":
            self._entries.remove_book(self._entries.find_book(name))
            self._entries.save_data()
        for index in range(self._num_books):
            dpg.delete_item(f"Group {index}")
        self._num_books = 0
        self.create_fields()

    def close_and_show_windows(self, tag1: str, tag2: str):
        self.save()
        dpg.configure_item(tag1, show=False)
        dpg.configure_item(tag2, show=True)

    def run(self):
        # TODO: add main window for general info and redirects to edit window and view window
        with dpg.window(label="Pybook", tag="Primary", width=self._window_size[0], height=self._window_size[1]):
            with dpg.menu_bar():
                with dpg.menu(label="File"): # TODO ADD CALLBACKS!!
                    dpg.add_menu_item(label="Export")
                    dpg.add_menu_item(label="Settings")
                    dpg.add_menu_item(label="Close Application")
                with dpg.menu(label="Edit"):
                    dpg.add_menu_item(label="Edit Entries",
                        callback=lambda: self.close_and_show_windows("Primary", "Edit"))
                    dpg.add_menu_item(label="Clear All Entries")
                with dpg.menu(label="View"):
                    dpg.add_menu_item(label="View Entries")
                    dpg.add_menu_item(label="Sort Entries")
                    dpg.add_menu_item(label="Show File in Finder")
                with dpg.menu(label="About"):
                    dpg.add_menu_item(label="Documentation")
            
            dpg.add_text("Welcome to PyBook!")
            dpg.add_spacer()
            dpg.add_text("Would You Like to:")
            dpg.add_button(label="Edit Pybook Entries", tag="edit_button", width=150, height=50,
                callback=lambda: self.close_and_show_windows("Primary", "Edit"))
            dpg.add_button(label="View Pybook Entries", tag="view_button", width=150, height=50)
            dpg.add_spacer(height=12)
            with dpg.table(label="Books", tag="primary_book_table", width=self._window_size[0] - 15,
                    policy=dpg.mvTable_SizingStretchProp, borders_innerH=True, borders_outerV=True):
                dpg.add_table_column(label="Book Name")
                dpg.add_table_column(label="Author")
                dpg.add_table_column(label="Current Page")
                dpg.add_table_column(label="Total Pages")

                for _book in self._entries.book_list: # TODO update table after edit entries
                    with dpg.table_row():
                        with dpg.table_cell():
                            dpg.add_text(_book.name)
                        with dpg.table_cell():
                            dpg.add_text(_book.author)
                        with dpg.table_cell():
                            dpg.add_text(_book.current_page)
                        with dpg.table_cell():
                            dpg.add_text(_book.total_pages)
            dpg.add_spacer(height=12)

        with dpg.window(label="Entries", tag="Edit", width=self._window_size[0], height=self._window_size[1],
                 show=False):
            with dpg.menu_bar(): # TODO: Implement Menu
                with dpg.menu(label="File"):
                    dpg.add_menu_item(label="Return to Main Menu",
                        callback=lambda: self.close_and_show_windows("Edit", "Primary"))
                with dpg.menu(label="About"):
                    dpg.add_menu_item(label="Documentation") 
            dpg.add_text("PyBook Entries")
            dpg.add_button(label="Save", callback=self.save)
            dpg.add_separator()
            self.create_fields()
            
            _date = f"{datetime.datetime.now().strftime("%m/%d/%Y - %H:%M:%S", )}"
            dpg.add_button(label="Add Book", tag="add_book", callback=self.add_book)
            dpg.add_text(f"Last Updated: {_date}", tag="Updated")

        # TODO: Add view window for sorting and searching
        # dpg.set_primary_window("Primary", True)
        self.__show__()
        self.__destroy__()

def run_gui(entries: BookEntries):
    Gui(entries).run()