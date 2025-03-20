
###
## arreglar el mostrar para que muestre bien los datos
###
print("Agenda")



class Agenda:

    def __init__(self):
        
        self.contacto=[]    
    
    def registrar_contacto(self):

        nombre = input ("Introduce el nombre: ").strip
        self.contacto.append(nombre)
        apellido = input ("Introduce el apellido: ").strip  
        self.contacto.append(apellido)
        telefono = input ("Introduce el Telefon: ").strip
        self.contacto.append(telefono)
    
    def mostrar_contacto(self):
        print("Mostrando los contactos")
        for elements in self.contacto:
            print (str(elements))


agenda = Agenda()



while True:
    
    print("\n")
    print("Elija una de las siguientes opciones: ")
    print("\n")
    print("1. Insertar contacto") 
    print("2. Actualizar contacto")
    print("3. Eliminar contacto")
    print("4. Buscar contacto")
    print("5. Mostrar contactos")
    print("6. Salir")

    option = input("\nSelecciona una opción: ")

    match option:

        case "1":
            agenda.registrar_contacto()
        case "2":
            pass
        case "3":
            pass
        case "4":
            pass
        case "5":
            agenda.mostrar_contacto()
        case "6":
            print("Saliendo del simulador...")
            break
        case _:
            print("Opción invalida, selecciones una opción correcta....")
            
        