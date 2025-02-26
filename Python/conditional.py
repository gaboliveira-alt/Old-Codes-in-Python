print('Verifica o sinal de um numero inteiro\n')

number = int(input("Informe um numero inteiro: "))


if number > 0:
    result = "POSITIVO"
elif number < 0:
    result = "NEGATIVO"
else:
    result = "ZERO"
    

print(f'O número {number} é {result}.')

