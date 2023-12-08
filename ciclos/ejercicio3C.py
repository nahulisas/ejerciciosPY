x = int(input("eliga un numero: "))
z = int(input("eliga otro numero: "))
if x < z:
    # while x < z:
    #     x = x + 1
    #     print(x)
    for i in range (x,z):
        print(i)
else:
    print("el segundo valor debe ser mayor al primero")
    
