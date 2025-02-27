number = int(input("Number: "))
fact = number

while number >= 2:
    fact = fact * (number - 1)
    number -= 1
print(fact)
    