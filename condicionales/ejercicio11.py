num1 = int(input("ingrese el primer valor: "))
num2 = int(input("ingrese el segundo valor: "))
num3 = int(input("ingrese el tercer valor: "))

if num1 > num2 and num1 > num3:
    print(num1,"es el mnayor")
elif num2 > num1 and num2 > num3:
    print(num2,"es el mnayor")
elif num3 > num1 and num3 > num2:
    print(num3,"es el mnayor")
else:
    print('los numeros son iguales')

