from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre, dni):
        if not nombre or nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacío")
        if not dni or str(dni).strip() == "":
            raise ValueError("El DNI no puede estar vacío")
        self.nombre = nombre
        self.__dni = dni

    @property
    def dni(self):
        return self.__dni

    @abstractmethod
    def mostrarDatos(self):
        pass

