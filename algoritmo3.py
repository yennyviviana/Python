"""
Desarrollar un programa en Python que permita simular el siguiente juego:
El planeta Centauro está en guerra! En dicho planeta existe una raza de
malvados leales a Throm que luchan contra otra raza benévola que no quieren
que el mal reine en el planeta.
"""

# Valores asignados a cada raza
benevolos = {
    "ositos": 1,
    "principes": 2,
    "enanos": 3,
    "caris": 4,
    "fulos": 5
}

malvados = {
    "lolos": 2,
    "fulanos": 2,
    "hoggins": 2,
    "lurcos": 3,
    "trollis": 5
}

# Función para calcular el poder total de un ejército
def calcular_poder(ejercito, razas):
    poder_total = 0
    for raza, valor in razas.items():
        try:
            cantidad = int(input(f"¿Cuántos {raza} hay en el ejército? "))
            poder_total += cantidad * valor
        except ValueError:
            print("Valor inválido, se tomará como 0.")
    return poder_total

def main():
    print("== PLANETA CENTAURO: BATALLA ENTRE EL BIEN Y EL MAL ==")

    print("\nEjército Benévolo:")
    poder_bien = calcular_poder("bien", benevolos)

    print("\nEjército Malvado:")
    poder_mal = calcular_poder("mal", malvados)

    print("\n--- RESULTADO DE LA BATALLA ---")
    print(f"Poder del Bien: {poder_bien}")
    print(f"Poder del Mal: {poder_mal}")

    if poder_bien > poder_mal:
        print("¡Gana el Bien!")
    elif poder_mal > poder_bien:
        print("¡Gana el Mal!")
    else:
        print("Es un empate.")


if __name__ == "__main__":
    main()
