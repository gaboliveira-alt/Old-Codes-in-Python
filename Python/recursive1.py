def ifib(n):
    t1 = 0
    t2 = 1
    for k in range(n):
        t = t1 + t2
        t2 = t1
        t1 = t
    return t

fibs = [None]*100

def dfib(n):
    global fibs
    
    if fibs[n]:
        return fibs[n]
    
    if n == 1 or n == 2:
        return 1
    fibs[n] =  rfib(n - 1) + rfib(n - 2)
    return fibs[n]

def rfib(n):
    if n == 1 or n == 2:
        return 1
    return rfib(n - 1) + rfib(n - 2)

def main():
    print('** CALCULO DO N-ESIMO TERMO DA SERIE DE FIBBONNACI **\n')
    
    n = int(input("Valor de N: "))
    
    print(f'fib{n} = {ifib(n)}\t(versão interativa)')
    print(f'fib{n} = {dfib(n)}\t(versão dinamica)')
    print(f'fib{n} = {rfib(n)}\t(versão recursiva)')

if __name__ == '__main__':
    main()
    