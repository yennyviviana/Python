
print("=============================")
print("Bienvenido al juego de aventuras en el bosque encantado")
print("=============================")
print("Tu meta es aventurarte por el bosque encantado")
nombre = input("Escribe tu nombre: ")



print("\n Tus opcuiones son: ")
print("\n Entrar al bosque")
print("\n  Buscar un objeto mágico")
print("\n Salir del juego ")



# Manejo de excepciones
try:
    # Capturar la elección del jugador
    eleccion = int(input("\n¿Qué elección deseas escoger? (1, 2 o 3): "))

    # Procesar la elección del jugador con estructuras selectivas
    if eleccion == 1:
        print("\nHas escogido Entrar al bosque.")
        camino = input("¿Por qué camino deseas ir? (iluminado/oscuro): ").lower()

        if camino == "iluminado":
            print("\nHas llegado a un hermoso lago.")
            descanso = input("¿Quieres descansar aquí? (s/n): ").lower()
            if descanso == "s":
                print("Descansaste y recuperaste energía. ¡Buena elección!")
            else:
                print("Decides seguir explorando sin descansar.")
        
        elif camino == "oscuro":
            print("\nTe has adentrado en un bosque oscuro lleno de criaturas mágicas.")
            accion = input("Te encuentras con una criatura mágica. ¿Quieres luchar o negociar? (luchar/negociar): ").lower()
            if accion == "luchar":
                print("Luchaste contra la criatura pero perdiste algo de energía.")
            elif accion == "negociar":
                print("Lograste negociar con la criatura y ganaste un objeto mágico.")
            else:
                print("No tomaste una decisión válida, la criatura desaparece.")

        else:
            print("No has escogido un camino válido.")

    elif eleccion == 2:
        print("\nHas escogido Buscar un objeto mágico.")
        print("Los objetos mágicos disponibles son:")
        print("1. Espada mágica (te ayudará en combate).")
        print("2. Escudo encantado (te protege mejor en batallas).")
        print("3. Poción curativa (te permite recuperar energía).")
        
        objeto = int(input("Elige el número del objeto que deseas: "))
        
        if objeto == 1:
            print("Has obtenido una Espada mágica. ¡Ahora eres más fuerte!")
        elif objeto == 2:
            print("Has obtenido un Escudo encantado. ¡Ahora tienes más defensa!")
        elif objeto == 3:
            print("Has obtenido una Poción curativa. ¡Podrás recuperar energía cuando la necesites!")
        else:
            print("No has seleccionado un objeto válido.")

    elif eleccion == 3:
        print("\nHas escogido Salir del juego. ¡Gracias por jugar!")

    else:
        print("Error: opción no válida. Debes elegir 1, 2 o 3.")

except ValueError:
    print("Error: Debes ingresar un número válido.")
