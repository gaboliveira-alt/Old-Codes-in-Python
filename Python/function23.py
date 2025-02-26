def show_items(category, *items):
    print("Category: " + category)
    for item in items:
        print(item)
        
print(show_items("Eletronics", "Laptop", "Smarthphone", "Tablet"))
