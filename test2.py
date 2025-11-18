def calcular_estadisticas_alumno(nombre, calificaciones):
  """
  Calcula la nota máxima, mínima y promedio de un alumno.
  Devuelve un diccionario con los resultados.
  """
  max_nota = max(calificaciones)
  min_nota = min(calificaciones)
  promedio = sum(calificaciones) / len(calificaciones)

  print(f"Estadísticas de {nombre}:")
  print(f"Nota máxima: {max_nota}")
  print(f"Nota mínima: {min_nota}")
  print(f"Promedio: {promedio:.2f}")

  return {
    "max_nota": max_nota,
    "min_nota": min_nota,
    "promedio": promedio
  }