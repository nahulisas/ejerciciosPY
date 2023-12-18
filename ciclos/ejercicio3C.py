#Hacer un programa que permita al usuario elegir un número n y un número c, y luego muestre los c números naturales que le siguen a n (n + 1, n + 2, · · · , n + c).

x = int(input("eliga un numero: "))
z = int(input("eliga otro numero: "))

#FIXME: NO funciona. Si ingreso x = 10, y z = 3, deberia imprimir: 11, 12, 13
if x < z:
    for i in range (x,z):
        print(i)
    while x < z:
        x = x + 1
        print(x)
else:
    print("el segundo valor debe ser mayor al primero")
    
