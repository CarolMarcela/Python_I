#Sistema de Gestion de Tareas
class Tarea:
    def __init__(self, titulo, descripcion, estado="pendiente"):
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = estado

def mostrar_menu():
    print("Sistema de Gestión de Tareas")
    print("1. Agregar Tarea")
    print("2. Mostrar Todas las Tareas")
    print("3. Buscar Tarea por Título")
    print("4. Actualizar Estado de Tarea")
    print("5. Eliminar Tarea por Título")
    print("6. Salir")

Tareas = []

while True:
    mostrar_menu()
    opcion = input("Elige una opción:")

    if opcion == "6":
        print("Saliendo del programa.")
        break

    if opcion == "1": #Agregar una nueva tarea
        titulo = input("Ingresar el título de la tarea: ")
        descripcion = input("Ingresar la descripción de la tarea:")
        tarea = Tarea(titulo, descripcion)
        Tareas.append(tarea)
        print("Tarea agregada.")

    elif opcion == "2": #Mostrar todas las tareas
        for t in Tareas:
                print(f"Título: {t.titulo}, Descripción: {t.descripcion}, Estado: {t.estado}")


    elif opcion == "3": #Buscar tarea por título
        titulo = input("Ingresa el título de la tarea a buscar: ")
        encontrado = False
        for t in Tareas:
            if t.titulo == titulo:
                print(f"Título: {t.titulo}, Descripción: {t.descripcion}, Estado: {t.estado}")
                encontrado = True
                break
        if not encontrado:
            print("Tarea no encontrada.")


    elif opcion == "4":  #Actualizar estado de tarea con manejo de errores
        try:
            titulo = input("Ingresa el título de la tarea a actualizar: ")
            encontrado = False
            for t in Tareas:
                if t.titulo == titulo:
                    t.estado = "completada"
                    print("Estado de la tarea actualizado a completada.")
                    encontrado = True
                    break
            if not encontrado:
                print("Tarea no encontrada.")
        except ValueError:
            print(f"Ocurrió un error al actualizar la tarea:")


    elif opcion == "5": #Eliminar tarea por título
        titulo = input("Ingresa el título de la tarea a eliminar: ")
        encontrado = False
        for t in Tareas:
            if t.titulo == titulo:
                Tareas.remove(t)
                print("Tarea eliminada.")
                encontrado = True
                break
        if not encontrado:
            print("Tarea no encontrada.")
    
    else:
        print("Opcion no valida, intentar de nuevo.")