# Pybook

A tool expanded from its version written in shell "Booker"

## Purpose

Keep track of books being read like a library. Keeps track of the name of the book, its author, the total number of pages it has, and the number of pages read in a csv file.

## How to Use

Used as a command through a shell executable. Can be used solely in shell, but also has a GUI version (in progress). The executable is called "pybook". It uses the built-in python environment for pybook, so while the program is in use, `python` and `python3` will resolve to the version of python used in the virtual environment (3.12).

### The Basics

For command help:

    Run `pybook`.
    
This will show a list of commands for adding books, deleting books, outputting info of a book, and a few others.

To add a book:

    Run `pybook add "<name_of_book>"`.
    
This will ask for more input to generate the book in the csv.

To delete a book:

    Run `pybook del "<name_of_book>"`.
    
This will ask for confirmation and then delete the book from the csv.
