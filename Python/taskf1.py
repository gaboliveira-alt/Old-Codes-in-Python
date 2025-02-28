
def elevation_number(word, number):
    if word == "quadrado":
        result = pow(number, 2)
    elif word == "cubo":
        result = pow(number, 3)
    return result


word = input("Quadrado ou Cubo? ")
number = int(input("Numero: "))

print(elevation_number(word, number))