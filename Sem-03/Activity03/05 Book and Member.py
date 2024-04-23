class Book:
    def __init__(self, title, author, availability=True):
        self.title = title
        self.author = author
        self.availability = availability

class Member:
    def __init__(self, name, membershipType):
        self.name = name
        self.membershipType = membershipType
        self.borrowedBooks = []

    def borrowBook(self, book):
        if book.availability:
            self.borrowedBooks.append(book)
            book.availability = False
            print(f"{self.name} has borrowed {book.title} by {book.author}")
        else:
            print(f"Sorry, {book.title} by {book.author} is not available for borrowing.")

    def returnBook(self, book):
        if book in self.borrowedBooks:
            self.borrowedBooks.remove(book)
            book.availability = True
            print(f"{self.name} has returned {book.title} by {book.author}")
        else:
            print(f"{self.name} did not borrow {book.title} by {book.author}")

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling")

member1 = Member("Alice", "Gold")
member2 = Member("Bob", "Silver")

member1.borrowBook(book1)
member2.borrowBook(book2)

member1.returnBook(book1)
member2.borrowBook(book3)
