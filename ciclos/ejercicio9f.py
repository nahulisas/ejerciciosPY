n=int(input('eliga un numero: '))
c=int(input('eliga un numero menor al anterior: '))

contador = 1

for i in range (n+1,1,-1):
    if n % i == 0:
        if contador <= c:
            print(i)
            contador += 1
        



