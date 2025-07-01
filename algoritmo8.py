"""Capturar por teclado un número entero mayor que 0 y menor que 5000, 
se debe establecer en qué rango se encuentra el número 2 de acuerdo con 
las siguientes características: rango alto mayor que 4000, rango medio
entre 2000 y 4000 ambos incluidos y rango bajo menor que 2000. 
El programa debe implementar un ciclo que permita validar que el número 
sea mayor a 0, en caso de que el número ingresado sea menor a 0 se debe volver 
a solicitar al usuario que ingrese el número este procedimiento se debe repetir
hasta que el número ingresado sea mayor a 0.
"""

while True:
    try:
        numero = int(input("Ingrese un número entero mayor que 0: "))
        if numero > 0:
            break
        else:
            print("Error: el número debe ser mayor que 0.")
    except ValueError:
        print("Error: debe ingresar un número entero válido.")


# Clasificar el número según el rango
if numero > 4000:
    print("Rango alto")
elif 2000 <= numero <= 4000:
    print("Rango medio")
else:
    print("Rango bajo")
