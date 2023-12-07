tarifaFija = 480
impuestos = 78
bonificacion = 200
costeInicial = tarifaFija + impuestos
print("el coste inicial del servicios es de $",costeInicial,"con un consumo de 0kw")
consumo = int(input("ingrese el consumo realizado: "))
consumoTotal = consumo - bonificacion
costeTotal = (25.5 * consumoTotal) + costeInicial
print('el coste total del servicios es de $',costeTotal,"por un total de",consumoTotal,"KW consumido")






