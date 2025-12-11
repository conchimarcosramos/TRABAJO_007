"""
Solución 02: Nivel Intermedio
Soluciones a los ejercicios intermedios
"""

# Ejercicio 1: List comprehension para cuadrados
cuadrados = [x ** 2 for x in range(1, 11)]
print(f"Cuadrados del 1 al 10: {cuadrados}")

# Ejercicio 2: Función que cuenta vocales
def contar_vocales(texto):
    vocales = "aeiouAEIOU"
    return sum(1 for letra in texto if letra in vocales)

print(f"Vocales en 'Python': {contar_vocales('Python')}")
print(f"Vocales en 'Programación': {contar_vocales('Programación')}")

# Ejercicio 3: Filtrar números pares
def filtrar_pares(numeros):
    return [n for n in numeros if n % 2 == 0]

# Alternativa con filter
def filtrar_pares_v2(numeros):
    return list(filter(lambda x: x % 2 == 0, numeros))

print(f"Pares de [1,2,3,4,5,6]: {filtrar_pares([1,2,3,4,5,6])}")

# Ejercicio 4: Frecuencia de palabras
def frecuencia_palabras(texto):
    palabras = texto.lower().split()
    frecuencia = {}
    for palabra in palabras:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    return frecuencia

# Alternativa con Counter
from collections import Counter
def frecuencia_palabras_v2(texto):
    return dict(Counter(texto.lower().split()))

print(f"Frecuencia: {frecuencia_palabras('hola mundo hola python mundo')}")

# Ejercicio 5: Elementos comunes entre dos listas
def elementos_comunes(lista1, lista2):
    return list(set(lista1) & set(lista2))

# Alternativa con list comprehension
def elementos_comunes_v2(lista1, lista2):
    return [x for x in lista1 if x in lista2]

print(f"Comunes entre [1,2,3] y [2,3,4]: {elementos_comunes([1,2,3], [2,3,4])}")

# Ejercicio 6: Calcular promedio con *args
def calcular_promedio(*numeros):
    if not numeros:
        return 0
    return sum(numeros) / len(numeros)

print(f"Promedio de 1,2,3,4,5: {calcular_promedio(1,2,3,4,5)}")
print(f"Promedio de 10,20,30: {calcular_promedio(10,20,30)}")

# Ejercicio 7: Contar líneas de un archivo
import tempfile
import os

def contar_lineas(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            return len(archivo.readlines())
    except FileNotFoundError:
        return 0

# Crear un archivo de ejemplo para probar (multiplataforma)
temp_dir = tempfile.gettempdir()
ejemplo_path = os.path.join(temp_dir, 'ejemplo_lineas.txt')

with open(ejemplo_path, 'w') as f:
    f.write("Línea 1\nLínea 2\nLínea 3\n")

print(f"Líneas en archivo: {contar_lineas(ejemplo_path)}")
print(f"Líneas en archivo inexistente: {contar_lineas(os.path.join(temp_dir, 'no_existe.txt'))}")

# Ejercicio 8: Función lambda que duplica
duplicar = lambda x: x * 2
print(f"Duplicar 5: {duplicar(5)}")
print(f"Duplicar 10: {duplicar(10)}")

# Ejercicio 9: Convertir Celsius a Fahrenheit con map
celsius = [0, 10, 20, 30, 40]
fahrenheit = list(map(lambda c: c * 9/5 + 32, celsius))
print(f"Celsius: {celsius}")
print(f"Fahrenheit: {fahrenheit}")

# Ejercicio 10: Invertir diccionario con dict comprehension
original = {"a": 1, "b": 2, "c": 3}
invertido = {valor: clave for clave, valor in original.items()}
print(f"Original: {original}")
print(f"Invertido: {invertido}")

# Ejemplos adicionales
print("\n=== Ejemplos adicionales ===")

# List comprehension con condición
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares_cuadrados = [x ** 2 for x in numeros if x % 2 == 0]
print(f"Cuadrados de pares: {pares_cuadrados}")

# Uso de zip con múltiples listas
nombres = ["Ana", "Luis", "Carmen"]
edades = [25, 30, 28]
ciudades = ["Madrid", "Barcelona", "Valencia"]

personas = list(zip(nombres, edades, ciudades))
print(f"Personas: {personas}")

# Dict comprehension con transformación
palabras = ["python", "java", "javascript"]
longitudes = {palabra: len(palabra) for palabra in palabras}
print(f"Longitudes: {longitudes}")

print("\n=== Todas las soluciones completadas ===")
