from book import Book
import csv


class Library:
    def __init__(self, library_name):
        self.book_list: list[Book] = []
        self._library_name = library_name

    @property
    def library_name(self):
        return self._library_name

    @library_name.setter
    def library_name(self, new_name: str):
        if new_name.strip():
            self._library_name = new_name
        else:
            raise ValueError("Invalid. Name cannot be empty")

    # TODO: Edit add book system

    def add_book(self, book_to_add):
        self.book_list.append(book_to_add)

    # Remove a book from the library
    def remove_book(self, index):
        try:
            # Pop removes an item at a specific index and also returns the value which we store in a variable to print
            removed_book = self.book_list.pop(index)
            print(f'Removed {removed_book.title} by {removed_book.author}')
        except IndexError as e:
            print(e)

    # Given an index, return the title of the book
    def seek_book(self, index):
        if self.book_list:
            return self.book_list[index].title

    def load_books(self, filename):
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file, delimiter='\t')

            # Skips the header row
            next(reader)

            for row in reader:
                # Avoiding empty rows
                if row:
                    title, author, read_status, owned_status = row
                    # converts to boolean
                    # read_status = read_status.strip().lower() == 'true'
                    if read_status.strip().lower() == "true":
                        read_status = True
                    else:
                        read_status = False
                    if owned_status.strip().lower() == "true":
                        owned_status = True
                    else:
                        owned_status = False

                    book = Book(title, author, read_status, owned_status)
                    self.book_list.append(book)

    def save_books(self, filename):
        # Open the file in writing mode
        with open(f'{filename}.csv', 'w', newline='') as file:
            writer = csv.writer(file, delimiter='\t')

            # Write headers
            writer.writerow(['title', 'author', 'read_status', 'owned_status'])

            # Loop through the library object and write data to file
            for book in self.book_list:
                writer.writerow(
                    [book.title, book.author, book.read_status, book.owned_status])

        print("Books successfully saved to file!\n")

    # Prints all books in the library
    def print_all_books(self):
        print(f"Library: '{self.library_name}'\n")
        if self.book_list:
            # Enumerate function loops through an interable while keeping track of the index for the current item.
            for index, book in enumerate(self.book_list):
                print(f'ID:{index}\n{book}\n')
        else:
            print("No books in library")

    # Search for a book in the library using title
    # Returns the book or if not found then a message
    def search_by_title(self, title: str):
        if self.book_list:
            for book in self.book_list:
                # Non strict search e.g 'test' will return, if user types 'est'
                if title.lower().strip() in book.title.lower().strip():
                    return f'\nBook found!\n\n{book}\n'
                else:
                    return f'\nNot book {title} found.'
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
            print("Library sorted.\n")
        else:
            print("No books in library\n")

    # Clear the contents of the library
    def wipe(self):
        self.book_list.clear()
