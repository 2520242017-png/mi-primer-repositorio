print ("hola mundo")

import tkinter as tk
from tkinter import messagebox

# CLASE

class Mascota:
    def __init__(self, nombre, especie, edad, dueno):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.dueno = dueno

    def mostrar_info(self):
        return f"{self.nombre} | {self.especie} | {self.edad} años | Dueño: {self.dueno}"


# DATOS

lista_mascotas = []
mascotas_por_especie = {}


# FUNCIONES

def registrar_mascota():
    nombre = entry_nombre.get()
    especie = entry_especie.get()
    edad = entry_edad.get()
    dueno = entry_dueno.get()

    if not nombre or not especie or not edad or not dueno:
        messagebox.showwarning("Campos vacíos", "Completa todos los campos")
        return

    mascota = Mascota(nombre, especie, edad, dueno)
    lista_mascotas.append(mascota)

    if especie not in mascotas_por_especie:
        mascotas_por_especie[especie] = []

    mascotas_por_especie[especie].append(mascota)

    messagebox.showinfo("Registro exitoso", "Mascota registrada correctamente")
    limpiar_campos()


def buscar_mascota():
    nombre = entry_buscar.get()
    for mascota in lista_mascotas:
        if mascota.nombre.lower() == nombre.lower():
            resultado.set(mascota.mostrar_info())
            return

    resultado.set("❌ Mascota no encontrada")


def mostrar_todas():
    if not lista_mascotas:
        resultado.set("No hay mascotas registradas")
        return

    texto = "\n".join([m.mostrar_info() for m in lista_mascotas])
    resultado.set(texto)


def limpiar_campos():
    entry_nombre.delete(0, tk.END)
    entry_especie.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_dueno.delete(0, tk.END)


# INTERFAZ

ventana = tk.Tk()
ventana.title("Sistema de Registro de Mascotas")
ventana.geometry("500x500")
ventana.config(bg="#f4f6f7")

# TÍTULO
tk.Label(
    ventana,
    text="Clínica Veterinaria 🐾",
    font=("Arial", 18, "bold"),
    bg="#f4f6f7"
).pack(pady=10)

# FRAME REGISTRO

frame_registro = tk.Frame(ventana, bg="white", bd=2, relief="groove")
frame_registro.pack(pady=10, padx=20, fill="x")

tk.Label(frame_registro, text="Registro de Mascotas", font=("Arial", 12, "bold"), bg="white").grid(row=0, column=0, columnspan=2, pady=5)

tk.Label(frame_registro, text="Nombre:", bg="white").grid(row=1, column=0, sticky="e")
entry_nombre = tk.Entry(frame_registro)
entry_nombre.grid(row=1, column=1, pady=2)

tk.Label(frame_registro, text="Especie:", bg="white").grid(row=2, column=0, sticky="e")
entry_especie = tk.Entry(frame_registro)
entry_especie.grid(row=2, column=1, pady=2)

tk.Label(frame_registro, text="Edad:", bg="white").grid(row=3, column=0, sticky="e")
entry_edad = tk.Entry(frame_registro)
entry_edad.grid(row=3, column=1, pady=2)

tk.Label(frame_registro, text="Dueño:", bg="white").grid(row=4, column=0, sticky="e")
entry_dueno = tk.Entry(frame_registro)
entry_dueno.grid(row=4, column=1, pady=2)

tk.Button(
    frame_registro,
    text="Registrar",
    bg="#2ecc71",
    fg="white",
    command=registrar_mascota
).grid(row=5, column=0, columnspan=2, pady=10)

# FRAME BÚSQUEDA

frame_busqueda = tk.Frame(ventana, bg="white", bd=2, relief="groove")
frame_busqueda.pack(pady=10, padx=20, fill="x")

tk.Label(frame_busqueda, text="Buscar Mascota", font=("Arial", 12, "bold"), bg="white").pack(pady=5)

entry_buscar = tk.Entry(frame_busqueda)
entry_buscar.pack(pady=5)

tk.Button(
    frame_busqueda,
    text="Buscar",
    bg="#3498db",
    fg="white",
    command=buscar_mascota
).pack(pady=5)

tk.Button(
    frame_busqueda,
    text="Mostrar todas",
    bg="#9b59b6",
    fg="white",
    command=mostrar_todas
).pack(pady=5)

# RESULTADOS

resultado = tk.StringVar()

tk.Label(
    ventana,
    text="Resultados:",
    font=("Arial", 12, "bold"),
    bg="#f4f6f7"
).pack()

tk.Label(
    ventana,
    textvariable=resultado,
    bg="white",
    width=50,
    height=10,
    anchor="n",
    justify="left",
    wraplength=400,
    relief="sunken"
).pack(padx=20, pady=10)


# EJECUCIÓN
ventana.mainloop()