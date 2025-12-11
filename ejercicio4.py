import pandas as pd

print("\n--- EJERCICIO 4: Pandas Básico ---")

#Crear datos de ejemplo
datos = {
    'Alumno': ['Ana', 'Luis', 'Carlos', 'Marta'],
    'Nota': [8.5, 7.3, 9.0, 4.7],
    'Aprobado': [True, True, True, False]
}
#Crear DataFrame
df = pd.DataFrame(datos)

#Mostrar DataFrame - Tabla completa
print("\n--- Tabla de Notas ---")
print(df)

#Filtrar: Notas superiores a 8
print("\n--- Alumnos con Nota > 8 ---")
destacados = df[df['Nota'] > 8]
print(destacados)

#Calcular promedio de notas
promedio = df['Nota'].mean()
print(f"\n--- Promedio de Notas: {promedio:.2f} ---")
#print(f"\n--- Promedio de Notas: {promedio} ---")


#{promedio:.2f} formatea el valor de 'promedio' como un número decimal con dos cifras decimales,    
#lo que es útil para mostrar promedios o valores numéricos de manera más legible.

    