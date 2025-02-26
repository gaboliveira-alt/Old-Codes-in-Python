try:
    print(len(5))
except NameError:
    print("Variable is not defined")
except TypeError:
    print("Not iterable")
    
    