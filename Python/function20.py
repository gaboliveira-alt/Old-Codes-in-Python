def total(*args):
    result = 0
    for arg in args:
        result += arg
    return result

print(total(1, 2, 3, 4, 5))
print(total(1, 2, 3, 4, 5, 6, 7))
print(total(1, 2, 3))


        