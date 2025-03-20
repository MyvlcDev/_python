#
## 
###
####    SCRIPTI DE CONTRASEÑAS EN USO V_0.1 - 18/01/2024
###
##    
#
print("Mis contraseñas v.0.1.2 - 18/01/2024")

import mislibrerias
import lib_contrasenas
import sys
import mysql.connector
import hashlib
import getpass


##print(mislibrerias.saludo)

print("Usuario:")
usuario = input()
##print("Password:")

password_por_teclado_oculto= getpass.getpass().encode('utf-8')

## password_por_teclado = str(input("Password:\n")).encode('utf-8')
psw_sha224 =  hashlib.sha224(password_por_teclado_oculto).hexdigest()
cifrado_pwd = str(psw_sha224)

#####  descifrado_psw_sha224 = hashlib.sha224(psw_sha224).hexdigest()

## cprint("Passwrd :" + descifrado_psw_sha224)

########## JUEVES 18 CONEXIÓN BD

try:
    
    print(usuario)
    
    conexion2=mysql.connector.connect(host="myvlcsys.com", user="u591865418_usu_myvlcsys", passwd="oD7TRr&2tO@", database ="u591865418_bd_myvclsys_es")
    
    sql_select_Query = "select * from t_cont where usuario = '"+ usuario + "' "

    print("sql es:  " + sql_select_Query)


    cursor = conexion2.cursor()
    cursor.execute(sql_select_Query)
    # get all records
    records = cursor.fetchall()
    print("Total number of rows in table: ", cursor.rowcount)

    print("\nPrinting each row")
    for row in records:
        print("Id = ", row[0], )
        print("Name = ", row[1])
        print("Password = ", row[2])
        print("Departamento  = ", row[3], "\n")
except mysql.connector.Error as e:
          print("Error reading data from MySQL table", e)
        # finally:
        #         if conexion2.is_connected():
        #                 conexion2.close()
        #                 cursor.close()
        #                 print("MySQL connection is closed")      




def menu():
        print("estoy dentro del menuç'p del mismo archvio")
      



def gestion_contrasenas():

    print("estoy dentro de la gestion de contraseñas")

def conexion_bd():
    ##import mysql.connector
    


    conexion = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "programacionfacil",
    )
    cursor = conexion.cursor()
    cursor.execute("SHOW DATABASES")
    for bd in cursor:  # type: ignore
        print(bd)

    ####
        print("dentro de conexion_bd")
     ####









## SOLICITO POR CONSOLA USUARIO Y CONTREASEÑA



##psw_cifrado=cifrar()
##print("pasword cifrado : " + psw_cifrado)
##validar_us(usuario ,psw_cifrado)
