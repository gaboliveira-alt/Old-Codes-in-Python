colors = ['Red', 'Yellow', 'Green']
try:
    print(colors[10])
except IndexError:
    print("Index Range")
except NameError:
    print("Variable is not defined")
    
print("Happy Shopping")
