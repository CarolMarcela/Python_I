#Gestion de Contactos

#Definir la clase contacto
class Contacto:
    def __init__(self, nombre, telefono): # Inicializar la clase y los atributos
        #Constructor de la clase contacto
        self.nombre = nombre
        self.telefono = telefono

def mostrar_menu():
    print("Gestion de contactos")
    print("1. Agregar Contacto")
    print("2. Mostrar Contactos")
    print("3. Buscar Contacto")
    print("4. Eliminar Contacto")
    print("5. Salir")

Contactos = [] #Creamos lista para guardar contactos

while True:
    mostrar_menu()
    opcion = input("Elige una opcion:")

    if opcion == "5":
        print("Saliendo del programa.")
        break

    if opcion == "1": #Agregar un nuevo contacto
        nombre = input("Ingresar el nombre: ")
        telefono = input("Ingresar el telefono: ")
        contacto = Contacto(nombre,telefono)
        Contactos.append(contacto) # Metodo para agregar un elemento al final de la lista
        print("Contacto agregado")

    elif opcion == "2": #Mostrar contactos
        for c in Contactos:
            print(f"Nombre: {c.nombre}, Telefono: {c.telefono}")
    
    elif opcion == "3": #Buscar contacto por nombre
        nombre = input("Ingrese el nonmbre a buscar: ")
        encontrado = False
        for c in Contactos:
            if c.nombre == nombre:
                print(f"Nombre: {c.nombre}, Telefono: {c.telefono}")
                encotrado = True
                break
        if not encontrado:
            print("Contacto no encontrado")
    
    elif opcion == "4": #Eliminar contacto por nombre
        nombre = input("Ingrese el nombre del contacto a eliminar: ")
        encontrado = False
        for c in Contactos:
            if c.nombre == nombre:
                Contactos.remove(c)
                encontrado = True
                print("Contacto eliminado")
                break
        if not encontrado:
            print("Contacto no encontrado")

    else:
        print("Opcion no valida, intentar de nuevo.")
    


        
        
        