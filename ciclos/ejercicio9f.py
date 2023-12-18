#Hacer un programa que permita al usuario elegir dos números positivos c y n y luego muestre en pantalla los últimos c divisores de n.

n=int(input('eliga un numero: '))
c=int(input('eliga un numero menor al anterior: '))

contador = 0
for i in range(n + 1, 1, -1):
    if n % i == 0:
        contador += 1
        if contador <= c:
            print(i)
        



