try:
  print(3 + "3")
except ValueError:
  print("Cannot add different types")
except TypeError:
  print("Type mismatch error")