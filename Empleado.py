from Persona import Persona
class Empleado(Persona):
    def __init__(self, nombre, dni, categoria):
        super().__init__(nombre, dni)
        self.__categoria = categoria
        self.__trabajo = None

    @property
    def categoria(self):
        return self.__categoria

    @property
    def trabajo(self):
        return self.__trabajo

    @trabajo.setter
    def trabajo(self, trabajo):
        self.__trabajo = trabajo

    def mostrarDatos(self):
        if self.trabajo is not None:
            trabajo_str = self.trabajo.descripcion
        else:
            trabajo_str = "Sin trabajo asignado"
        print(f"Nombre Empleado: {self.nombre}, DNI: {self.dni}, Categoria: {self.categoria.nombre}, Trabajo: {trabajo_str}")
