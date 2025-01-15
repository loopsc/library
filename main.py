from book import Book
from library import Library
# os enables interaction with the file system
import os
# glob allows for matching of file extensions
import glob

# TODO: ensure 'in' is used correctly. typing es for yes shouldnt be possible

my_library = None


def main():
    print('Howdy!')
    if my_library.library_name == 'temp':
        # pass
        print(f'library name: {my_library.library_name}')
    else:
        print(my_library.library_name())

    # Loops until user correctly enters for new or existing library
    while my_library.library_name == 'temp':
        choose_new_existing_library()

    while True:
        display_actions(my_library.library_name)
        user_action = input("Choice: ").strip().lower()
        print()
        match user_action:

            # Prints all books
            case '1':
                my_library.print_all_books()

            # Add a new book
            case '2':
                while True:
                    book_to_add: Book = prompt_book_details()

                    # If library is not empty
                    if my_library.book_list:
                        duplicate_spotted = False

                        for book in my_library.book_list:
                            if book.title.lower() == book_to_add.title.lower():
                                duplicate_spotted = True

                        # Checking if a duplicate entry is found
                        if duplicate_spotted:
                            confirmation = get_yn_input(
                                f"\nDuplicate title spotted. Are you sure you want to add '{book_to_add.title}'? ")
                            print()

                            # Checking if the user would still like to add
                            # if duplicate is found
                            if confirmation:
                                my_library.add_book(book_to_add)
                                print(
                                    f'\n{book_to_add.title} was successfully added to the library.\n')
                                break
                            else:
                                print(f'{book_to_add.title} was not added.')
                                print()
                                break
                        else:
                            my_library.add_book(book_to_add)
                    else:
                        my_library.add_book(book_to_add)

                    my_library.add_book(prompt_book_details())

                    # If no then break out
                    if not get_yn_input("\nWould you like to add another book? (y/n)\n"):
                        break

            # Remove a book
            case '3':
                while True:
                    try:
                        # There is only 1 book in the list
                        if len(my_library.book_list) == 1:
                            # Ask for confirmation
                            if get_yn_input(f'Are you sure you would like to delete {my_library.seek_book(0)}?\n'):
                                # Delete single book
                                my_library.remove_book(0)
                            else:
                                print("Canceling deletion of book")
                                break
                        else:
                            my_library.print_all_books()
                            index = int(input(
                                "To exit enter [x]\nWhich book would you like to remove? (Enter the ID): ").strip())

                            if get_yn_input(f'Are you sure you would like to delete {my_library.seek_book(index)}'):
                                my_library.remove_book(index)
                            else:
                                print("Canceling deletion...")
                                print()
                                break
                    except ValueError:
                        print("Exiting delete mode...")
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
            # Save books to file
            case 's':
                my_library.save_books(f'{my_library.library_name}')
            case 'b':
                confirmation = get_yn_input(
                    "This will delete all newly added changes. Please ensure you have saved the data to file. Would you still like to go back? (y/n) ")
                # If yes
                if confirmation:
                    my_library.wipe()

                    # Delete the temp csv file
                    delete_temp_csv()
                    # Ask user if create new file or choose existing file
                    choose_new_existing_library()
                elif not confirmation:
                    pass
            case 'x':
                confirmation = get_yn_input(
                    "This will delete all newly added changes. Please ensure you have saved the data to file. Would you still like to go back? (y/n) ")
                if confirmation:
                    print("Exiting program...")
                    delete_temp_csv()
                    break
            case _:
                print("Invalid choice. Please try again")


# Display actions for user
def display_actions(library_name):
    print(f"Choose an action for '{library_name}'. (Enter the number)")
    print("[1] List all books")
    print("[2] Add a new book")
    print("[3] Remove a book")
    print("[4] Search book by title")
    print("[5] Sort books alphabetically")
    # print("[5] Print all owned books")
    # print("[6] Print all unowned books")
    print('---------------------------------------------')
    print('[s] Save books to file')
    print('[b] Choose another library')
    print("[x] Exit Program")


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
def prompt_book_details():
    title = input("Title: ")
    author = input("Author: ")
    read = get_yn_input("Have you read this? (y/n): ")
    owned = get_yn_input("Do you own this book? (y/n): ")

    return Book(title, author, read, owned)


def list_all_libraries():
    # Create a list to store all found csv files
    all_libraries = glob.glob('**/*.csv', recursive=True)

    print("\nExisting libraries:")
    for library in all_libraries:
        print(f'- {os.path.splitext(os.path.basename(library))[0]}')


def create_list_libraries():
    libraries_list = []
    all_libraries = glob.glob('**/*.csv', recursive=True)
    for library in all_libraries:
        libraries_list.append(os.path.splitext(os.path.basename(library))[0])
    return libraries_list


# Asks the user of they want to create a new library or view an existing one
def choose_new_existing_library():
    while True:
        create_new = input(
            "Enter [n] to create new library or [e] for viewing an existing library.\nPress [x] to quit. ").strip().lower()

        # Create a list of all pre-existing libraries
        existing_libraries = create_list_libraries()

        # Creating a new library
        if create_new == "new" or create_new == "n":

            input_library_name = input(
                "\nWhat would you like to name your library?\nOr press [x] to quit. ").strip()

            duplicate_flag = False

            if input_library_name == "x" or input_library_name == "X":
                # Go back to the start of the first while loop
                break
            else:
                for library in existing_libraries:
                    if library == input_library_name:
                        duplicate_flag = True

                if duplicate_flag:
                    print("Invalid name. This library already exists.")
                else:
                    my_library.library_name = input_library_name

                    print(f"Welcome to {my_library.library_name}.")

                    with open(f'{input_library_name}.csv', 'w') as file:
                        pass
            break

        # Editing an existing library
        elif create_new == "existing" or create_new == "e":
            # Call function to list all existing library csv files
            list_all_libraries()

            existing_libraries = create_list_libraries()

            # Loops until user correctly enters a valid file name
            while True:
                # Ask the user, which library they want to view
                get_existing_library = input(
                    "\nWhat is the name of the library you wish to view?\n").strip().lower()
                print()

                if f'{get_existing_library}' in existing_libraries:
                    my_library.library_name = get_existing_library
                    # Load books from csv into the library object
                    my_library.load_books(f'{get_existing_library}.csv')
                    break
                else:
                    print(
                        "\nThis library does not exist. Please ensure you have typed the name correctly")
            break
        elif create_new == "x" or create_new == "X":
            exit()
        else:
            print('Invalid input, please try again')


# Delete the temp file
def delete_temp_csv():
    try:
        os.remove('temp.csv')
    except:
        pass


def initialize_library():
    global my_library
    my_library = Library('temp')


if __name__ == "__main__":
    initialize_library()
    main()
