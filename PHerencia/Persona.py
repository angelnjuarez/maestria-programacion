class Persona:
    def __init__(self, nombre, edad, dni):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

    def __str__(self):
        return self.__nombre + " (" + str(self.__edad) + ") " + self.__dni


if __name__ == "__main__":
    persona = Persona("Juan", 23, "12345678")
    print(persona)
