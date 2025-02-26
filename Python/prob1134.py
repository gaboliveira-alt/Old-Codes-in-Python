purchase = {
    1: 0,
    2: 0,
    3: 0,
}

while True:
    fuel_type = int(input())
    if fuel_type == 4:
        break
    
    if (fuel_type >= 1) and (fuel_type <= 3):
        purchase[fuel_type] += 1


print('Muito Obrigado')
print('Alcool:', purchase[1])
print('Gasolina:', purchase[2])
print('Diesel:', purchase[3])
