# Hacer un programa que permita al usuario elegir un número positivo n y luego muestre en pantalla todos los divisores de n.

n = int(input("ingrese un numero: "))
i = 1
while i <= n:
    if n % i == 0:
        print(i)
    i +=1

for i in range (1, n + 1):
    if n % i == 0:
        print(i)
