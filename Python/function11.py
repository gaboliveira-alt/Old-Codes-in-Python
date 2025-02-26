def order(dish):
    return "Your order, " + dish

def process_order(dish, func):
    return func(dish)

print(process_order("Fish", order))
