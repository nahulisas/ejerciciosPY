# Hacer un programa que permita al usuario elegir un número n y luego muestre los primeros n números naturales (1, 2, · · · , n).

x = int(input("eliga un numero: "))
n = 1

if x > 1:
    #FIXME: el 0 no es un numero natural. Si el input es 17, deberia mostrar del 1 al 17, no del 0 al 16
    while n <= x:
        print(n)
        n = n+1
    for i in range (1,x+1):
        print(i)
else:
    print("El numero debe ser mayor que 0")


