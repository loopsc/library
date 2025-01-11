
class Book:
    def __init__(self, title: str, author, read_status, owned_status):
        self.title = title
        self.author = author
        self.read_status = read_status
        self.owned_status = owned_status

    # Change Title
    def change_title(self, title):
        self.title = title

    # Change Author
    def change_author(self, author):
        self.author = author

    # Change Status
    def change_read_status(self, read_status):
        self.read_status = read_status

    # Change Owned
    def change_owned_status(self, owned_status):
        self.owned_status = owned_status

    # Custom print statement
    def __str__(self):
        return f'Title: {self.title}\nAuthor: {self.author}\nStatus: {self.read_status}\nOwnership: {self.owned_status}'
