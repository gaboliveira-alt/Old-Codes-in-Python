
password = "Nelson"


count = 0
while count < 3:
    try_password = input("Acerte a senha: ")
    
    if try_password != password:
        print("Incorret")
        count += 1
        continue
    print("Acess")
    break







