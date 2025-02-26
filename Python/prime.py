print("** VERIFICAR SE UM INTEIRO POSITIVO É PRIMO **\n")

number = int(input("Informe um inteiro: "))

abs_number = abs(number)

prime = (abs_number != 0) and (abs_number != 1)

d = 2
while d < abs_number:
    if abs_number % d == 0:
        prime = False
        break
    d = d + 1
    

if prime:
    print(number, 'é PRIMO')
else:
    print(number, 'não é PRIMO')
    

