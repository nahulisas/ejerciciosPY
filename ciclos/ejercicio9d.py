n = int(input('eliga un numero: '))
suma = 0
contador = 1
# for i in range(1,n+1):
#     if 10 % i == 0:
#         suma = suma + i
# print(suma)

while contador <= n:
    if n % contador ==0:
        suma = suma + contador
    contador += 1
print(suma)

