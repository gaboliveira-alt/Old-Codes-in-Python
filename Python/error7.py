prices = [250, 300, "240", 400]
try:
    total = sum(prices)
    print(total)
    
except TypeError:
    print("Invalid data type")
    
print("Happy Shopping")
