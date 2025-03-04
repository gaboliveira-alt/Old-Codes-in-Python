import random


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    

class Library:
    def __init__(self, name):
        self.name = name
        self.__books = []
    
    def add_book(self, book):
        if not isinstance(book, Book):
            raise Exception("Parameter is not a Book instance")
        self.__books.append(book)
    
    def __get_colums_width(self):
        max_title_len = 0
        max_author_len = 0
        
        for books in self.__books:
            max_title_len = max(len(books.title), max_title_len)
            max_author_len = max(len(books.author), max_author_len)
            
        table_len = max_title_len + max_author_len + 1
        lib_len = len(self.name)
        
        if table_len < lib_len:
            max_title_len += max_title_len - table_len
            table_len = lib_len
        return (table_len, max_title_len, max_author_len)
    
    def show_books(self):
        table_width, title_width, author_width = self.__get_colums_width()
        
        print('-' * table_width)
        
        padding = (table_width - len(self.name)) // 2
        print('', padding, self.name.upper(), sep='')
        print('-' * table_width)
        print('%-s %s %s' % (title_width, 'TITULO', 'AUTOR'))
        print('-' * title_width, '-' * author_width)
        
        for book in self.__books:
            print('%-s %s %s' % (title_width, book.title, book.author))
        
        print('-' * table_width)
        

def main():
    global lib 
    
    lib = Library('Bibilioteca Central')
    for _ in range(15):
        title = f'Titulo da Obra {random.randint(500, 5000)}'
        author = f'Autor da Obra {random.randint(500, 5000)}'
        book = Book(title, author)
        lib.add_book(book)
        
    lib.show_books()

if __name__ == '__main__':
    main()
        