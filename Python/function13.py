def book_title(title):
    return "Book title: " + title

def info(title, func):
    return func(title)

print(info("Great Gasby", book_title))

