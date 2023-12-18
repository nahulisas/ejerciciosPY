#Hacer un programa que reciba un número n (n > 0) y muestre las n primeras potencias de 2.
#Por ejemplo, si el usuario ingresa 6, el programa mostrará: 1 2 4 8 16 32.

n = int(input('Por favor eliga un numero: '))
cont = 1
p = 1
while cont <= n:
    print(p)
    p *= 2
    cont += 1

#Otra forma de hacerlo:
for i in range(0, n):
    print(2 ** i)