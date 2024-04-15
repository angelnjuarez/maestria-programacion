from ejercicios import *


opciones = {
    "1": promedioCadenas,
    "2": digitoADigito,
    "3": secuenciaNum,
    "4a": palindromos,
    "4b": palindromosRecursivo,
    "5": totalMarcas,
    "6": esBiciesto
}


if __name__ == "__main__":
    print("N° de enunciados:" +
          "\n1. Promedio de cadenas" +
          "\n2. Dígitos de un número" +
          "\n3. Secuencia de números" +
          "\n4a. Palíndromos" +
          "\n4b. Palíndromos recursivo" +
          "\n5. Total de marcas" +
          "\n6. Año biciesto")

    while True:
        opcion = input("Ingrese el número del enunciado: ")
        if opcion in opciones:
            opciones[opcion]()
        else:
            break
