numbers = []
while True:
    data = int(input())
    if data == 0:
        break
    numbers.append(data)
    
    for elems in numbers[::-1]:
        print(elems, end=' ')
    print()
    
    