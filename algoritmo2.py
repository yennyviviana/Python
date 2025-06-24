"""Dados los resultados obtenidos en un laboratorio de análisis clínicos,
un doctor puede determinar si una persona tiene anemia o no, lo cual depende
de su nivel de hemoglobina en la sangre, de su edad y de su sexo.
Desarrollar un programa en Python que permita determinar si el resultado 
es positivo o negativo. Si el nivel de hemoglobina que tiene una persona es
menor que el rango que le corresponde, el resultado será positivo y en 
caso contrario negativo."""


def mostrar_menu():
    print("\n=== Menú de Edad y Niveles de Hemoglobina ===")
    print("1. 0 - 1 mes")
    print("2. > 1 y <= 6 meses")
    print("3. > 6 y <= 12 meses")
    print("4. > 1 y <= 5 años")
    print("5. > 5 y <= 10 años")
    print("6. > 10 y <= 15 años")
    print("7. Mujeres > 15 años")
    print("8. Hombres > 15 años")
    print("9. Salir")
    
    

def determinar_rango_hemoglobina(edad_meses, sexo):
    if edad_meses <= 1:
        return (13.0, 26.0)
    elif 1 < edad_meses <= 6:
        return (10.0, 18.0)
    elif 6 < edad_meses <= 12:
        return (11.0, 15.0)
    elif 12 < edad_meses <= 60:
        return (11.5, 15.0)
    elif 60 < edad_meses <= 120:
        return (12.6, 15.5)
    elif 120 < edad_meses <= 180:
        return (13.0, 15.5)
    else:
        if sexo.lower() == "f":
            return (12.0, 16.0)
        elif sexo.lower() == "m":
            return (14.0, 18.0)
        else:
            return None

def main():
    print("=== Evaluación de Anemia ===")
    
    try:
        edad_anios = int(input("Ingrese la edad (años): "))
        edad_meses_adicionales = int(input("Ingrese los meses adicionales (0 si no hay): "))
        sexo = input("Ingrese el sexo (M/F): ").lower()
        hemoglobina = float(input("Ingrese el nivel de hemoglobina (g/dl): "))

        edad_total_meses = edad_anios * 12 + edad_meses_adicionales
        rango = determinar_rango_hemoglobina(edad_total_meses, sexo)

        if rango is None:
            print("Sexo no válido. Use 'M' para masculino o 'F' para femenino.")
            return

        minimo, maximo = rango
        print(f"Rango normal para esa edad y sexo: {minimo} – {maximo} g/dl")

        if hemoglobina < minimo:
            print("Resultado: Positivo (Tiene anemia)")
        else:
            print("Resultado: Negativo (No tiene anemia)")

    except ValueError:
        print("Error: Por favor ingrese números válidos.")


if __name__ == "__main__":
    main()
