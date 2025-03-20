"""  * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
  
 */  """

import sys


#delcaro mi diccionario llamado Contacto

contacto= {}
control = True

contacto={

    "nombre":" ",
    "apellidos":" ",
    "telefono":" "

}

def insertasrContacto():
    
    print("\n")
    print("in")
    nombre_input = input("Por favor introduzca su Nombre: ")
    apellido_input = input("Por favor introduzca su Apellido: ")    
    telefono_input = nombre= input("Por favor introduzca su Telefono: ")

    contacto["nombre"]= nombre_input
    contacto["apellidos"] = apellido_input
    contacto["telefono"] = telefono_input

    menu()



    


def actualizarContacto():
    print("ac")
    pass

def eliminarContacto():
    print("el")
    pass

def buscarContacto():
    print("bs")
    pass
    ##volver a menu
    op = int(input("Pulse 0 para volver a menu: "))

    if op == 0:
     menu()
     control = True
    

    pass

def mostrarContactos():

    # Obtener todos los pares clave-valor del diccionario
    print("mostrar contacto")

    for clave, valor in contacto.items():
        print(f"{clave}: {valor}")
    
    

def menu():

    print("\n")
    print("Elija una de las siguientes opciones: ")
    print("\n")
    print("1. Insertar contacto") 
    print("2. Actualizar contacto")
    print("3. Eliminar contacto")
    print("4. Buscar contacto")
    print("5. Mostrar contactos")
    print("6. Salir")

    print("\n")
    
    opcion = int(input("Selecciona una opción: "))
    return opcion

def main():
    
    opcion=menu()
    print(opcion)

    while control==True:
    
        if opcion == 1:
            insertasrContacto()
        elif opcion == 2:
            actualizarContacto()
        elif opcion == 3:
            eliminarContacto()
        elif opcion == 4:   
            buscarContacto()
        elif opcion == 5:
            mostrarContactos()
        elif opcion == 6:
            sys.exit()
        else:
            print("Opción no válida")   
        ##pass


main()