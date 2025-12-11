"""
Solución 01: Fundamentos de Python
Soluciones a los ejercicios básicos
"""

# Ejercicio 1: Variable con nombre y edad
nombre = "Juan Pérez"
edad = 25
print(f"Nombre: {nombre}, Edad: {edad}")

# Ejercicio 2: Función que calcula el área de un rectángulo
def area_rectangulo(base, altura):
    return base * altura

print(f"Área rectángulo (5x3): {area_rectangulo(5, 3)}")

# Ejercicio 3: Función que determina si un número es par o impar
def es_par(numero):
    return numero % 2 == 0

print(f"¿Es 4 par? {es_par(4)}")
print(f"¿Es 7 par? {es_par(7)}")

# Ejercicio 4: Lista con 5 colores
colores = ["rojo", "azul", "verde", "amarillo", "morado"]
print(f"Tercer color: {colores[2]}")

# Ejercicio 5: Diccionario con información de estudiante
estudiante = {
    "nombre": "María García",
    "edad": 20,
    "curso": "Programación Python"
}
print(f"Estudiante: {estudiante}")

# Ejercicio 6: Bucle que imprime números del 1 al 10
print("Números del 1 al 10:")
for i in range(1, 11):
    print(i, end=" ")
print()

# Ejercicio 7: Función que convierte Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return celsius * 9/5 + 32

print(f"25°C en Fahrenheit: {celsius_a_fahrenheit(25)}°F")
print(f"0°C en Fahrenheit: {celsius_a_fahrenheit(0)}°F")

# Ejercicio 8: Suma de elementos en una lista
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
suma = 0
for numero in numeros:
    suma += numero
print(f"Suma total: {suma}")

# Alternativa usando sum()
suma_alternativa = sum(numeros)
print(f"Suma total (con sum()): {suma_alternativa}")

# Ejercicio 9: Función que encuentra el máximo
def encontrar_maximo(lista):
    if not lista:
        return None
    maximo = lista[0]
    for elemento in lista:
        if elemento > maximo:
            maximo = elemento
    return maximo

# Alternativa usando max()
def encontrar_maximo_v2(lista):
    return max(lista) if lista else None

print(f"Máximo de [3,7,2,9,1]: {encontrar_maximo([3,7,2,9,1])}")
print(f"Máximo de [3,7,2,9,1] (v2): {encontrar_maximo_v2([3,7,2,9,1])}")

# Ejercicio 10: Programa que saluda al usuario
# Nota: Para ejecutar esta parte, descomenta las siguientes líneas:
# nombre_usuario = input("¿Cómo te llamas? ")
# print(f"¡Hola, {nombre_usuario}! Bienvenido/a.")

print("\n=== Todas las soluciones completadas ===")
