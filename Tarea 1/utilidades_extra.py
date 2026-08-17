"""Modulo extra de utilidades (VERSION CORREGIDA).

Esta es la version del archivo con los 3 errores de flake8 ya
corregidos:
  1. Se elimino el import no utilizado (F401).
  2. Se agregaron espacios alrededor del operador "=" (E225).
  3. Se acorto la linea que superaba los 79 caracteres (E501).
"""


def sumar(a, b):
    """Suma dos numeros y devuelve el resultado.

    :param a: primer sumando.
    :param b: segundo sumando.
    :return: la suma de a y b.
    """
    resultado = a + b  # Corregido: espacios alrededor del "=".
    return resultado


def saludar(nombre):
    """Construye un mensaje de saludo para el nombre dado.

    :param nombre: nombre de la persona a saludar.
    :return: mensaje de saludo.
    """
    # Corregido: la linea se divide para no superar los 79 caracteres.
    mensaje = "Hola " + nombre + ", este es un mensaje de saludo"
    return mensaje
