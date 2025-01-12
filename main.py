from book import Book
from library import Library


def main():
    library_name = input("'Owdy! What would you like to name your library?").strip()
    my_library = Library()

    while True:
        display_actions()
        user_action = input("Choice: ").strip()
        match user_action:
            case '1':
                my_library.print_all_books(library_name)
            case '2':
                while True:
                    my_library.add_book(get_book_details())

                    # If no then break out
                    if not get_yn_input("Would you like to add another book? (y/n)\n"):
                        break
            case '3':
                while True:
                    try:
                        # There is only 1 book in the list
                        if len(my_library.book_list) == 1:
                            # Ask for confirmation
                            if confirmation(f'Are you sure you would like to delete {my_library.seek_book(0)}?\n'):
                                # Delete single book
                                my_library.remove_book(0)
                            else:
                                print("Canceling deletion of book")
                                break
                        else:
                            my_library.print_all_books()
                            index = int(input(
                                "If you would like to exit delete book mode, enter any alphabetical letter.\nWhich book would you like to remove? (Type the ID): ").strip())
                            if confirmation(f'Are you sure you would like to delete {my_library.seek_book(index)}'):
                                my_library.remove_book(index)
                            else:
                                print("Exiting delete book mode...")
                                break
                    except ValueError:
                        print()
                        break

            case '4':
                book_to_search = input("What is the title of the book?\n")
                print(my_library.search_by_title(book_to_search))
            case '5':
                my_library.sort_alphabetically()
            # case '5':
            #     my_library.print_owned_books()
            # case '6':
            #     my_library.print_unowned_books()
            case 'x':
                print("Exiting program...")
                break
            case _:
                print("Invalid choice. Please try again")


# Display actions for user
def display_actions():
    print("\nChoose an action. (Enter the number)")
    print("[1] List all books")
    print("[2] Add a new book")
    print("[3] Remove a book")
    print("[4] Search book by title")
    print("[5] Sort books alphabetically")
    # print("[5] Print all owned books")
    # print("[6] Print all unowned books")
    print("[X] Exit Program")


# Helper function to get a yes/no answer and return true or false
def get_yn_input(prompt):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input == "y" or user_input == "yes":
            return True
        elif user_input == "n" or user_input == "no":
            return False
        else:
            print('Invalid input. Please try again')


# Get the details from the user about a book
# Returns a Book object
def get_book_details():
    title = input("Title: ")
    author = input("Author: ")
    read = get_yn_input("Have you read this? (y/n): ")
    owned = get_yn_input("Do you own this book? (y/n): ")

    return Book(title, author, read, owned)


def confirmation(prompt):
    while True:
        confirmation: bool = input(prompt).strip().lower()
        if confirmation in ("yes", 'y'):
            return True
        elif confirmation in ("no", "n"):
            return False
        else:
            print("Invalid input, please try again.")


if __name__ == "__main__":
    main()
