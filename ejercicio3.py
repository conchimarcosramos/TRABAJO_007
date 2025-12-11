print ("\n---Ejercicio 3: Decoradores ===")

# Definición de un decorador simple
def mi_chivato(funcion):
    def envoltura(*args, **kwargs):
        print(f"Antes de llamar a la función {funcion.__name__}.")
        resultado = funcion(*args, **kwargs)
        print(f"Después de llamar a la función {funcion.__name__}.")
        return resultado
    return envoltura 

# Uso del decorador en funciones @
@mi_chivato
def suma_pesada(a, b):
    return a + b

@mi_chivato 
def saludar(nombre):
    print(f"Hola, {nombre}!")
      
# Uso de las funciones decoradas
x = suma_pesada(10, 20)
print(f"Resultado de la suma: {x}\n")
saludar("Estudiante")       

# Haciendo uso de *args en la declaración de la función podemos hacer 
# que el número de parámetros que acepte sea variable.
# Haciendo uso de **kwargs en la declaración de la función nos permiten 
# dar un nombre a cada argumento de entrada, pudiendo acceder a ellos dentro 
# de la función a través de un diccionario.