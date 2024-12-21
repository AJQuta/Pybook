from typing import Callable
from main.compares import compare
from main.entries import Book

def _sort_helper(books: list[Book], comp: Callable) -> list[Book]:
    if len(books) == 2:
        if comp(books[0], books[1]) == 1:
            temp = books[0]
            books[0] = books[1]
            books[1] = temp
    if len(books) <= 2:
        return books
    
    length = len(books)
    first = _sort_helper(books[:length // 2], comp)
    second = _sort_helper(books[length // 2:], comp)

    result: list[Book] = []
    first_i, second_i = 0, 0
    len_first = len(first)
    len_second = len(second)

    while first_i < len_first and second_i < len_second:
        if comp(first[first_i], second[second_i]) == 1:
            result.append(second[second_i])
            second_i += 1
        else:
            result.append(first[first_i])
            first_i += 1
    
    for book in first[first_i:]:
        result.append(book)
    
    for book in second[second_i:]:
        result.append(book)

    return result

def sort(books: list[Book], selector) -> list[Book]:
    return _sort_helper(books, compare(selector))