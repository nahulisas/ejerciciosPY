# Hacer un programa que permita al usuario elegir un número positivo n y luego muestre en pantalla el 
# producto (es decir, la multiplicación) de los numeros entre 1 y n.
n = int(input('eliga un numero mayor a 0: '))
producto_de_n = 1
for i in range (1,n):
    producto_de_n = producto_de_n * (i+1)
print(producto_de_n)
    

