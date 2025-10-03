import json
from datetime imp   ort datetime

# Clase Tarea
class Tarea:
    def __init__(self, titulo, descripcion, prioridad, fecha_limite, completada=False):
        self.titulo = titulo
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.fecha_limite = fecha_limite
        self.completada = completada

    def __str__(self):
        estado = "✅ Completada" if self.completada else "⏳ Pendiente"
        return f"[{estado}] {self.titulo} | Prioridad: {self.prioridad} | Vence: {self.fecha_limite}"

# Clase Gestor de Tareas
class GestorTareas:
    def __init__(self, archivo="tareas.json"):
        self.tareas = []
        self.archivo = archivo
        self.cargar()

    # Crear tarea
    def agregar_tarea(self, titulo, descripcion, prioridad, fecha_limite):
        tarea = Tarea(titulo, descripcion, prioridad, fecha_limite)
        self.tareas.append(tarea)
        self.guardar()

    # Listar tareas
    def mostrar_tareas(self):
        if not self.tareas:
            print("No hay tareas registradas.")
        else:
            for i, tarea in enumerate(self.tareas, 1):
                print(f"{i}. {tarea}")

    # Actualizar tarea (marcar completada)
    def completar_tarea(self, indice):
        try:
            self.tareas[indice - 1].completada = True
            self.guardar()
        except IndexError:
            print("Número de tarea no válido.")

    # Eliminar tarea
    def eliminar_tarea(self, indice):
        try:
            self.tareas.pop(indice - 1)
            self.guardar()
        except IndexError:
            print("Número de tarea no válido.")

    # Guardar en archivo
    def guardar(self):
        datos = [t.__dict__ for t in self.tareas]
        with open(self.archivo, "w") as f:
            json.dump(datos, f, indent=4)

    # Cargar desde archivo
    def cargar(self):
        try:
            with open(self.archivo, "r") as f:
                datos = json.load(f)
                self.tareas = [Tarea(**t) for t in datos]
        except FileNotFoundError:
            self.tareas = []

# Programa principal
def menu():
    gestor = GestorTareas()

    while True:
        print("\n--- GESTOR DE TAREAS ---")
        print("1. Agregar tarea")
        print("2. Ver tareas")
        print("3. Completar tarea")
        print("4. Eliminar tarea")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            descripcion = input("Descripción: ")
            prioridad = input("Prioridad (Alta/Media/Baja): ")
            fecha_limite = input("Fecha límite (dd-mm-aaaa): ")
            gestor.agregar_tarea(titulo, descripcion, prioridad, fecha_limite)

        elif opcion == "2":
            gestor.mostrar_tareas()

        elif opcion == "3":
            gestor.mostrar_tareas()
            num = int(input("Número de tarea a completar: "))
            gestor.completar_tarea(num)

        elif opcion == "4":
            gestor.mostrar_tareas()
            num = int(input("Número de tarea a eliminar: "))
            gestor.eliminar_tarea(num)

        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

# Ejecutar programa
if __name__ == "__main__":
    menu()
