
tabu = int(input("Insira um numero: "))

limit = int(input("Limite: "))

for tabu_mult in range(1, limit + 1):
    print(f"Tabuada: {tabu}, {tabu} x {tabu_mult} = {tabu * tabu_mult}")
