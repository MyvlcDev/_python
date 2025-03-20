import mysql.connector
#### INSERT DE BD

print("------------")
print("------------")
                

#### INSERT DE BD


def fun_insert_Bd():
        try:
                conexion2=mysql.connector.connect(host="myvlcsys.com", user="u591865418_usu_myvlcsys", passwd="oD7TRr&2tO@", database ="u591865418_bd_myvclsys_es")
                mycursor = conexion2.cursor()
                ##sql = "INSERT into prueba (id, usuario, password, departamento) VALUES (16,'Luca','Luca_pass','Toys')"
                ##print("Sql generada " + sql)
                ##mycursor.execute(sql)
                mySql_insert_query = """INSERT INTO prueba (id, usuario, password, departamento)  VALUES (100,'Lucas_34','passord_lucas','dpto_lucas') """
                print(mySql_insert_query)
                ##record = (id, id,usuario, passw2, dpto)
                mycursor.execute("INSERT INTO prueba (id, usuario, password, departamento)  VALUES (100,'pedro34','passord_lucas','dpto_lucas')")
                conexion2.commit
                print(mycursor.rowcount)
                conexion2.close
                                

        except mysql.connector.Error as e:
          print("Error reading data from MySQL table", e)
        # finally:
        #         if conexion2.is_connected():
        #                 conexion2.close()
        #                 cursor.close()
        #                 print("MySQL connection is closed")

print ("")
print("INSERT BD ")
print ("")
fun_insert_Bd()

