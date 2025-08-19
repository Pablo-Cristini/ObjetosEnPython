class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.__empleados = []

    def agregar_empleado(self, empleado):
        self.__empleados.append(empleado)

    def obtener_empleados(self):
        return self.__empleados


