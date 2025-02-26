def ifat(n):
    fat = 1
    for k in range(1, n + 1):
        fat *= k
    return fat

def rfat(n):
    if n == 0:
        return 1
    return n * rfat(n - 1)


def main():
    print('** CALCULO DO FATORIAL DE N **\n')
    
    n = int(input('Valor de N: '))
    
    print(f'{n} = {ifat(n)}')
    print(f'{n} = {rfat(n)}')
    
    
if __name__ == '__main__':
    main()
