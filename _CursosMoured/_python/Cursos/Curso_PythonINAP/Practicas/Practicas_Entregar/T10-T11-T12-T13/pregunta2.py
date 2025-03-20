import sys
import re

caracteres_a_buscar = input("Introduzca los tres primeros caracteres del nombre buscado: ")

with open("fichero.txt", "r") as archivo:
    contenido = archivo.read()
    ##
    patron = r"Nombre:\W+\b"+ caracteres_a_buscar+r"\w+\b"

    print("Lo resultados son los siguientes: "  )

    print( re.findall(patron,contenido, re.IGNORECASE))



## Faltaría mostrar las dos lineas siguientes, que no encuentro la forma.