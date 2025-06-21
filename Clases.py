from abc import ABC, abstractmethod
class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.__empleados = []

    def agregar_empleado(self, empleado):
        self.__empleados.append(empleado)

    def obtener_empleados(self):
        return self.__empleados
    
class Persona(ABC):  #clase Abstracta Persona
    def __init__(self, nombre, dni):
        self.nombre = nombre      
        self.__dni = dni              #Encapsulamiento 

    @property
    def dni(self):
        return self.__dni

    @abstractmethod         #metodo Abstracto de la clase abstracta
    def mostrarDatos(self):
        pass

class Empleado(Persona): #Empleado hereda de Persona
    def __init__(self, nombre, dni, categoria, sueldoTotal):
        super().__init__(nombre, dni)
        self.__categoria = categoria
        self.__sueldoTotal = sueldoTotal
        self.__trabajo = None

    @property
    def categoria(self):
        return self.__categoria
    @property
    def sueldoTotal(self):
        return self.__sueldoTotal
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
            print(f"Nombre Empleado: {self.nombre}, DNI: {self.dni}, Categoria: {self.categoria.nombre}, Sueldo Total: {self.sueldoTotal}, Trabajo: {trabajo_str}")

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
        self.__sueldoXHora = sueldoXHora
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
                lista_empleados.append(lista_empleados.pop(i))  # Mando empleado al final
                return empleado
        return None

