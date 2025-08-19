
class Trabajo:
    def __init__(self, descripcion, categoria, sueldoXHora, cantHoras):
        self.__descripcion = descripcion
        self.__categoria = categoria
        self.__sueldoXHora = sueldoXHora if sueldoXHora >= 1000 else 1000
        if cantHoras < 4:
            self.__cantHoras = 4
        elif cantHoras > 8:
            self.__cantHoras = 8
        else:
            self.__cantHoras = cantHoras

    @property
    def descripcion(self):
        return self.__descripcion

    @property
    def categoria(self):
        return self.__categoria

    @property
    def sueldoXHora(self):
        return self.__sueldoXHora

    @property
    def cantHoras(self):
        return self.__cantHoras
