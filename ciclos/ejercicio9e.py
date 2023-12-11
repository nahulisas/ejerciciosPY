n=int(input('eliga un numero: '))
c=int(input('eliga un numero menor al anterior: '))
contador = 1
# contador = 0
# suma = 1

# if n > c:
#     while contador < c:
#         if  n % suma == 0:
#             print(suma)
#             contador += 1
#         suma += 1
# else:
#     print('el numero debe ser menor al anterior')

for i in range (1,n+1):
    if n % i == 0:
        if contador <=c:
            print(i)
            contador += 1
        
            

    
       
    