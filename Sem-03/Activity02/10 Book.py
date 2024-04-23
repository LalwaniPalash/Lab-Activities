class Book:
    def __init__(self, title, author, genre, publicationYear):
        self.title = title
        self.author = author
        self.genre = genre
        self.publicationYear = publicationYear

    def printBookInfo(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nGenre: {self.genre}\nPublication Year: {self.publicationYear}"

    def sameGenre(self, other_book):
        return self.genre == other_book.genre

book1 = Book("To Kill a Mockingbird", "Harper Lee", "Fiction", 1960)
book2 = Book("1984", "George Orwell", "Science Fiction", 1949)
book3 = Book("Pride and Prejudice", "Jane Austen", "Fiction", 1813)

print("Book 1 Info:")
print(book1.printBookInfo())
print()

print("Book 2 Info:")
print(book2.printBookInfo())
print()

print("Book 3 Info:")
print(book3.printBookInfo())
print()

print("Are Book 1 and Book 2 from the same genre?", book1.sameGenre(book2))
print("Are Book 1 and Book 3 from the same genre?", book1.sameGenre(book3))
