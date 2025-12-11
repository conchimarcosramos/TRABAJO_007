"""
Práctica 01: Fundamentos de Python
Conceptos básicos de programación en Python
"""

# Ejercicio 1: Variables y tipos de datos
# Crea variables de diferentes tipos y muestra sus valores

print("=== Ejercicio 1: Variables y tipos de datos ===")
nombre = "Juan"
edad = 25
altura = 1.75
es_estudiante = True

print(f"Nombre: {nombre} (tipo: {type(nombre).__name__})")
print(f"Edad: {edad} (tipo: {type(edad).__name__})")
print(f"Altura: {altura} (tipo: {type(altura).__name__})")
print(f"Es estudiante: {es_estudiante} (tipo: {type(es_estudiante).__name__})")

# Ejercicio 2: Operaciones aritméticas
print("\n=== Ejercicio 2: Operaciones aritméticas ===")
a = 10
b = 3

suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b
division_entera = a // b
modulo = a % b
potencia = a ** b

print(f"{a} + {b} = {suma}")
print(f"{a} - {b} = {resta}")
print(f"{a} * {b} = {multiplicacion}")
print(f"{a} / {b} = {division}")
print(f"{a} // {b} = {division_entera}")
print(f"{a} % {b} = {modulo}")
print(f"{a} ** {b} = {potencia}")

# Ejercicio 3: Condicionales (if/else)
print("\n=== Ejercicio 3: Condicionales ===")
numero = 15

if numero > 10:
    print(f"{numero} es mayor que 10")
elif numero == 10:
    print(f"{numero} es igual a 10")
else:
    print(f"{numero} es menor que 10")

# Ejercicio 4: Bucle for
print("\n=== Ejercicio 4: Bucle for ===")
print("Números del 1 al 5:")
for i in range(1, 6):
    print(i, end=" ")
print()

# Ejercicio 5: Bucle while
print("\n=== Ejercicio 5: Bucle while ===")
contador = 0
print("Contando hasta 5 con while:")
while contador < 5:
    contador += 1
    print(contador, end=" ")
print()

# Ejercicio 6: Listas
print("\n=== Ejercicio 6: Listas ===")
frutas = ["manzana", "banana", "naranja", "pera"]
print(f"Lista de frutas: {frutas}")
print(f"Primera fruta: {frutas[0]}")
print(f"Última fruta: {frutas[-1]}")
print(f"Número de frutas: {len(frutas)}")

frutas.append("uva")
print(f"Después de añadir uva: {frutas}")

# Ejercicio 7: Diccionarios
print("\n=== Ejercicio 7: Diccionarios ===")
persona = {
    "nombre": "María",
    "edad": 30,
    "ciudad": "Madrid"
}
print(f"Diccionario persona: {persona}")
print(f"Nombre: {persona['nombre']}")
print(f"Edad: {persona['edad']}")

# Ejercicio 8: Funciones básicas
print("\n=== Ejercicio 8: Funciones ===")

def saludar(nombre):
    return f"¡Hola, {nombre}!"

def sumar(a, b):
    return a + b

def es_par(numero):
    return numero % 2 == 0

print(saludar("Pedro"))
print(f"5 + 7 = {sumar(5, 7)}")
print(f"¿Es 8 par? {es_par(8)}")
print(f"¿Es 7 par? {es_par(7)}")
