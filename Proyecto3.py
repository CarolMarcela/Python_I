#Sistema de Inventario
class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

def mostrar_menu():
    print("Sistema de inventario")
    print("1. Agregar Producto")
    print("2. Mostrar Producto")
    print("3. Buscar Producto")
    print("4. Actualizar la cantidad de Producto")
    print("5. Eliminar Producto")
    print("6. Salir")

Inventario = [] #Crear lista

while True:
    mostrar_menu()
    opcion = input("Elige una opcion:")

    if opcion == "6":
        print("Saliendo del programa.")
        break

    if opcion == "1": #Agregar un nuevo prodcuto
        nombre = input("Ingresar el nombre del producto: ")
        try:
            cantidad = int(input("Ingresar la cantidad del producto"))
            precio = float(input("Ingresar el precio del producto"))
            producto = Producto(nombre, cantidad, precio)
            Inventario.append(producto)
            print("Producto agregado")
        except ValueError:
            print("Error: Entrada no valida")

    elif opcion == "2": #Mostrar Producto
        for p in Inventario:
            print(f"Nombre: {p.nombre}, Cantidad: {p.cantidad}, Precio: {p.precio}")

    elif opcion == "3": #Buscar Producto
        nombre = input("Ingresa el nombre del producto a buscar:")
        encontrado = False
        for p in Inventario:
            if p.nombre == nombre:
              print(f"Nombre: {p.nombre}, Cantidad: {p.cantidad}, Precio: {p.precio}")
              encontrado = True
              break
        if not encontrado: 
            print("Producto no encontrado.")

    elif opcion == "4": #Actualizar la cantidad de Producto
        nombre = input("Ingresa el nombre del producto a actualizar:")
        try:
            Nueva_Cantidad = int(input("Ingresa la nueva cantidad"))
            for p in Inventario:
                if p.nombre == nombre:
                    p.cantidad = Nueva_Cantidad
                    print("Cantidad actualizada")
                    break
        except ValueError:
            print("Error: Entrada no valida.")

    elif opcion == "5": #Eliminar Producto
        nombre = input("Ingresa el nombre del producto a eliminar: ")
        encontrado = False
        for p in Inventario:
            if p.nombre == nombre:
                Inventario.remove(p)
                print("Producto eliminado")
                encontrado = True
                break
        if not encontrado:
            print("Producto no encontrado.")

    else:
        print("Opcion no valida, intentar de nuevo.")
        


            

  


    

        