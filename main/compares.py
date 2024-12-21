#!/usr/bin/env python3

import os.path
from typing import Callable
from main.entries import Book
from main.errorlog import errorlog

def _compare_by_name(a: Book, b: Book) -> int:
    if a.name < b.name or (a.name == b.name and a.author < b.author):
        return -1
    if a.name == b.name and a.author == b.author:
        return 0
    return 1

def _compare_by_author(a: Book, b: Book) -> int:
    if a.author < b.author or (a.author == b.author and a.name < b.name):
        return -1
    if a.author == b.author and a.name == b.name:
        return 0
    return 1

def _compare_by_total_pages(a: Book, b: Book) -> int:
    if a.total_pages > b.total_pages:
        return 1
    if a.total_pages < b.total_pages:
        return -1
    if _compare_by_name(a,b) == 0 and _compare_by_author(a,b) == 0:
        return 0
    if _compare_by_name(a,b) == 1 or (_compare_by_name(a,b) == 0 and _compare_by_author(a,b) == 1):
        return 1
    return -1

def _compare_by_current_page(a: Book, b: Book) -> int:
    if a.current_page > b.current_page:
        return 1
    if a.current_page < b.current_page:
        return -1
    if _compare_by_name(a,b) == 0 and _compare_by_author(a,b) == 0:
        return 0
    if _compare_by_name(a,b) == 1 or (_compare_by_name(a,b) == 0 and _compare_by_author(a,b) == 1):
        return 1
    return -1

def compare(selector: str = "name") -> Callable:
    if selector == "name":
        return _compare_by_name
    if selector == "author":
        return _compare_by_author
    if "total" in selector:
        return _compare_by_total_pages
    if "current" in selector:
        return _compare_by_current_page
    
    err_message = f"ERR: Invalid Function Selector {selector}."
    print(err_message)
    errorlog(os.path.basename(__file__), err_message)
    raise ValueError(err_message)