nota = int(input("ingrese la nota del alumo: "))
if nota <= 3:
    print("Reprobado")
elif nota > 3 and nota <=6:
    print("Debe rendir examen final")
else:
    print("Eximido")