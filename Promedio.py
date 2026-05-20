"""
Sistema de Calificaciones - promedio.py

Este script solicita el nombre de un alumno y tres calificaciones,
calcula el promedio matemático y determina si el alumno aprobó o reprobó
basándose en una nota mínima de 70.

Autor: Demi
Herramienta de documentación recomendada: Sphinx
"""

def calcular_promedio(cal1, cal2, cal3):
    """
    Calcula la media aritmética de tres calificaciones.

    Args:
        cal1 (float): La primera calificación.
        cal2 (float): La segunda calificación.
        cal3 (float): La tercera calificación.

    Returns:
        float: El promedio obtenido de las tres notas.
    """
    promedio = (cal1 + cal2 + cal3) / 3
    return promedio


def mostrar_resultado(nombre, promedio):
    """
    Muestra en pantalla el reporte del alumno y su estado académico.

    Si el promedio es igual o mayor a 70, el alumno se considera 'APROBADO'.
    De lo contrario, se muestra como 'REPROBADO'.

    Args:
        nombre (str): Nombre completo del estudiante.
        promedio (float): Promedio final calculado.
    """
    print("\nAlumno:", nombre)
    print("Promedio:", promedio)

    if promedio >= 70:
        print("Resultado: APROBADO")
    else:
        print("Resultado: REPROBADO")


# --- Bloque Principal del Programa ---
if __name__ == "__main__":
    print("=== SISTEMA DE CALIFICACIONES ===")

    # Captura de datos del usuario
    nombre = input("Ingresa el nombre del alumno: ")

    cal1 = float(input("Ingresa la primera calificación: "))
    cal2 = float(input("Ingresa la segunda calificación: "))
    cal3 = float(input("Ingresa la tercera calificación: "))

    # Procesamiento
    promedio_final = calcular_promedio(cal1, cal2, cal3)

    # Salida de datos
    mostrar_resultado(nombre, promedio_final)
  
