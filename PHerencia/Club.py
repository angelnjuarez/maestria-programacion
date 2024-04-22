from abc import ABC, abstractmethod


class Empleado(ABC):
    def __init__(self, nombre, salario):
        self._nombre = nombre
        self._salario = salario

    @abstractmethod
    def calcularSueldoACobrar(self):
        pass


class Jugador(Empleado):
    def __init__(self, nombre, salario, cant_partidos, cant_goles):
        super().__init__(nombre, salario)
        self.__cant_partidos = cant_partidos
        self.__cant_goles = cant_goles

    def calcularSueldoACobrar(self):
        if self.__cant_goles / self.__cant_partidos > 0.5:
            return self._salario * 2
        return self._salario


class Entrenador(Empleado):
    def __init__(self, nombre, salario, cant_campeonatos):
        super().__init__(nombre, salario)
        self.__cant_campeonatos = cant_campeonatos

    def calcularSueldoACobrar(self):
        return self._salario + self.__cant_campeonatos * 1000


if __name__ == "__main__":
    jugador = Jugador("Juan", 1000, 5, 10)
    entrenador = Entrenador("Carlos", 2000, 3)
    print(jugador.calcularSueldoACobrar())
    print(entrenador.calcularSueldoACobrar())
