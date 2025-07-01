"""Solicitar por teclado un número entero positivo entre 10 y 90 ambos incluidos 
y luego obtener, del número capturado, sus divisores y la cantidad de ellos.
Debe mostrar por pantalla todos los divisores y la cantidad de ellos.
"""


while True:
    try:
        numero = int(input("Por favor, ingrese un número entero positivo mayor entre 10 y 90: "))
        if 5 <=numero <=90:
            break
        else:
            print("Error!, el número entre 10 y 90: ")
    except:
        print("Error: Debes ingresar un número válido.")
        
        
        # Paso 2: Calcular divisores
divisores = []

for i in range(1, numero + 1):
    if numero % i == 0:
        divisores.append(i)

# Paso 3: Mostrar resultados
print(f"\nLos divisores de {numero} son: {divisores}")
print(f"Cantidad de divisores: {len(divisores)}")