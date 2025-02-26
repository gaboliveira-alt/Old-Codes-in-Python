names = ["alice", "bob", "CHARLIE", "dEborah"]

def capitalizer(name):
    return name.capitalize()

capitalized = map(capitalizer, names)

capitalized = list(capitalized)

print(capitalized)