a = int(input('ingrese un valor A: '))
b = int(input('ingrese un valor B: '))
c = int(input('ingrese un valor C: '))

if a > b:
    aux = b
    b = a
    a = aux
if b > c:
    aux = c
    c = b
    b = aux
if a > b:
    aux = b
    b = a
    a = aux
print(a,b,c)


    