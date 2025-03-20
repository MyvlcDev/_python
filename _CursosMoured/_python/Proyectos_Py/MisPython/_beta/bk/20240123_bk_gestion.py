from getpass import getpass
import mysql.connector


print ("Gestión")


############
############      FUNCIONES
############
def validar_usuario(usuario,pswds):
    print("Datos recogidos de usuario: " )
    print("Usuario: " + usu)
    print("Password (0): " + pswds)
    param_prue="parametro de prueba" 


    #### CONEXION DE BD
    
    print("vamos a conectar con la bd--")
    conexion1=mysql.connector.connect(host="myvlcsys.com", user="u591865418_usu_myvlcsys", passwd="oD7TRr&2tO@")
    cursor1=conexion1.cursor()
    cursor1.execute("show databases")
    ##cursor1.execute("select * from prueba")
    for base in cursor1:
        print(base)
    conexion1.close()
    
    
    ### SELEC DE BD
    '''
    
    conexion2=mysql.connector.connect(host="myvlcsys.com", user="u591865418_usu_myvlcsys", passwd="oD7TRr&2tO@")
    cursor2=conexion2.cursor()
    cursor2.execute("SELECT * FROM prueba")
    myresult = cursor2.fetchall()
    for x in myresult:
        print("Imprimiendo todo de tabla prueba" + x)
    conexion2.close()
    '''
    

    
    





    



    

def conexion_BD_usu(usuario_v, passwd_v):
    print("en fucnion conexión bd :" + usuario_v + " - " + passwd_v)
    conexion1=mysql.connector.connect(host="myvlcsys.com", user="u591865418_usu_myvlcsys", passwd="oD7TRr&2tO@")
    cursor1=conexion1.cursor()
    cursor1.execute("show databases")
    for base in cursor1:
        print(base)
    conexion1.close()
    if(5==5):
        print("5"+ parametro)




def menu():
    print("1- Gestión de Contraseñas: ")
    print("2- Notas: ")



############
############ FIN  FUNCIONES
############


############
############      PROGRAMA
############


print("Validación de usuario: ")

usu=input("Usuario :")
pswd= getpass("Password 2:")

validar_usuario(usu,pswd)



menu()

print("elija una opción de menu: ")


