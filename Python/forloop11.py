def fibonnaci(number):
    n1 = 0
    n2 = 1
    
    for _ in range(number):
        n = n1 + n2
        n2 = n1
        n1 = n
    return n


number = int(input("Fibonnaci: "))

print(fibonnaci(number))

