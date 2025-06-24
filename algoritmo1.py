"""Realizar un programa en Python que calcule el total a pagar en entradas 
al estadio el CAMPIN. El estadio cuenta con los siguientes sectores codificados 
y sus respectivos precios:
Sectores del estadio: A- Norte alta $15.000,B- Norte baja $13.000,C- Oriental alta $10.000
D- Occidental alta $11.000,E- Exclusivo $20.000
El programa debe imprimir:
Precio Unitario de la boleta,Cantidad de entradas compradas,Total a pagar
Nota: Validar que la cantidad de boletas debe ser un entero positivo.
"""

def mostrar_menu():
    print("\nEstadio El CAMPÍN - Sectores disponibles:")
    print("A - Norte alta      $15.000")
    print("B - Norte baja      $13.000")
    print("C - Oriental alta   $10.000")
    print("D - Occidental alta $11.000")
    print("E - Exclusivo       $20.000")

def obtener_precio(codigo):
    precios = {
        "A": 15000,
        "B": 13000,
        "C": 10000,
        "D": 11000,
        "E": 20000
    }
    return precios.get(codigo.upper(), None)

def leer_codigo():
    while True:
        codigo = input("Seleccione el código del sector (A-E): ").upper()
        if codigo in ['A', 'B', 'C', 'D', 'E']:
            return codigo
        else:
            print("Código inválido. Intente nuevamente.")

def registrar_compras():
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de boletas (entero positivo): "))
            if cantidad > 0:
                return cantidad
            else:
                print("Debe ingresar un número mayor que cero.")
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")

def main():
    mostrar_menu()
    codigo = leer_codigo()
    precio_unitario = obtener_precio(codigo)

    if precio_unitario is None:
        print("No se pudo obtener el precio del sector.")
        return

    cantidad = registrar_compras()
    total_pagar = cantidad * precio_unitario

    print("\n--- Detalle de la Compra ---")
    print(f"Sector seleccionado: {codigo}")
    print(f"Precio unitario: ${precio_unitario:,.0f}")
    print(f"Cantidad de entradas: {cantidad}")
    print(f"Total a pagar: ${total_pagar:,.2f}")


if __name__ == "__main__":
    main()



