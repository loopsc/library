from library import Library
from book import Book


class BookManager:
    def __init__(self, book_list: list[Book]):
        if book_list:
            self.book_list = book_list
        else: 
            self.book_list = []
    
    