import copy

print("=== Ejercicio 1: Copia de listas ===")
# Crear una lista original con algunos elementos
inventario_original = ["Tablet",[10, 80]]
copia_superficial = copy.copy(inventario_original)
copia_profunda = copy.deepcopy(inventario_original)
print("Lista original:", inventario_original)

copia_superficial[1][0] = 5
copia_profunda[1][0] = 0

#\n damos un salto de línea para mejor visualización
print ("\n--- Después de modificar las copias ---")
print(f"Copia superficial: {copia_superficial} (Cantidad cambiada a 5)")
print(f"Copia profunda: {copia_profunda} (Cantidad cambiada a 0)")
print(f"Lista original: {inventario_original} (Cantidad en la lista original)")
print("\nOBSERVACIÓN: ¡La copia superficial refleja el cambio en la lista original, mientras que la copia profunda no lo hace!")