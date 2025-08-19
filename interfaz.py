import tkinter as tk
from tkinter import messagebox

from Categoria import Categoria
from Empleado import Empleado
from TrabajoFactory import TrabajoFactory
from Empresa import Empresa
from Buscador import Buscador

empresa = Empresa("MiEmpresa S.A.")
categorias = []
trabajos = []
buscador = Buscador()


def crear_categoria():
    nombre = entry_categoria.get()
    if not nombre:
        messagebox.showerror("Error", "Debe ingresar un nombre de categoría")
        return
    cat = Categoria(nombre)
    categorias.append(cat)
    messagebox.showinfo("Éxito", f"Categoría '{nombre}' creada correctamente")
    entry_categoria.delete(0, tk.END)


def crear_empleado():
    nombre = entry_nombre.get()
    dni = entry_dni.get()
    categoria_nombre = entry_cat_empleado.get()

    categoria = next((c for c in categorias if c.nombre == categoria_nombre), None)
    if not categoria:
        messagebox.showerror("Error", "Categoría no encontrada")
        return

    try:
        empleado = Empleado(nombre, dni, categoria)
        empresa.agregar_empleado(empleado)
        messagebox.showinfo("Éxito", f"Empleado '{nombre}' agregado correctamente")
        entry_nombre.delete(0, tk.END)
        entry_dni.delete(0, tk.END)
        entry_cat_empleado.delete(0, tk.END)
    except ValueError as e:
        messagebox.showerror("Error", str(e))


def crear_trabajo():
    descripcion = entry_descripcion.get()
    categoria_nombre = entry_cat_trabajo.get()
    try:
        sueldo = int(entry_sueldo.get())
        horas = int(entry_horas.get())
    except ValueError:
        messagebox.showerror("Error", "Sueldo y horas deben ser numéricos")
        return

    categoria = next((c for c in categorias if c.nombre == categoria_nombre), None)
    if not categoria:
        messagebox.showerror("Error", "Categoría no encontrada")
        return

    trabajo = TrabajoFactory.crear_trabajo(descripcion, categoria, sueldo, horas)
    trabajos.append(trabajo)
    messagebox.showinfo("Éxito", f"Trabajo '{descripcion}' creado correctamente")
    entry_descripcion.delete(0, tk.END)
    entry_cat_trabajo.delete(0, tk.END)
    entry_sueldo.delete(0, tk.END)
    entry_horas.delete(0, tk.END)


def asignar_trabajos():
    lista_empleados = empresa.obtener_empleados()
    resultados.delete("1.0", tk.END)

    for trabajo in trabajos:
        empleado = buscador.asignarTrabajoAEmpleado(trabajo, lista_empleados)
        if empleado:
            resultados.insert(tk.END, f"Asignado: {trabajo.descripcion} → {empleado.nombre}\n")
        else:
            resultados.insert(tk.END, f"No disponible: {trabajo.descripcion}\n")


def mostrar_estado_empleados():
    lista_empleados = empresa.obtener_empleados()
    resultados.delete("1.0", tk.END)
    resultados.insert(tk.END, "--- Estado de empleados ---\n")
    for emp in lista_empleados:
        trabajo_str = emp.trabajo.descripcion if emp.trabajo else "Sin trabajo asignado"
        resultados.insert(
            tk.END,
            f"{emp.nombre} ({emp.dni}) - {emp.categoria.nombre} → {trabajo_str}\n"
        )



root = tk.Tk()
root.title("Gestión de Empleados y Trabajos")

tk.Label(root, text="Crear Categoría").grid(row=0, column=0, sticky="w")
entry_categoria = tk.Entry(root)
entry_categoria.grid(row=0, column=1)
tk.Button(root, text="Crear", command=crear_categoria).grid(row=0, column=2)

tk.Label(root, text="Nombre Empleado").grid(row=1, column=0, sticky="w")
entry_nombre = tk.Entry(root)
entry_nombre.grid(row=1, column=1)

tk.Label(root, text="DNI").grid(row=2, column=0, sticky="w")
entry_dni = tk.Entry(root)
entry_dni.grid(row=2, column=1)

tk.Label(root, text="Categoría").grid(row=3, column=0, sticky="w")
entry_cat_empleado = tk.Entry(root)
entry_cat_empleado.grid(row=3, column=1)

tk.Button(root, text="Crear Empleado", command=crear_empleado).grid(row=3, column=2)

tk.Label(root, text="Descripción Trabajo").grid(row=4, column=0, sticky="w")
entry_descripcion = tk.Entry(root)
entry_descripcion.grid(row=4, column=1)

tk.Label(root, text="Categoría").grid(row=5, column=0, sticky="w")
entry_cat_trabajo = tk.Entry(root)
entry_cat_trabajo.grid(row=5, column=1)

tk.Label(root, text="Sueldo x Hora").grid(row=6, column=0, sticky="w")
entry_sueldo = tk.Entry(root)
entry_sueldo.grid(row=6, column=1)

tk.Label(root, text="Cantidad de Horas").grid(row=7, column=0, sticky="w")
entry_horas = tk.Entry(root)
entry_horas.grid(row=7, column=1)

tk.Button(root, text="Crear Trabajo", command=crear_trabajo).grid(row=7, column=2)

tk.Button(root, text="Asignar Trabajos", command=asignar_trabajos).grid(row=8, column=0)
tk.Button(root, text="Ver Estado Empleados", command=mostrar_estado_empleados).grid(row=8, column=1)

resultados = tk.Text(root, height=15, width=70)
resultados.grid(row=9, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()
