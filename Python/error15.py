ages = [18, 24, 43, 56]
try:
    print(ages[10])
except IndexError:
    print("Out of range")
    