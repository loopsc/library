from book import Book
from library import Library


def main():
    my_library = Library()

    while True:
        my_library.add_book(get_book_details())

        # If no then break out
        if not get_yn_input("Would you like to add another book? (y/n)\n"):
            break

    while True:
        display_actions()
        user_action = input("Choice: ").strip()
        match user_action:
            case '1':
                my_library.print_all_books()
            case '2':
                my_library.add_book(get_book_details())
            case '3':
                while True:
                    try:
                        my_library.print_all_books()
                        index = int(input("If you would like to cancel, enter any letter.\nWhich book would you like to remove? (Type the ID): ").strip())
                        my_library.remove_book(index)
                        break
                    except ValueError:
                        print()
                        break
                        
            case '4':
                book_to_search = input("What is the title of the book? ")
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


if __name__ == "__main__":
    main()
