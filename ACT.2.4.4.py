print("Bienvenido a tu programa de Boleteria")
pasajes = int(input("Igresa el numero pasajes deseas vender:\n"))
print(f"Has vendido un total de: {pasajes} Pasajes")
ingresos = 0
for i in range(pasajes):
    while True:
        try:
            precio_pasajes = float(input(f"Ingrese el precio del pasaje {i+1}: "))
            ingresos += precio_pasajes
            break
        except ValueError:
            print("Debes ingresar un valor numerico valido para el precio del pasaje")
print(f"\nEl Total de Ingresos por la venta de pasajes es: ${ingresos}")

    