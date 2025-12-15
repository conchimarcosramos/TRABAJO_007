print ("\nEjercicio 7: Lambdas y funciones de orden superior (map y filter)\n")
# Definir una lista de números
precios_en_dolares = [10, 25, 40, 5, 100]
tasa_cambio = 0.92  # Supongamos que 1 dólar = 0.92 euros

# Usar map con una función lambda para convertir los precios a euros
precios_en_euros = list(map(lambda p: p * tasa_cambio, precios_en_dolares))

# Filtrar los precios mayores a 20 euros usando filter y una función lambda
baratos = list(filter(lambda p: p < 20, precios_en_euros))

# Imprimir los resultados
print(f"Precios en dólares ($): {[f'{p:.2f}' for p in precios_en_dolares]}")
print(f"Precios en euros (€): {[f'{p:.2f}' for p in precios_en_euros]}")
print(f"Precios menores a 20 euros (€): {[f'{p:.2f}' for p in baratos]}")

# Explicación:
# 1. Se define una lista de precios en dólares.
# 2. Se utiliza map junto con una función lambda para convertir cada precio a euros.
# 3. Se utiliza filter junto con una función lambda para filtrar los precios menores a 20 euros.
# 4. Finalmente, se imprimen los precios originales, los convertidos y los filtrados.
# Para conseguir los dos decimales en la impresión, se usa formateo de cadenas con f-strings.
# Esto asegura que los precios se muestren con dos decimales en la salida.
# .2f indica que queremos dos dígitos después del punto decimal.
