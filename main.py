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
    print(my_library.get_library_name())
    
    # Loops until user correctly enters for new or existing library
    while my_library.get_library_name() == 'temp':
        choose_new_existing()

    while True:
        display_actions(my_library.get_library_name())
        user_action = input("Choice: ").strip().lower()
        match user_action:
            # Prints all books
            case '1':
                my_library.print_all_books()
            # Add a new book
            case '2':
                while True:
                    my_library.add_book(get_book_details())

                    # If no then break out
                    if not get_yn_input("\nWould you like to add another book? (y/n)\n"):
                        break
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
                                "If you would like to exit delete book mode, enter any alphabetical letter.\nWhich book would you like to remove? (Type the ID): ").strip())
                            if get_yn_input(f'Are you sure you would like to delete {my_library.seek_book(index)}'):
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
            # Save books to file
            case 's':
                my_library.save_books(f'{my_library.get_library_name()}')
            case 'b':
                confirmation = get_yn_input(
                    "This will delete all newly added changes. Please ensure you have saved the data to file. Continue? (y/n) ")
                # If yes
                if confirmation:
                    my_library.wipe()

                    # Delete the temp csv file
                    delete_temp_csv()
                    # Ask user if create new file or choose existing file
                    choose_new_existing()
                elif not confirmation:
                    pass
            case 'x':
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
    print('[s] Save books to file')
    print('[b] Go back')
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


def get_book_details():
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


def choose_new_existing():
    while True:
        create_new = input(
            "Please enter [n] for creating a new library or [e] for viewing an existing library.\nOr press [x] to quit. ").strip().lower()

        # Create a list of all pre-existing libraries
        existing_libraries = create_list_libraries()

        # Creating a new library
        if create_new == "new" or create_new == "n":

            library_name = input(
                "\nWhat would you like to name your library?\nOr press [x] to quit. ").strip()
            
            duplicate_flag = False
            
            if library_name == "x" or library_name == "X":
                # Go back to the start of the first while loop
                break
            else:
                for library in existing_libraries:
                    if library == library_name:
                        duplicate_flag = True
                    
                if duplicate_flag:
                    print("Invalid name. This library already exists.")
                else:
                    my_library.set_library_name(library_name)

                    print(f"Welcome to {library_name}.")

                    with open(f'{library_name}.csv', 'w') as file:
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

                if f'{get_existing_library}' in existing_libraries:
                    my_library.set_library_name(get_existing_library)
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
