def greet(name):
    print("Hey", name)
    
    def account():
        return "Your account is created"
    
    message = account()
    return message


print(greet("Bob"))

