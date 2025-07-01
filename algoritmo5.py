"""Fedepapa tiene como política fijar un precio inicial al kilo de papa, 
la cual se clasifica en Pastusa y Sabanera, y además en tamaños 1 y 2.
Cuando se realiza la venta del producto, ésta es de un solo tipo y tamaño.
Se requiere determinar cuánto recibirá un productor por la papa que entrega 
en una venta, considerando lo siguiente: si es Pastusa, tiene un recargo 
de $2000 al precio inicial cuando es de tamaño 1; y $3000 si es de tamaño 2. 
Si es Sabanera, se rebajan $4000 cuando es de tamaño 1, y $5000 cuando es de 
tamaño 2. Realice un programa en Python para determinar la ganancia obtenida.
"""

print("\n Ganancia obtenida")
print("\n Papa Sabanera")
print("\n Papa Pastusa")


# Función que calcula el valor que recibirá el productor...
def clasificar_papas(tipo, tamano, precio_inicial):
    if tipo == "Pastusa":
        if tamano == 1:
            return precio_inicial + 2000
        elif tamano == 2:
            return precio_inicial + 3000
    elif tipo == "Sabanera":
        if tamano == 1:
            return precio_inicial - 4000
        elif tamano == 2:
            return precio_inicial - 5000


# Validar tipo de papa.....
while True:
    tipo = input("Ingrese el tipo de papa (Pastusa o Sabanera): ").capitalize()
    if tipo in ["Pastusa", "Sabanera"]:
        break
    else:
        print("Tipo inválido. Debe ser 'Pastusa' o 'Sabanera'.")


# Validar tamaño de papa.....
while True:
    try:
        tamano = int(input("Ingrese el tamaño (1 o 2): "))
        if tamano in [1, 2]:
            break
        else:
            print("Tamaño inválido. Debe ser 1 o 2.")
    except ValueError:
        print("Debe ingresar un número entero.")


# Validar precio inicial.....
while True:
    try:
        precio_inicial = int(input("Ingrese el precio inicial por kilo: "))
        if precio_inicial >= 0:
            break
        else:
            print("El precio debe ser un número positivo.")
    except ValueError:
        print("Debe ingresar un número entero.")


# Calcular y mostrar el total.....
total = clasificar_papas(tipo, tamano, precio_inicial)
print(f"\nEl productor recibirá: ${total}")
