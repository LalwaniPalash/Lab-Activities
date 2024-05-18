class LibraryResource:
    def __init__(self, title, author, is_available=True):
        self.title = title
        self.author = author
        self.is_available = is_available

class Book(LibraryResource):
    def __init__(self, title, author, genre, is_available=True):
        super().__init__(title, author, is_available)
        self.genre = genre

class Audiobook(LibraryResource):
    def __init__(self, title, author, narrator, is_available=True):
        super().__init__(title, author, is_available)
        self.narrator = narrator

def check_availability(resource):
    if resource.is_available:
        print(f"{resource.title} by {resource.author} is available for borrowing.")
    else:
        print(f"{resource.title} by {resource.author} is not available for borrowing.")

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction", True)
check_availability(book1)

audiobook1 = Audiobook("The Hobbit", "J.R.R. Tolkien", "Andy Serkis", False)
check_availability(audiobook1)
