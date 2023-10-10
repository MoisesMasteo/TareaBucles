cantidad = int(input("Cuanto capital quieres invertir? "))
interes = int(input("Inserte el interés anual: "))
años = int(input("Durante cuantos años? "))

for i in range (años):
    cantidad = cantidad * (1 + interes/100)
    print("El capital será de ", cantidad, "euros.")