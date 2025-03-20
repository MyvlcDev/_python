import mysql.connector



#### CONEXION DE BD



def fun_conexion_Bd():
        try:
              conexion2=mysql.connector.connect(host="myvlcsys.com", user="u591865418_usu_myvlcsys", passwd="oD7TRr&2tO@")
              if conexion2.is_connected():
                print("conexión exitosa")
                info_server=conexion2.get_server_info()
                print(info_server)
                cursor1=conexion2.cursor()
                cursor1.execute("show databases")
                row= cursor1.fetchone()
                print("Conectado a la base de datos, mediante la funciónn : {}".format(row))

        except Exception as ex:
                print(ex) 
print ("")
print("Conexion BD :")
print ("")
fun_conexion_Bd()

#########
######
  

print("------------")
print("------------")
                

#### SELECT DE BD


def fun_select_Bd():
        try:
                conexion2=mysql.connector.connect(host="myvlcsys.com", user="u591865418_usu_myvlcsys", passwd="oD7TRr&2tO@", database ="u591865418_bd_myvclsys_es")
                sql_select_Query = "select * from prueba"
                cursor = conexion2.cursor()
                cursor.execute(sql_select_Query)
                # get all records
                records = cursor.fetchall()
                print("Total number of rows in table: ", cursor.rowcount)

                print("\nPrinting each row")
                for row in records:
                        print("Id = ", row[0], )
                        print("Name = ", row[1])
                        print("Departamento  = ", row[2], "\n")
                      

        except mysql.connector.Error as e:
          print("Error reading data from MySQL table", e)
        # finally:
        #         if conexion2.is_connected():
        #                 conexion2.close()
        #                 cursor.close()
        #                 print("MySQL connection is closed")

print ("")
print("Select BD ")
print ("")
fun_select_Bd()

