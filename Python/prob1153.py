n = int(input())

factorial = 1

for term in range(1, n + 1):
    factorial *= term
    
print(factorial)
