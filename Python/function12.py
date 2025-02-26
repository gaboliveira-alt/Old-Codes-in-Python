def welcome(name):
    return "Welcome, " + name

def bye(name):
    return "Goodbye, " + name

def process_user(name, func):
    return func(name)

print(process_user("Alice", welcome))
print(process_user("Bob", bye))

