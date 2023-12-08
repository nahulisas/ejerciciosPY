a = int(input("eliga el valor inicial: "))
b = int(input("eliga el valor final: "))
c = int(input("eliga el salteo de numeros hasta llegar del inicial al final: "))

# while a <= b:
#     print(a)
#     a = a + c

for i in range (a,b+a,c):
    print(i)