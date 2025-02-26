def stock_status_decorator(func):
    def wrapper(item):
        result = func(item)
        print(result, ": stoc status for", item)
        return result
    return wrapper


@stock_status_decorator
def restock_item(item):
    return "Restocked"

@stock_status_decorator
def sell_item(item):
    return "Sold"

print(restock_item("Laptop"))
print(sell_item("Smarthphone"))