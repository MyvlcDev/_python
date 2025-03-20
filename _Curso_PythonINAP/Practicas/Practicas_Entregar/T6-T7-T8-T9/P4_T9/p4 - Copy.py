from Persona import Persona

per = Persona ("Juan")
per.darNombre("chato")
per.darApeliido= 4
per.darDNI= "23948345G"
per.darFechaNacimeitno ="12/04/1983"

 
print(per.mostrarNombre())
print(per.mostrarApellidos())


if (per.mostrarNombre().isalpha()):
    print("la cadena introducida es valida")
else:
    print("la cadena introducida no es valida")


if (per.mostrarApellidos().isalpha()):
    print("la cadena introducida para el Apellido es valida")
else:
    print("la cadena introducida no Apellido es valida")



