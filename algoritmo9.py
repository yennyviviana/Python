"""Un banco está ofreciendo interés al 0.7% mes vencido a la cantidad 
de meses que el cliente desee. Se requiere una aplicación que le proyecte 
a un cliente cuánto dinero obtendrá si deposita un capital determinado
a un número de meses, esta información se debe capturar por teclado. 
Se debe mostrar por pantalla el capital mes a mes hasta el número de meses capturado"""


opcion = ""

while opcion != "2":
    print("\nMenu inicial")
    print("1. Proyectar capital con interés 0.7% mensual")
    print("2. Salir")
    
    opcion = input("Seleccione una opción: ")

    if opcion == "1": 
        print("\nProyección del capital:")
        capitalPrincipal = float(input("Ingrese el capital inicial: "))
        meses = int(input("Ingrese el número de meses: "))
        
        tasa = 0.007
        capital = capitalPrincipal
        
        for mes in range(1, meses + 1):
            capital *= (1 + tasa)
            print(f"Capital después de {mes} mes:  ${capital:.2f}")
        
        print(f"\nCapital final después de {meses} meses: ${capital:.2f}")
    
    elif opcion == "2":
        print(f"Gracias por utilizar esta aplicación.")
        break
    
    else:
        print("Opción inválida")
