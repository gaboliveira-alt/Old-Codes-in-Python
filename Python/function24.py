def display_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ':', value)

print(display_info(name = "Alice", age = 30, city = "New York"))
