#Hacer un programa que permita al usuario elegir un número m y un n y luego muestre todos los naturales entre m y n (m, m + 1, m + 2, · · · , n − 1, n).
#Qué pasa si n es menor que m?


x = int(input('eliga el primer numero '))
y = int(input('eliga el segundo numero '))

#FIXME: el 0 no es un numero natural. Si elijo imprimir los numeros entre el 0 y 25 deberia imprimir desde el 1 al 25, no desde el 0 al 25
for i in range (x, y + 1, 1):
    print(i)


#FIXME: el 0 no es un numero natural. Si elijo imprimir los numeros entre el 0 y 25 deberia imprimir desde el 1 al 25, no desde el 0 al 25
while x <= y:
    print(x)
    x += 1

