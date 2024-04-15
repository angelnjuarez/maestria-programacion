from diccionarios import kioskos


def promedioCadenas():
    cantCadena = 0
    cadenaTotal = 0

    while True:
        cadena = input("Introduce una cadena: ")
        cadenaTotal += len(cadena)
        if len(cadena) != 0:
            cantCadena += 1
            continue
        print("El promedio de caracteres es: ", cadenaTotal / cantCadena)
        break


def digitoADigito():
    num = int(input("Introduce un número: "))
    num = num * 365
    numStr = str(num)
    for i in range(len(numStr)):
        print(numStr[len(numStr) - i - 1], end="\n")


def secuenciaNum():
    numeros = set()  # Para no repetir números
    while True:
        num = input("Ingresa un número: ")
        if not num.isnumeric():
            print("El número ingresado no es un número")
            continue
        if num == "0":
            break
        numeros.add(float(num))
    numeros = sorted(list(numeros))  # Convertir a lista para ordenar
    if len(numeros) != 0:
        print("El máximo es: ", numeros[-1], ", y el mínimo es: ", numeros[0])
        numeros = numeros[1:-1]
        print("La secuencia sin el máximo y el mínimo es: ", numeros)


def palindromos():
    cadena = input("Introduce una cadena: ")
    cadena2 = input("Introduce otra cadena: ")
    cadenaInvertida = cadena2[::-1]
    print(cadena == cadenaInvertida)


def palindromosRecursivo():
    cadena = input("Introduce una cadena: ") + input("Introduce otra cadena: ")
    print(auxPalindromosRecursivo(cadena))


def auxPalindromosRecursivo(cadena):
    if len(cadena) == 0:
        return True
    if cadena[0] == cadena[-1]:
        return auxPalindromosRecursivo(cadena[1:-1])
    return False


def totalMarcas():
    kiosko = input("Nombre del kiosko: ")
    print(len(kioskos.get(kiosko)))


def esBiciesto():
    anio = int(input("Introduce un año: "))
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        print("Es biciesto")
    else:
        print("No es biciesto")
