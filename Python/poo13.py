class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def describe_book(self):
        print(self.title, "by", self.author)
    
    @classmethod
    def book_in_series(cls, series_name, number_of_books):
        print("There are:", series_name, "books in the", number_of_books)

my_book = Book("Harry Potter and Sorceres Stone", "J.K Rowlling")

my_book.describe_book()

Book.book_in_series("Harry Potter", 7)

        