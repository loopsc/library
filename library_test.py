from library import Library
from book import Book
import pytest

@pytest.fixture
def sample_library():
    library = Library("Test Library")
    book = Book("test title", 'test author', True, False)
    library.add_book(book)
    return library


def test_add_book(sample_library: Library):
    book = Book("test title2", 'test author2', True, False)
    sample_library.add_book(book)
    assert book in sample_library.book_list
    
def test_remove_book(sample_library):
    sample_library.remove_book(0)
    
    assert not sample_library.book_list
    
def test_library_rename(sample_library):
    sample_library.library_name = "New Library Name"
    assert sample_library.library_name == "New Library Name"