import random


def cantVocales(palabra):
    vocales = "aeiou"
    cant = 0
    for letra in palabra:
        if letra in vocales:
            cant += 1
    return cant


def cantVocalesRec(palabra):
    vocales = "aeiou"
    if palabra == "":
        return 0
    if palabra[0] in vocales:
        return 1 + cantVocalesRec(palabra[1:])
    else:
        return cantVocalesRec(palabra[1:])


def numAleatorios(cantidad):
    return [random.uniform(1, 100) for i in range(cantidad)]
