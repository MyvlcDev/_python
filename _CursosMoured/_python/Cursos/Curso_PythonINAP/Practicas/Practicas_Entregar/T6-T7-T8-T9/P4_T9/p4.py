from Persona import Persona

per = Persona ("Juan")
per.darNombre("chato")
per.darApeliido= 4
per.darDNI= "23948345G"
per.darFechaNacimeitno ="12/04/1983"

 
print(per.mostrarNombre())
print(per.mostrarApellidos())




nom= str(per.mostrarNombre())
ape=per.mostrarApellidos()
    
def controdeTexto(self):
        if (self.isalpha()):
            return("la cadena es valida.")
        else:
            return("La cadena no reune las condiciones exigidas. Tiene caracteres no validos.")


print(""+controdeTexto(nom))

print(""+controdeTexto(ape))