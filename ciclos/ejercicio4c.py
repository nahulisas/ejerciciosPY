#Hacer un programa que permita al usuario elegir un número n, un m y un p y luego muestre todos los naturales entre m y n, pero salteando de a p números. 
#Por ejemplo, si el usuario ingresara un n igual a 2 y un m igual a 14, y un p igual a 4, el programa deberá mostrar 2, 6, 10, 14.

a = int(input("eliga el valor inicial: "))
b = int(input("eliga el valor final: "))
c = int(input("eliga el salteo de numeros hasta llegar del inicial al final: "))

for i in range (a, b + a, c):
    print(i)

while a <= b:
    print(a)
    a = a + c
