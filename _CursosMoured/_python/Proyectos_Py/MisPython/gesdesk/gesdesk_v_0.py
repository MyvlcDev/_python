import mysql.connector
from getpass import getpass
import bcrypt
import os

import config
import misFunciones


print("" +config.cabecera())

###### pasamos usario y contraseña para validar usuario
usu=input("Usuario :")


##### validar contraseña pwd2 = chato

pwd2 = b'$2b$12$U4kNV/yvgTENsLjPiiMHau0yHejCGOstvj3NysA/KCjWsHAfJ7Mti'

txt2 = bytes(getpass("Password1:").encode('utf-8'))
####if bcrypt.checkpw(txt2, pwd2) el if funciona asi

txt3=config.val_password()

if bcrypt.checkpw(txt2, pwd2):
    print("la contraseña es correcta")
    config.menu()
          
else:
    print("La contraseña es incorrecta")



def administracion():
    os.system("cls")
    print("Estamos en administración : ")