from book import Book


class Library:
    def __init__(self):
        self.book_list: list[Book] = []

    # Add a book to the library
    def add_book(self, book_to_add: Book):
        # If book list is not empty
        if self.book_list:
            duplicate_spotted = False
            # Iterate through the entire library, and if there is a duplicate, set flag to True
            for book in self.book_list:
                if book.title.lower() == book_to_add.title.lower():
                    duplicate_spotted = True
            
            # If duplicate was spotted then ask for confirmation
            if duplicate_spotted:
                confirmation = input(f"Duplicate title spotted. Are you sure you want to add {book_to_add.title}? (y/n)\n").strip().lower()
                if confirmation in ("yes", "y"):
                    self.book_list.append(book_to_add)
                    print(f'{book_to_add.title} was successfully added to the library.\n')
                elif confirmation in ("no", "n"):
                    return
                else:
                    print("Invalid input. Add book failed.\n")
                    return
        # If library is empty, add book  
        else:
            self.book_list.append(book_to_add)
            print(f'{book_to_add.title} was successfully added to the library.\n')

    # Remove a book from the library
    def remove_book(self, index):
        # index = input("Which book would you like to remove? (Type the index) ").strip()

        try:
            # Pop removes an item at a specific index and also returns the value which we store in a variable to print
            removed_book = self.book_list.pop(index)
            print(f'Removed {removed_book.title} by {removed_book.author}')
        except IndexError as e:
            print(e)

    # List all books in the library

    def print_all_books(self):
        if self.book_list:
            # Enumerate function loops through an interable while keeping track of the index for the current item.
            for index, book in enumerate(self.book_list):
                print(f'\nID:{index}\n{book}')
        else:
            print("No books in library")

    # Search for a book in the library using title
    # Returns the book or if not found then a message
    def search_by_title(self, title: str):
        if self.book_list:
            for book in self.book_list:
                # Non strict search e.g 'test' will return, if user types 'est'
                if title.lower().strip() in book.title.lower().strip():
                    return f'Book found!\n{book}'
        else:
            return f'No books in library'

    # Print all owned books
    def print_owned_books(self):
        if self.book_list:
            # Set a flag variable to be false,
            # this it made True if at least one owned book is found in the library
            has_owned_books = False
            
            for book in self.book_list:
                if book.owned_status:
                    print(book)
                    has_owned_books = True
                    
            if not has_owned_books:
                print("No owned books in the library.\n")
        else:
            print("No books in library\n")
        
    # Print all unowned books
    def print_unowned_books(self):
        if self.book_list:
            has_unowned_book = False
            for book in self.book_list:
                if not book.owned_status:
                    print(book)
                    has_unowned_book = True
            
            if not has_unowned_book:
                print("No unowned books in the library\n")
        else:
            print("No books in library\n")
            
    # Print all read books
    def print_read_books(self):
        if self.book_list:
            # Set a flag variable to be false,
            # this it made True if at least one owned book is found in the library
            has_read_books = False
            
            for book in self.book_list:
                if book.read_status:
                    print(book)
                    has_read_books = True
                                        
            if not has_read_books:
                print("No read books in the library.\n")
        else:
            print("No books in library\n")

    # Print all unread books
    def print_unread_books(self):
        if self.book_list:
            has_unread_book = False
            for book in self.book_list:
                if not book.read_status:
                    print(book)
                    has_unread_book = True
            
            if not has_unread_book:
                print("No unread books in the library\n")
        else:
            print("No books in library\n")

    # Soft books by title alphabetical order
    def sort_alphabetically(self):
        if self.book_list:
            # Key is a property of the sort() function that sorts by the key.
            # Lambda function creates a single use nameless one line function.
            # Provide book to the function as a variable, which we use to sort via book.title
            self.book_list.sort(key=lambda book: book.title.lower())
        else:
            print("No books in library\n")