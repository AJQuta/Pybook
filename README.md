# Pybook

A tool expanded from its version written in shell "Booker"

## Purpose

Keep track of books being read like a library. Keeps track of the name of the book, its author, the total number of pages it has, and the number of pages read in a csv file.

## How to Use

Used as a command through python3. Can be used solely in terminal, but also has a GUI version (in progress). To run the main program run `./pybook` or `python3 pybook`. The command requres everything in requirements.txt. It mainly uses dearpygui for the gui in progress.

### The Basics

For command help run:

    `./pybook`
    
This will show a list of commands for adding books, deleting books, outputting info of a book, and a few others.

To add a book run:

    `./pybook add "<name_of_book>"`
    
This will ask for more input to generate the book in the csv.

To delete a book run:

    `./pybook del "<name_of_book>"
    
This will ask for confirmation and then delete the book from the csv.
