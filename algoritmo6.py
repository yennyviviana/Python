"""Se necesita diseñar un algoritmo que permita mostrar por pantalla 
una cantidad de elementos de la serie de Fibonacci, para esto se debe 
capturar un número entero positivo mayor que 1 por el teclado y esa debe 
ser la cantidad elementos a mostrar.
"""

print("\n Serie de Fibonacci")


while True:
    try:
        num_positivo = int(input("Por favor, ingrese un número entero positivo mayor a 1: "))
        if num_positivo > 1:
            break
        else:
            print("Error!, el número es 0, o negativo")
    except:
        print("Error: Debes ingresar un número válido.")



# Mostrar la serie de Fibonacci.....
anterior = 0
actual = 1
print("\nSerie de Fibonacci:")
print(anterior, end=" ")
print(actual, end=" ")

for  i in range(2, num_positivo):
    siguiente = anterior + actual
    print(siguiente, end=" ")
    anterior, actual = actual, siguiente
