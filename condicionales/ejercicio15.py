a = int(input('ingrese un valor A: '))
b = int(input('ingrese un valor B: '))
c = int(input('ingrese un valor C: '))

if a < b:
    if a < c:
        if b < c:
            print(a,b,c)
        else:
            print(a,c,b)
    else:
        if b < c:
            print(b,c,a)
        else:
            print(c,a,b)
else:
    if c < b:
        print(c,b,a)
    else:
        print(b,c,a)

            







