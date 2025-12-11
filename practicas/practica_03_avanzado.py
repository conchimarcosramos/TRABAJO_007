"""
Práctica 03: Nivel Avanzado de Python
Programación orientada a objetos, excepciones y módulos
"""

# Ejercicio 1: Clases y Objetos básicos
print("=== Ejercicio 1: Clases y Objetos ===")

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años"
    
    def cumpleanios(self):
        self.edad += 1
        return f"¡Feliz cumpleaños! Ahora tengo {self.edad} años"

persona1 = Persona("Carlos", 25)
persona2 = Persona("Laura", 30)

print(persona1.saludar())
print(persona2.saludar())
print(persona1.cumpleanios())

# Ejercicio 2: Herencia
print("\n=== Ejercicio 2: Herencia ===")

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hacer_sonido(self):
        return "Algún sonido"

class Perro(Animal):
    def hacer_sonido(self):
        return f"{self.nombre} dice: ¡Guau!"

class Gato(Animal):
    def hacer_sonido(self):
        return f"{self.nombre} dice: ¡Miau!"

perro = Perro("Rex")
gato = Gato("Michi")

print(perro.hacer_sonido())
print(gato.hacer_sonido())

# Ejercicio 3: Métodos especiales
print("\n=== Ejercicio 3: Métodos Especiales ===")

class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    
    def __str__(self):
        return f"'{self.titulo}' por {self.autor}"
    
    def __len__(self):
        return self.paginas
    
    def __eq__(self, otro):
        return self.paginas == otro.paginas

libro1 = Libro("Don Quijote", "Cervantes", 863)
libro2 = Libro("Cien años de soledad", "García Márquez", 471)

print(f"Libro 1: {libro1}")
print(f"Libro 2: {libro2}")
print(f"Páginas del libro 1: {len(libro1)}")
print(f"¿Son iguales en páginas? {libro1 == libro2}")

# Ejercicio 4: Manejo de excepciones
print("\n=== Ejercicio 4: Manejo de Excepciones ===")

def dividir(a, b):
    try:
        resultado = a / b
        return f"El resultado es: {resultado}"
    except ZeroDivisionError:
        return "Error: No se puede dividir por cero"
    except TypeError:
        return "Error: Los argumentos deben ser números"

print(dividir(10, 2))
print(dividir(10, 0))
print(dividir(10, "a"))

# Ejercicio 5: Try-Except-Finally
print("\n=== Ejercicio 5: Try-Except-Finally ===")

def leer_archivo(nombre):
    try:
        with open(nombre, 'r') as archivo:
            return archivo.read()
    except FileNotFoundError:
        return f"Error: El archivo '{nombre}' no existe"
    finally:
        print(f"Intento de lectura de '{nombre}' completado")

print(leer_archivo('/tmp/ejemplo.txt'))
print(leer_archivo('/tmp/no_existe.txt'))

# Ejercicio 6: Propiedades
print("\n=== Ejercicio 6: Propiedades (Properties) ===")

class Rectangulo:
    def __init__(self, ancho, alto):
        self._ancho = ancho
        self._alto = alto
    
    @property
    def area(self):
        return self._ancho * self._alto
    
    @property
    def perimetro(self):
        return 2 * (self._ancho + self._alto)

rectangulo = Rectangulo(5, 3)
print(f"Rectángulo: {rectangulo._ancho} x {rectangulo._alto}")
print(f"Área: {rectangulo.area}")
print(f"Perímetro: {rectangulo.perimetro}")

# Ejercicio 7: Métodos de clase y estáticos
print("\n=== Ejercicio 7: Métodos de Clase y Estáticos ===")

class Matematicas:
    pi = 3.14159
    
    @classmethod
    def area_circulo(cls, radio):
        return cls.pi * radio ** 2
    
    @staticmethod
    def es_primo(numero):
        if numero < 2:
            return False
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                return False
        return True

print(f"Área de círculo (radio 5): {Matematicas.area_circulo(5)}")
print(f"¿Es 17 primo? {Matematicas.es_primo(17)}")
print(f"¿Es 20 primo? {Matematicas.es_primo(20)}")

# Ejercicio 8: Context Managers
print("\n=== Ejercicio 8: Context Managers ===")

class MiArchivo:
    def __init__(self, nombre, modo):
        self.nombre = nombre
        self.modo = modo
        self.archivo = None
    
    def __enter__(self):
        print(f"Abriendo archivo: {self.nombre}")
        self.archivo = open(self.nombre, self.modo)
        return self.archivo
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Cerrando archivo: {self.nombre}")
        if self.archivo:
            self.archivo.close()

with MiArchivo('/tmp/test.txt', 'w') as f:
    f.write("Ejemplo de context manager\n")

# Ejercicio 9: Decoradores simples
print("\n=== Ejercicio 9: Decoradores ===")

def decorador_tiempo(func):
    def wrapper(*args, **kwargs):
        print(f"Ejecutando {func.__name__}...")
        resultado = func(*args, **kwargs)
        print(f"{func.__name__} completada")
        return resultado
    return wrapper

@decorador_tiempo
def calcular_suma(a, b):
    return a + b

resultado = calcular_suma(5, 3)
print(f"Resultado: {resultado}")

# Ejercicio 10: Generadores
print("\n=== Ejercicio 10: Generadores ===")

def contador(maximo):
    n = 0
    while n < maximo:
        yield n
        n += 1

print("Generador de números:")
for numero in contador(5):
    print(numero, end=" ")
print()

# Generador de números pares
def pares(limite):
    for i in range(0, limite, 2):
        yield i

print("Números pares hasta 10:")
for par in pares(11):
    print(par, end=" ")
print()
