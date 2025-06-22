from abc import ABC, abstractmethod

class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.__empleados = []

    def agregar_empleado(self, empleado):
        self.__empleados.append(empleado)

    def obtener_empleados(self):
        return self.__empleados

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

class Categoria:
    def __init__(self, nombre):
        self.__nombre = nombre

    @property
    def nombre(self):
        return self.__nombre

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

class Buscador:
    def asignarTrabajoAEmpleado(self, trabajo, lista_empleados):
        for i, empleado in enumerate(lista_empleados):
            if empleado.categoria == trabajo.categoria and empleado.trabajo is None:
                empleado.trabajo = trabajo
                lista_empleados.append(lista_empleados.pop(i))
                return empleado
        return None
