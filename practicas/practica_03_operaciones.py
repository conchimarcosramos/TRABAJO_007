#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Práctica 03: Operaciones Matemáticas
Aprendiendo sobre operaciones matemáticas básicas en Python
"""

def main():
    """
    Función principal que demuestra operaciones matemáticas
    """
    # Números para operar
    a = 10
    b = 3
    
    print("=== Operaciones Matemáticas ===")
    print(f"a = {a}, b = {b}")
    print()
    
    # Operaciones básicas
    print(f"Suma: {a} + {b} = {a + b}")
    print(f"Resta: {a} - {b} = {a - b}")
    print(f"Multiplicación: {a} * {b} = {a * b}")
    print(f"División: {a} / {b} = {a / b}")
    print(f"División entera: {a} // {b} = {a // b}")
    print(f"Módulo (resto): {a} % {b} = {a % b}")
    print(f"Potencia: {a} ** {b} = {a ** b}")


if __name__ == "__main__":
    main()
