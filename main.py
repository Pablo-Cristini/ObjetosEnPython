from Clases import Categoria, Empleado, Trabajo, Buscador, Empresa

def main():
    catRepositor = Categoria("Repositor")
    catCajero = Categoria("Cajero")
    catAsistente = Categoria("Asistente")

    empresa = Empresa("MiEmpresa S.A.")
    empresa.agregar_empleado(Empleado("Lucía", "44556677", catRepositor))
    empresa.agregar_empleado(Empleado("Pedro", "22334455", catRepositor))
    empresa.agregar_empleado(Empleado("Ana", "11223344", catAsistente))
    empresa.agregar_empleado(Empleado("Carlos", "99887766", catCajero))
    empresa.agregar_empleado(Empleado("María", "55443322", catCajero))

    trabajos = [
         Trabajo("Repositor gondolas", catRepositor, 2000, 6),
    #     Trabajo("Asistente en Hogar", catAsistente, 3000, 5),
    #     Trabajo("Asistente en Electrodomesticos", catAsistente, 1800, 8),
    #     Trabajo("Cajero caja 5", catCajero, 1900, 8),
    #     Trabajo("Cajero caja 4", catCajero, 2100, 8),
    #     Trabajo("Repositor heladeras", catRepositor, 2100, 8),
    ]

    lista_empleados = empresa.obtener_empleados()

    buscador = Buscador()

    for trabajo in trabajos:
        empleado_asignado = buscador.asignarTrabajoAEmpleado(trabajo, lista_empleados)
        if empleado_asignado:
            print(f" Se asignó '{trabajo.descripcion}' a {empleado_asignado.nombre}")
        else:
            print(f"No hay empleados disponibles '{trabajo.descripcion}'")

    print("\n---Estado final de empleados ---")
    for emp in lista_empleados:
        emp.mostrarDatos()

if __name__ == "__main__":
    main()