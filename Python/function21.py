def total(*prices):
    result = 0
    for arg in prices:
        result += arg
    return result

print(total(1, 2, 3, 4, 5, 6, 7))