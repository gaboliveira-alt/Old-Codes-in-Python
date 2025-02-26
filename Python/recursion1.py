def ifib(n):
    t1 = 0
    t2 = 1
    for k in range(n):
        t = t1 + t2
        t2 = t1
        t1 = t
    return t


def rfib(n):
    if n == 1 or n == 2:
        return 1
    return rfib(n - 1) + rfib(n - 2)


def main():
    print('** CALCULO DO N ESIMO TERMO DA SERIE DE FIBONNACI **\n')
    
    n = int(input('Valor de N: '))
    
    print(f'{n} = {ifib(n)}')
    print(f'{n} = {rfib(n)}')
    
    
if __name__ == '__main__':
    main()
