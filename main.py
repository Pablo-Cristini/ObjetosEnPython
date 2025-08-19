from Buscador import Buscador
from Categoria import Categoria
from Empleado import Empleado
from Empresa import Empresa
from TrabajoFactory import TrabajoFactory

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
    TrabajoFactory.crear_trabajo("Repositor gondolas", catRepositor, 2000, 6),
    TrabajoFactory.crear_trabajo("Asistente en Hogar", catAsistente, 3000, 2),  
    TrabajoFactory.crear_trabajo("Cajero caja 5", catCajero, 500, 10),          
]

    lista_empleados = empresa.obtener_empleados()

    buscador = Buscador()

    for trabajo in trabajos:
        empleado_asignado = buscador.asignarTrabajoAEmpleado(trabajo, lista_empleados)
        if empleado_asignado:
            print(f" Se asignó '{trabajo.descripcion}' a {empleado_asignado.nombre} {trabajo.cantHoras} horas")
        else:
            print(f"No hay empleados disponibles '{trabajo.descripcion}'")

    print("\n---Estado final de empleados ---")
    for emp in lista_empleados:
        emp.mostrarDatos()

if __name__ == "__main__":
    main()