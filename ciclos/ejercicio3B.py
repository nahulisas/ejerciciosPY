#Hacer un programa que permita al usuario elegir un número n y luego muestre los 5 números naturales que le siguen a n (n + 1, n + 2, · · · , n + 5).

x = int(input("eliga un numero: "))

for i in range (x + 1,x + 6):
    print(i)


#FIXME: Se deben imprimir los 5 numeros que le sigen a n, sin incluir n. Es decir que si elijo 14, deberian imprimirse del 15 al 19, no del 14 al 19
aux = x
while x <= aux + 5:
    print(x)
    x += 1
    