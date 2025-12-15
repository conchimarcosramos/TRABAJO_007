import sys
#la libreria sys nos permite acceder a argumentos pasados por linea de comandos

print ("\n -- Ejercicio 6: GGeneradores (yield)-- \n")

# Enfoque clásico: Crear lista comleta en memoria
def obtener_lista_cuadrados(n):
    resultado = []
    for i in range(n):
        resultado.append(i ** 2)
    return resultado

# Enfoque Generador: Usar yield para producir valores uno a uno
def generar_cuadrados(n):
    for i in range(n):
        yield i ** 2
        
cantidad = 10000

# Comparamos el tamaño en memoria de ambos enfoques
lista = obtener_lista_cuadrados(cantidad)
generador = generar_cuadrados(cantidad)

print(f"Tamaño en memoria de la lista completa: {sys.getsizeof(lista)} bytes")
print(f"Tamaño en memoria del generador: {sys.getsizeof(generador)} bytes")
print("\nOBSERVACION: El generador usa significativamente menos memoria que la lista completa.")
print("El generador es minúsculo porque no guarda los datos, los crea al vuelo!\n")

# Como usamos el generador
print("Primeros 3 cuadrados usando el generador:")
print(next(generador))  # 0
print(next(generador))  # 1
print(next(generador))  # 4

# Resumen
print("\nResumen:")
print("1. Los generadores permiten manejar grandes conjuntos de datos con bajo consumo de memoria.")
print("2. Usan la palabra clave 'yield' para producir valores uno a uno.")      