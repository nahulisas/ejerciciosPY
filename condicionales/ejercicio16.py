year = int(input("Ingrese un año: "))

if year%4 == 0:
    if year%100 == 0 and year%400 != 0:
        print('no es bisiesto')
    else:
        print('es bisiesto')
else:
    print('no es bisiesto')
        


