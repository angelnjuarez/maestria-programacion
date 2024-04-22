from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nombre):
        self.__nombre = nombre

    def getNombre(self):
        return self.__nombre

    def __str__(self):
        return str("Nombre: " + self.__nombre)

    @abstractmethod
    def desplazar(self):
        pass

class Terrestre(Animal):
    def __init__(self, nombre, cantPatas):
        super().__init__(nombre)
        self.__cantPatas = cantPatas

    def desplazar(self):
        print("El animal camina")

    def __str__(self):
        return super().__str__() + ", Numero de patas: " + str(self.__cantPatas)

class Acuatico(Animal):
    def __init__(self, nombre, cantAletas):
        super().__init__(nombre)
        self.__cantAletas =  cantAletas

    def desplazar(self):
        print("El animal nada")
    
    def __str__(self):
        return super().__str__() + ", Numero de aletas: " + str(self.__cantAletas)

perro = Terrestre("Perro", 4)
print(perro.getNombre())
perro.desplazar()
print(perro)
