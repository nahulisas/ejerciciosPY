num1 = int(input('ingrese un valor: '))
num2 = int(input('ingrese un valor distinto al anterior: '))
if num1 > num2:
    print(num1,"es mayor que",num2)
elif num2 > num1:
    print(num2,"es mayor que",num1)
else:
    print("los numeros son iguales")