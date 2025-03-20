import mysql
import hashlib
import getpass


def cabecera():
        testo_cab_l_1="""
        
        ###################################################
        ###################################################
        
        #######     GESTIÓN MYVLCSYS BETA V.0.1     #######

        ###################################################
        ###################################################
        
        """
        print (testo_cab_l_1)
        return  ""
        


def validar_usuario(usuario_validar, password_validar):
        try:
                print("Dentro de libreria de gestion")
                print("")

                mi_pasword= password_validar

                activo_u=False
                exixte_u=False
                
                                
        

                ## password_por_teclado = str(input("Password:\n")).encode('utf-8')
                psw_sha224 =  hashlib.sha224(mi_pasword).hexdigest()
                cifrado_pwd = str(psw_sha224)
                
                print(usuario_validar)
                print(cifrado_pwd)
                print("")



                
                conexion2=mysql.connector.connect(host="myvlcsys.com", user="u591865418_usu_myvlcsys", passwd="oD7TRr&2tO@", database ="u591865418_bd_myvclsys_es")
                sql_select_Query = "select * from t_gestion"
                cursor = conexion2.cursor()
                cursor.execute(sql_select_Query)
                # get all records
                records = cursor.fetchall()
                ##print("Total number of rows in table: ", cursor.rowcount)

                ##print("\nPrinting each row")
               
                """  for row in records:
                       print("Id = ", row[0], )
                       print("Name = ", row[1])
                       print("Password = ", row[2])
                       print("Activo = ", row[3])
                       print("Comentarios  = ", row[4])
                       print("Privilegios  = ", row[5], "\n") """
                
                for row in records:
                       if row[1] == usuario_validar:
                            print("usuario dentro del if : ", row[1] )
                            exixte_u=True

                for row3 in records:  ### AQUI VER QUE HACER  
                        if row[1] == usuario_validar:
                                if(row3[3]== 0):
                                        print("Parametro de Activo : Inactivo" )
                                        activo_u=False
                                else:                                  
                                        print("Parametro de Activo : Activo" )
                                        activo_u=True
                                        
                               
                                  

                for row3 in records:
                       if row3[1] == usuario_validar:
                            print("Coemntarios : ", row[4] )
                            activo_u=True

                                               

                
                        

                if exixte_u==True and activo_u == True:
                      print ("Usuario exite zz y activo.")
                else:
                      print ("El usuario NO está activo, o NO existe.")
                


                                                 
                            
                            
                            
                            
                        

                      

        except mysql.connector.Error as e:
          print("Error reading data from MySQL table", e)
        # finally:
        #         if conexion2.is_connected():
        #                 conexion2.close()
        #                 cursor.close()
        #                 print("MySQL connection is closed")
          

def menu():
       
       print ("1- Admiinstrar")
       print ("2- Gestor de contraseñas")
       print ("3- Salir")

