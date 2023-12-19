#Hacer un programa que permita al usuario elegir un número n y un número c, y luego muestre los c números naturales que le siguen a n (n + 1, n + 2, · · · , n + c).

n = int(input("eliga un numero: "))
c = int(input("eliga otro numero: "))
contador = 1

#FIXME: NO funciona. Si ingreso x = 10, y z = 3, deberia imprimir: 11, 12, 13
# while contador <= c:
#     n += 1
#     contador += 1
#     print(n)

for i in range (1,c+1):
    n +=1
    print(n)
 
