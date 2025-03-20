from Persona import Persona
import re


nombre=input("Nombre: ")
apellidos= input("Apellidos: ")
fechaNac= input("Fecha Nacimiento: ")
dni= input("Número de DNI: ")


pers1 = Persona(nombre,apellidos,fechaNac,dni)



try:
    # Solicitar al usuario que ingrese texto
    # texto_ingresado = input("Por favor, ingresa algún texto: ")
   

    # Verificar si es texto
    if pers1.validar_texto(nombre):
        print("¡Has ingresado texto!")
    else:
        print("No has ingresado texto o solo has ingresado números u otros caracteres.")

except KeyboardInterrupt:
    print("\nInterrupción de teclado. El usuario ha cancelado la entrada de texto.")
except Exception as e:
    print("Se ha producido una excepción: No has introducido texto con formato valido para el valor nombre.")
    ##print ("El nombre o apellido no pueden tener cáracteres númericos.")
    


        
try:
    # Solicitar al usuario que ingrese texto
    # texto_ingresado = input("Por favor, ingresa algún texto: ")
   

    # Verificar si es texto
    if pers1.validar_texto(apellidos):
        print("¡Has ingresado texto!")
    else:
        print("No has ingresado texto o solo has ingresado números u otros caracteres.")

except KeyboardInterrupt:
    print("\nInterrupción de teclado. El usuario ha cancelado la entrada de texto.")
except Exception as e:
    print("Se ha producido una excepción: No has introducido texto con formato valido para el valor apellidos.")
    ##print ("El nombre o apellido no pueden tener cáracteres númericos.")
    