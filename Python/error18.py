books = ["Harry Potter", "Dune", "Emma"]

try:
    print(books[5])
except IndexError:
    print("Out of range")
finally:
    print("Good lecture")
    
