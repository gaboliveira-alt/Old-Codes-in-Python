products = ["Table", "Sofa", "Cushion", "Bookshelf", "Vase"]

filtered_prod = list(filter(lambda name: len(name) == 4, products))

print(filtered_prod)
