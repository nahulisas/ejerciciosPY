num1 = int(input('ingrese un valor: '))
num2 = int(input('ingrese un valor distinto al anterior: '))
if num1 < num2:
    aux = num2
    num2 = num1
    num1 = aux
print(num1,num2)
