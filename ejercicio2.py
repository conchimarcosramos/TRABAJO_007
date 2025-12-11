print ("\n---Ejercicio 2: TUPLAS VS LISTAS ===")

# Ejemplo de lista (mutable) y tupla (inmutable)
# Definición de una lista y una tupla
# Lista: colección de elementos que pueden cambiar 
# (puedes añadir, eliminar o modificar elementos)
# Tupla: colección de elementos que no pueden cambiar no se pueden cambiar una vez creadas) 
# y se definen con paréntesis.


#Lista de tareas (Mutable)
tareas = ["Estudiar", "Comer", "Dormir"]
tareas[1] = "Programar"  # Modificando la lista
print(f"Lista de tareas modificada: {tareas}") # f nos permite insertar variables dentro de cadenas

# Coodenadas geográficas (Inmutable - Tupla)
coordenadas = (40.416, -3.703)

try:
    print("Intentando modificar las coordenadas...")
    coordenadas[0] = 40.500  # Esto generará un error
except TypeError as e:
    print(f"ERROR CAPTURADO: {e}")
    print("Las tuplas son inmutables, por lo que no se pueden modificar sus elementos.")    