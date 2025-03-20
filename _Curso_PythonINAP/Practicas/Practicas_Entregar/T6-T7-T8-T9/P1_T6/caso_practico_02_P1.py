""" **// caso practico 2 Pregunta 1

    • Imprima por pantalla la hora con el siguiente formato: 19:37:52.
    • Imprima por pantalla la ruta del ejecutable de Python.
    • Imprima la versión de Python con la que se está trabajando.

 """
import datetime
import pathlib
import sys

esLaHora= datetime.datetime.now().time()

print("Hora actual: " + esLaHora.strftime('%H:%M:%S'))

ruta_ejecutable= pathlib.Path(__file__).parent.absolute()

print("Ruta de achivo ejcutable: " + str(ruta_ejecutable))

version_python =sys.version

print("La versión de Python en la que se está trabajado es: " + str(version_python))


