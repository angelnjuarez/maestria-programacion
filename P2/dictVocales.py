from ejercicios import cantVocales

if __name__ == "__main__":

    dict = {}
    while True:
        palabra = input("Ingrese una palabra: ")
        if palabra == "":
            break
        dict.setdefault(palabra, cantVocales(palabra))
    print(dict)
