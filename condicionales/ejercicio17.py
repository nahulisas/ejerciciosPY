a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
x = 0
if a > 0:
    if b > 0:
        x = -b / a
    else:
        x = (-b) / a
else:
    if b > 0:
        x = -b / -a
    else:
        x = (-b) / -a
print(x)

    

