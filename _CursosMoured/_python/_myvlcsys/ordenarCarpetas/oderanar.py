import os
import shutil
 
def ordenar_por_extension(carpeta):
    # Crear un diccionario para mantener la cuenta de las extensiones
    extensiones = {}
 
    for archivo in os.listdir(carpeta):
        # Obtener la extensión del archivo
        ext = os.path.splitext(archivo)[1].lower()
        if ext:
            # Crear una subcarpeta para la extensión si no existe
            dir_ext = os.path.join(carpeta, ext[1:])  # quita el punto de la extensión
            os.makedirs(dir_ext, exist_ok=True)
            
            # Mover el archivo a la subcarpeta
            shutil.move(os.path.join(carpeta, archivo), os.path.join(dir_ext, archivo))
 
# Llamar a la función con el camino a la carpeta
ordenar_por_extension('C:\\Users\\Chato\\Downloads')