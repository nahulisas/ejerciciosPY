#Hacer un programa que permita al usuario elegir un número m y un n y luego muestre todos los naturales entre m y n, pero salteando de a 3.
#Por ejemplo, si el usuario ingresara un n igual a 2 y un m igual a 14, el programa deberá mostrar 2, 5, 8, 11, 14.

x = int(input("eliga un numero: "))
z = int(input("eliga otro numero: "))

for i in range (x, z + 1, 3):
    print(i)

while x <= z:
    print(x)
    x += 3
