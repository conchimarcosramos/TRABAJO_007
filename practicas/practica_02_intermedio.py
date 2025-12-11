"""
Práctica 02: Nivel Intermedio de Python
Conceptos intermedios y estructuras de datos avanzadas
"""

# Ejercicio 1: List comprehensions
print("=== Ejercicio 1: List Comprehensions ===")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [n for n in numeros if n % 2 == 0]
cuadrados = [n ** 2 for n in numeros]

print(f"Números originales: {numeros}")
print(f"Números pares: {pares}")
print(f"Cuadrados: {cuadrados}")

# Ejercicio 2: Manipulación de strings
print("\n=== Ejercicio 2: Manipulación de Strings ===")
texto = "Python es un lenguaje de programación"

print(f"Texto original: {texto}")
print(f"Mayúsculas: {texto.upper()}")
print(f"Minúsculas: {texto.lower()}")
print(f"Título: {texto.title()}")
print(f"Palabras: {texto.split()}")
print(f"Longitud: {len(texto)}")
print(f"Reemplazar: {texto.replace('Python', 'JavaScript')}")

# Ejercicio 3: Tuplas
print("\n=== Ejercicio 3: Tuplas ===")
coordenadas = (10, 20)
persona = ("Ana", 28, "Barcelona")

print(f"Coordenadas: {coordenadas}")
print(f"X: {coordenadas[0]}, Y: {coordenadas[1]}")
print(f"Persona: {persona}")
print(f"Nombre: {persona[0]}, Edad: {persona[1]}, Ciudad: {persona[2]}")

# Ejercicio 4: Sets (conjuntos)
print("\n=== Ejercicio 4: Sets (Conjuntos) ===")
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {4, 5, 6, 7, 8}

print(f"Conjunto A: {conjunto_a}")
print(f"Conjunto B: {conjunto_b}")
print(f"Unión: {conjunto_a | conjunto_b}")
print(f"Intersección: {conjunto_a & conjunto_b}")
print(f"Diferencia (A-B): {conjunto_a - conjunto_b}")

# Ejercicio 5: Funciones con argumentos variables
print("\n=== Ejercicio 5: Funciones con *args y **kwargs ===")

def sumar_todos(*numeros):
    return sum(numeros)

def mostrar_info(**kwargs):
    for clave, valor in kwargs.items():
        print(f"  {clave}: {valor}")

print(f"Suma de 1,2,3,4,5: {sumar_todos(1, 2, 3, 4, 5)}")
print("Información de persona:")
mostrar_info(nombre="Carlos", edad=35, profesion="Ingeniero")

# Ejercicio 6: Lambda functions
print("\n=== Ejercicio 6: Funciones Lambda ===")
cuadrado = lambda x: x ** 2
suma = lambda a, b: a + b
es_mayor = lambda x: x > 10

print(f"Cuadrado de 5: {cuadrado(5)}")
print(f"Suma de 3 y 7: {suma(3, 7)}")
print(f"¿15 es mayor que 10? {es_mayor(15)}")

# Ejercicio 7: Map, Filter, Reduce
print("\n=== Ejercicio 7: Map y Filter ===")
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x ** 2, numeros))
pares = list(filter(lambda x: x % 2 == 0, numeros))

print(f"Números: {numeros}")
print(f"Cuadrados (map): {cuadrados}")
print(f"Pares (filter): {pares}")

# Ejercicio 8: Manejo de archivos
print("\n=== Ejercicio 8: Manejo de Archivos ===")

import tempfile
import os

# Escribir archivo (usando tempfile para compatibilidad multiplataforma)
temp_dir = tempfile.gettempdir()
archivo_path = os.path.join(temp_dir, 'ejemplo.txt')

with open(archivo_path, 'w') as archivo:
    archivo.write("Primera línea\n")
    archivo.write("Segunda línea\n")
    archivo.write("Tercera línea\n")
print("Archivo escrito correctamente")

# Leer archivo
with open(archivo_path, 'r') as archivo:
    contenido = archivo.read()
    print("Contenido del archivo:")
    print(contenido)

# Ejercicio 9: Iteración sobre diccionarios
print("=== Ejercicio 9: Iteración sobre Diccionarios ===")
estudiantes = {
    "Juan": 85,
    "María": 92,
    "Pedro": 78,
    "Ana": 95
}

print("Notas de estudiantes:")
for nombre, nota in estudiantes.items():
    print(f"  {nombre}: {nota}")

# Ejercicio 10: Enumerate y Zip
print("\n=== Ejercicio 10: Enumerate y Zip ===")
frutas = ["manzana", "banana", "naranja"]
precios = [1.2, 0.5, 0.8]

print("Enumerate:")
for indice, fruta in enumerate(frutas, 1):
    print(f"  {indice}. {fruta}")

print("\nZip:")
for fruta, precio in zip(frutas, precios):
    print(f"  {fruta}: ${precio}")
