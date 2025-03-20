import os
import shutil


### https://j2logo.com/como-copiar-un-fichero-con-python/


### pathCarpeta=input('escribe el path de una carpeta')

### pathCarpeta2=input('escribe el path de otra carpeta')

pathCarpeta="C:\\Users\\Chato\\Desktop"
pathCarpeta2="C:\\Users\\Chato\Desktop\\prueba_copia"

if not os.path.isdir(pathCarpeta):
    print('la primera carpeta no existe')
elif not os.path.isdir(pathCarpeta2):
    print('la segunda carpeta no existe')



else:
    contenidos=os.listdir(pathCarpeta)
    for elemento in contenidos:
        shutil.copy(elemento, pathCarpeta2)