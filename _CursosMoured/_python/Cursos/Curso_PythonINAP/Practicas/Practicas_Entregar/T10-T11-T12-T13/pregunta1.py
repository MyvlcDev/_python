import sys

archvio = open('fichero.txt', 'a')

print("\n") #### Salto de linea para formatear Texto

nombre = input("¿Cúal es tú nombre? ")
apellidos = input("¿Cúal es tú apellido? ")
edad = input("¿Cuántos años tienes? ")

datos_solicitados = {"Nombre:": nombre, "1er Apellido:": apellidos, "Edad:": edad,"":"" } #el último valor es para formatear el texto entre lo datos de persona y persona

print("\n") #### Salto de linea para formatear Texto

for misDatos, dato in datos_solicitados.items():
    print(f"{misDatos:15}  {dato:20}")
    archvio.write(f"{misDatos:15}  {dato:20}\n")
   

print("\n") #### Salto de linea para formatear Texto

archvio.close()





    

