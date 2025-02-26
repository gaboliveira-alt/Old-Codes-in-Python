choice = int(input())

coffes = ["lattes", "macchiato", "espresso"]
try:
    print(coffes[choice])
except IndexError:
    print("Escolha 0, 1 ou 2")
    
