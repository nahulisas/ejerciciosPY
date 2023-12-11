n=int(input('eliga un numero: '))
suma = 0
contador = 1

while contador <= n:
    if n % contador == 0:
        suma = suma + 1
    contador += 1
print('el numero ',n,' tiene ',suma,' divisores')
