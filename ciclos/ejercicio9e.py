#Hacer un programa que permita al usuario elegir dos números positivos c y n y luego muestre en pantalla los primeros c divisores de n

n = int(input('eliga un numero: '))
c = int(input('eliga un numero menor al anterior: '))

# contador = 0
# suma = 1

# if n > c:
#     while contador < c:
#         if  n % suma == 0:
#             print(suma)
#             contador += 1
#         suma += 1
# else:
#     print('el numero debe ser menor al anterior')

divisores_de_n = 0
for i in range (1, n + 1):
    if n % i == 0:
        divisores_de_n += 1
        if divisores_de_n <= c:
            print(i)
        
    