import mysql.connector
print("Conexion BD ")


#### CONEXION DE BD

def fun_conexion_Bd():
        try:
              conexion2=mysql.connector.connect(host="myvlcsys.com", user="u591865418_usu_myvlcsys", passwd="oD7TRr&2tO@")
              if conexion1.is_connected():
                print("conexión exitosa")
                info_server=conexion1.get_server_info()
                print(info_server)
                cursor1=conexion1.cursor()
                cursor1.execute("show databases")
                row= cursor1.fetchone()
                print("Conectado a la base de datos, mediante la funciónn : {}".format(row))

        except Exception as ex:
                print(ex) 



#########
######
""" try:
        conexion1=mysql.connector.connect(
        host="myvlcsys.com", 
        user="u591865418_usu_myvlcsys",
        passwd="oD7TRr&2tO@")
        

        if conexion1.is_connected():
              print("conexión exitosa")
              info_server=conexion1.get_server_info()
              print(info_server)
              cursor1=conexion1.cursor()
              cursor1.execute("show databases")
              row= cursor1.fetchone()
              print("Conectado a la base de datos : {}".format(row))
        #for base in cursor1:
         #print(base)
             

        ## FIN DE TRY
except Exception as ex:
        print(ex)
##finally:
##        if conexion1.is_connected(): 
##           conexion1.close()              
##           print("Conexión finalizada") """
        

#### SELECT DE BD
                

print("Select BD ")

try:
        conexion1=mysql.connector.connect(
        host="myvlcsys.com", 
        user="u591865418_usu_myvlcsys",
        passwd="oD7TRr&2tO@")
        

        if conexion1.is_connected():
              print("conexión exitosa")
              info_server=conexion1.get_server_info()
              print(info_server)
              cursor1=conexion1.cursor()
              cursor1.execute("select * from prueba")
              row= cursor1.fetchone()
              print("Conectado a la base de datos : {}".format(row))
        #for base in cursor1:
         #print(base)
             

        ## FIN DE TRY
except Exception as ex:
        print(ex)

print("------------")
print("------------")

fun_conexion_Bd()