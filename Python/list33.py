n = int(input('Informe ordem da matriz: '))

m = []
for i in range(n):
    m.append([0] * n)
    m[i][i] = 1
    
for row in m:
    for elem in m:
        print(elem, end=' ')
    print()
    
    