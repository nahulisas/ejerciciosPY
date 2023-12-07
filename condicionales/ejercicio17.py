a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))

if a > 0:
    if b > 0:
        x = -b / a
        print(x)
    else:
        x = (-b) / a
        print(x)
else:
    if b > 0:
        x = -b / -a
        print(x)
    else:
        x = (-b) / -a
        print(x)

    

