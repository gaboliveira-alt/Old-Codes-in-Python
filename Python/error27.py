print("Inicio do Programa")

try:
    r1 = int(input("Informe o valor 1: "))
    r2 = int(input("Informe o valor 2: "))
    result_r = r1 / r2
    print(f'{r1} / {r2} = {result_r}')
except ValueError:
    print("Os valores devem ser numericos")
except ZeroDivisionError:
    print("o 2o valor não pode ser zero")
else:
    print("Codigo executado com sucesso")
finally:
    print("Ocorreu algum erro")

