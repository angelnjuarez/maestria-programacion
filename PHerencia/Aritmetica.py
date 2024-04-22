from abc import ABC, abstractmethod


class OperacionAritmetica(ABC):

    @abstractmethod
    def imprimirDatos(self):
        pass


class Suma(OperacionAritmetica):

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def imprimirDatos(self):
        print(f"La suma de {self.num1} + {self.num2} es: {self.num1 + self.num2}")


class Resta(OperacionAritmetica):

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def imprimirDatos(self):
        print(f"La resta de {self.num1} - {self.num2} es: {self.num1 - self.num2}")


class Multiplicacion(OperacionAritmetica):

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def imprimirDatos(self):
        print(
            f"La multiplicación de {self.num1} * {self.num2} es: {self.num1 * self.num2}"
        )


class Division(OperacionAritmetica):

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def imprimirDatos(self):
        print(f"La división de {self.num1} / {self.num2} es: {self.num1 / self.num2}")


if __name__ == "__main__":
    suma = Suma(10, 5)
    resta = Resta(10, 5)
    multiplicacion = Multiplicacion(10, 5)
    division = Division(10, 5)

    suma.imprimirDatos()
    resta.imprimirDatos()
    multiplicacion.imprimirDatos()
    division.imprimirDatos()

    print(isinstance(suma, OperacionAritmetica))
    print(resta.__class__.__name__)
