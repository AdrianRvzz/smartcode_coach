def calc_promedio_notas(alumno, notas, ponderaciones, extra_credit=0):
    """
    Calcula el promedio ponderado de un alumno, considerando notas y ponderaciones.
    Imprime el resultado y la calificación según el promedio.
    """
    suma_notas = 0
    suma_pesos = 0

    for i in range(len(notas)):
        suma_notas += notas[i] * ponderaciones[i]
        suma_pesos += ponderaciones[i]

    if suma_pesos == 0:
        return 0

    promedio = suma_notas / suma_pesos + extra_credit

    # Imprimir resultados
    print(f"El promedio del alumno {alumno} es: {promedio:.2f}")

    if promedio >= 90:
        print("Excelente")
    elif promedio >= 80:
        print("Muy bien")
    elif promedio >= 70:
        print("Bien")
    else:
        print("Necesita mejorar")

    return promedio
 