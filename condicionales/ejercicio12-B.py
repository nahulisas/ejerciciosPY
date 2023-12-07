nota1 = int(input("ingrese la nota del alumo: "))
nota2 = int(input("ingrese la nota del alumo: "))
nota3 = int(input("ingrese la nota del alumo: "))
prom = (nota1 + nota2 + nota3) / 3
if prom <= 3:
    print("el promedio es",prom,"Reprobado")
elif prom > 3 and prom <=6:
    print("el promedio es",prom,"Debe rendir examen final")
else:
    print("el promedio es",prom,"Eximido")