def add(a, b):
    global alpha
    
    alpha = 500
    sum = a + b + alpha
    return sum

x = 35
y = 40
s = add(x, y)

print(x, '+',y, '=', s)
