books = ["Harry Potter", "Dune", "Emma"]

try:
    choice = books[1]
except IndexError:
    print("Out of Range")
else:
    print(choice + " is a great choice!")
    