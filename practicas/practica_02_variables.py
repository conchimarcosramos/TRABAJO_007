#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Práctica 02: Variables y Tipos de Datos
Aprendiendo sobre variables y tipos de datos en Python
"""

def main():
    """
    Función principal que demuestra el uso de variables
    """
    # Variables numéricas
    entero = 42
    decimal = 3.14
    
    # Variables de texto
    nombre = "Python"
    mensaje = 'Aprendiendo Python'
    
    # Variables booleanas
    es_verdadero = True
    es_falso = False
    
    # Imprimir variables
    print("=== Variables en Python ===")
    print(f"Número entero: {entero}")
    print(f"Número decimal: {decimal}")
    print(f"Nombre: {nombre}")
    print(f"Mensaje: {mensaje}")
    print(f"Booleano verdadero: {es_verdadero}")
    print(f"Booleano falso: {es_falso}")
    
    # Tipos de datos
    print("\n=== Tipos de Datos ===")
    print(f"Tipo de entero: {type(entero)}")
    print(f"Tipo de decimal: {type(decimal)}")
    print(f"Tipo de nombre: {type(nombre)}")
    print(f"Tipo de booleano: {type(es_verdadero)}")


if __name__ == "__main__":
    main()
