import Persona


class Alumno(Persona.Persona):
    def __init__(self, nombre, edad, dni, promedio):
        super().__init__(nombre, edad, dni)
        self.__promedio = promedio

    def __str__(self):
        return "ALUMNO: " + super().__str__() + " " + str(self.__promedio)


if __name__ == "__main__":
    alumno = Alumno("Juan", 23, "12345678", 7.6)
    print(alumno)
