import mysql.connector
from getpass import getpass


#### SELECT DE BD
import librerias_gestion

print("" +librerias_gestion.cabecera())


###### pasamos usario y contraseña para validar usuario
usu=input("Usuario :")
pswd= getpass("Password:").encode('utf-8')
print("")
print("")


librerias_gestion.validar_usuario(usu, pswd)


print ("")
print("Select BD ")
print ("")

