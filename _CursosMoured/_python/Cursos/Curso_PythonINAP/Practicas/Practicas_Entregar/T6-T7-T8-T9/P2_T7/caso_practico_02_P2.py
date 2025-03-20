from Persona import Persona
from Trabajador import Trabajador

per = Persona ("Antonio Jose")
per.darApeliido("Jimenez Martinez")
per.darDNI(23948345)
per.darFechaNacimeitno ("12/04/1983")

trab = Trabajador("Oficinista")
trab.darSueldo(1200)

print("El trabajador " + str (per.mostrarNombre()) + 
      " " + str(per.mostrarApellidos())+ "con Dni " +str(per.mostrarDNI()) +
        ",\n con puesto en la empresa, "+ str(trab.mostrarCargo()) +
          ",\n actualmente dispone de un salario de " + str( trab.mostrarSueldo()))




