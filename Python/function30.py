def greet():
    return "Welcome"

def uppercase(func):
        def wrapper():
            origin_message = func()
            modified_message = origin_message.upper()
            return modified_message
        return wrapper
    
greet_uper = uppercase(greet)
print(greet_uper())
            
        