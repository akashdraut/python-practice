
class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, PublicationYear: {self.publication_year}"


book1 = Book("Title1", "Author1", 2009)
book2 = Book("Title2", "Author2", 2012)

print(book1)
print(book2)


