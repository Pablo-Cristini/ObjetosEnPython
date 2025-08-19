class Buscador:
    def asignarTrabajoAEmpleado(self, trabajo, lista_empleados):
        for i, empleado in enumerate(lista_empleados):
            if empleado.categoria == trabajo.categoria and empleado.trabajo is None:
                empleado.trabajo = trabajo
                lista_empleados.append(lista_empleados.pop(i))
                return empleado
        return None
