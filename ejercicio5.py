# Creamos una plantilla (clase) para crear múltiples objetos (instancias) y entender mejor la programación orientada a objetos. 
#__init__ y self son conceptos clave en la creación de clases en Python.

print ("Ejercicio 5: Clases y Objetos en Python __init__ y self")
class Robot:
    # El método __init__ es el constructor de la clase. Se llama automáticamente cuando se crea una nueva instancia de la clase.
    def __init__(self, nombre, bateria=100):
        # 'self' se refiere a la instancia actual del objeto. 
        # Permite acceder a las variables y métodos asociados con la instancia.
        self.nombre = nombre  # Atributo de instancia
        self.bateria = bateria  # Atributo de instancia
    # creamos un nuevo método (acción) para la clase Robot
    def saludar(self):
        # Método que utiliza los atributos de la instancia para imprimir un saludo.
        if self.bateria > 0:
            print(f"[{self.nombre}]: ¡Hola, humano soy {self.nombre}! Bateria: {self.bateria}%")
            self.bateria -= 10  # Disminuye la batería en 10 unidades cada vez que saluda 
        else:
            print(f"[{self.nombre}]: No puedo saludar, batería agotada...")
        # Imprime un saludo utilizando el nombre del robot.
        
# Crear instancias (objetos) de la clase Robot
r1 = Robot("R2-D2")
r2 = Robot("C-3PO", bateria=20)   

# Llamar al método saludar en cada instancia
# Cada robot saluda y su batería disminuye
r1.saludar()  # R2-D2 saluda
r2.saludar()  # C-3PO saluda
r2.saludar()  # C-3PO saluda nuevamente
r2.saludar()  # C-3PO intenta saludar pero la batería se agota

print (f"\nEstado final de las baterías: {r1.nombre}: {r1.bateria}%, {r2.nombre}: {r2.bateria}%")    