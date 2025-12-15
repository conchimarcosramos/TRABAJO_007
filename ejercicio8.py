import threading
import time

# threading nos permite crear y manejar hilos en Python
# time nos permite manejar tiempos de espera

print("\nEjercicio 8: Hilos y sincronización\n")

def descargar_archivo(nombre, segundos):
    print(f"Iniciando descarga de {nombre} ({segundos}s)...")
    time.sleep(segundos)  # Simula el tiempo de espera para la descarga
    print(f"Descarga de {nombre} completada.")  
    
# Crear hilos para descargar archivos
hilo1 = threading.Thread(target=descargar_archivo, args=("Foto.jpg", 2))
hilo2 = threading.Thread(target=descargar_archivo, args=("Video.mp4", 5))

# Iniciar los hilos
print("--- Iniciando descargas en paralelo ---")
hilo1.start()
hilo2.start() 

print("--- Esperando a que las descargas terminen ---")
print("--- Tareas principales en ejecución mientras tanto ---")

# Esperar a que ambos hilos terminen
hilo1.join()
hilo2.join()
print("--- Todas las descargas completadas ---\n")           