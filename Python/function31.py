def uppercase(func):
    def wrapper():
        origin_message = func()
        modified_message = origin_message.upper()
        return modified_message
    return wrapper

@uppercase
def greet():
    return "Welcome"

print(greet())
