"""Modulo extra de utilidades (VERSION CON 3 ERRORES DE FLAKE8).

Este archivo se agrega en un branch a proposito con 3 errores que
flake8 puede detectar, para luego corregirlos en un commit posterior.
"""

import math  # ERROR 1 (F401): import no utilizado en ningun lugar.


def sumar(a, b):
    resultado=a + b  # ERROR 2 (E225): falta espacio alrededor del "=".
    return resultado


def saludar(nombre):
    mensaje = "Hola " + nombre + ", este es un mensaje demasiado largo que supera los limites"  # ERROR 3 (E501): linea muy larga.
    return mensaje
