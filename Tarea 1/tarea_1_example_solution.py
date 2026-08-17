"""Soluciones de la Tarea 1 - MT-7003 Microprocesadores.

Este modulo define las dos funciones evaluadas por el archivo de pruebas
'tarea_1_testing.py':

  - filtrar_vocales: filtra vocales o consonantes de una cadena.
  - encontrar_extremos: obtiene el minimo y el maximo de una lista.

Cada funcion valida sus parametros de entrada y devuelve un codigo de
estado (0 para exito, un numero negativo unico para cada tipo de error)
junto con el resultado. En caso de error, el o los resultados se
devuelven como None para respetar la cantidad de valores retornados.
"""

# ---------------------------------------------------------------------------
# Codigos de estado. Deben coincidir exactamente con los que espera el
# archivo de pruebas del profesor. Se definen como constantes para que el
# codigo sea mas legible y facil de mantener.
# ---------------------------------------------------------------------------
EXITO = 0                        # La funcion se ejecuto correctamente.

# Errores de filtrar_vocales.
ERR_CADENA_NO_STRING = -100      # La cadena no es un string.
ERR_CADENA_NO_ALFABETICA = -200  # La cadena tiene caracteres no alfabeticos.
ERR_CADENA_VACIA = -300          # La cadena esta vacia.
ERR_CADENA_MUY_LARGA = -400      # La cadena tiene mas de 30 caracteres.
ERR_BANDERA_NO_BOOL = -500       # La bandera no es un booleano.

# Errores de encontrar_extremos.
ERR_ENTRADA_NO_LISTA = -600      # La entrada no es una lista.
ERR_ELEMENTO_NO_NUMERO = -700    # Algun elemento de la lista no es numero.
ERR_LISTA_VACIA = -800           # La lista esta vacia.
ERR_LISTA_MUY_LARGA = -900       # La lista tiene mas de 15 elementos.


def _es_numero(valor):
    """Indica si 'valor' es un numero (int o float) y no un booleano.

    En Python el tipo bool es una subclase de int, por lo que True y
    False pasarian una verificacion normal de isinstance(x, int). Por eso
    se excluyen los booleanos de forma explicita.

    :param valor: valor a verificar.
    :return: True si es int o float (no bool), False en caso contrario.
    """
    return (isinstance(valor, (int, float))
            and not isinstance(valor, bool))


def filtrar_vocales(cadena, bandera):
    """Filtra las vocales o las consonantes de una cadena de texto.

    Parametros de entrada:
    :param cadena: texto a filtrar. Debe ser un string no vacio, con
        solo letras del abecedario y de maximo 30 caracteres.
    :param bandera: booleano. Si es True se devuelven solo las vocales;
        si es False se devuelven solo las consonantes.

    Valores de salida (siempre dos valores en este orden):
    :return: (estado, filtrada)
        - estado: 0 si todo salio bien, o un codigo de error negativo.
        - filtrada: string filtrado, o None si hubo error.

    Codigos de error:
        -100 si la cadena no es un string.
        -200 si la cadena contiene caracteres no alfabeticos.
        -300 si la cadena esta vacia.
        -400 si la cadena tiene mas de 30 caracteres.
        -500 si la bandera no es un booleano.
    """
    # 1) La cadena debe ser un string.
    if not isinstance(cadena, str):
        return ERR_CADENA_NO_STRING, None

    # 2) La cadena no puede estar vacia. Se verifica antes que el caracter
    #    alfabetico porque "" no es alfabetico y debe dar su error propio.
    if len(cadena) == 0:
        return ERR_CADENA_VACIA, None

    # 3) La cadena solo puede contener letras del abecedario.
    if not cadena.isalpha():
        return ERR_CADENA_NO_ALFABETICA, None

    # 4) La cadena no puede tener mas de 30 caracteres.
    if len(cadena) > 30:
        return ERR_CADENA_MUY_LARGA, None

    # 5) La bandera debe ser un booleano real (no un int como 0 o 1, ni un
    #    string). isinstance(bandera, bool) distingue True/False de 1/0.
    if not isinstance(bandera, bool):
        return ERR_BANDERA_NO_BOOL, None

    # 6) Se define el conjunto de vocales (minusculas y mayusculas).
    vocales = "aeiouAEIOU"

    # 7) Se recorre la cadena manteniendo el orden original y se agregan
    #    los caracteres segun el valor de la bandera.
    resultado = ""
    for caracter in cadena:
        es_vocal = caracter in vocales
        if bandera and es_vocal:
            # bandera True: solo vocales.
            resultado += caracter
        elif not bandera and not es_vocal:
            # bandera False: solo consonantes.
            resultado += caracter

    # 8) Todo correcto: se devuelve el codigo de exito y el string filtrado.
    return EXITO, resultado


def encontrar_extremos(lista_numeros):
    """Encuentra el valor minimo y el maximo de una lista de numeros.

    Parametros de entrada:
    :param lista_numeros: lista de numeros (int o float). No puede estar
        vacia ni tener mas de 15 elementos.

    Valores de salida (siempre tres valores en este orden):
    :return: (estado, minimo, maximo)
        - estado: 0 si todo salio bien, o un codigo de error negativo.
        - minimo: valor minimo de la lista, o None si hubo error.
        - maximo: valor maximo de la lista, o None si hubo error.

    Codigos de error:
        -600 si la entrada no es una lista.
        -700 si algun elemento no es un numero.
        -800 si la lista esta vacia.
        -900 si la lista tiene mas de 15 elementos.
    """
    # 1) La entrada debe ser una lista.
    if not isinstance(lista_numeros, list):
        return ERR_ENTRADA_NO_LISTA, None, None

    # 2) Todos los elementos deben ser numeros (int o float, no bool). Si
    #    la lista esta vacia este ciclo no se ejecuta y se pasa al punto 3.
    for elemento in lista_numeros:
        if not _es_numero(elemento):
            return ERR_ELEMENTO_NO_NUMERO, None, None

    # 3) La lista no puede estar vacia.
    if len(lista_numeros) == 0:
        return ERR_LISTA_VACIA, None, None

    # 4) La lista no puede tener mas de 15 elementos.
    if len(lista_numeros) > 15:
        return ERR_LISTA_MUY_LARGA, None, None

    # 5) Se obtienen el minimo y el maximo con las funciones nativas.
    minimo = min(lista_numeros)
    maximo = max(lista_numeros)

    # 6) Todo correcto: se devuelven el codigo de exito, minimo y maximo.
    return EXITO, minimo, maximo
