#Hacer un programa que permita al usuario elegir un número positivo n y luego muestre en pantalla la suma de los divisores de n.

n = int(input('eliga un numero: '))
suma_de_divisores = 0
i = 1
# for i in range(1,n+1):
#     if 10 % i == 0:
#         suma = suma + i
# print(suma)

while i <= n:
    if n % i == 0:
        suma_de_divisores += i
    i += 1

print(suma_de_divisores)
