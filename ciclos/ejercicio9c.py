#Hacer un programa que permita al usuario elegir un número positivo n y luego muestre en pantalla la cantidad de divisores de n.

num = int(input('eliga un numero: '))
cant_divisores = 0
i = 1
while i <= num:
    if num % i == 0:
        cant_divisores += 1
    i += 1

print(f"El numero {num} tiene {cant_divisores} divisores")
