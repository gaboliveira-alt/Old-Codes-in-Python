def convert_celsius(temperature):
    fahr_calcule = (temperature - 32) * 5//9
    print(fahr_calcule)

fahr = int(input("Temperatura: "))
convert_celsius(fahr)