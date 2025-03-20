import os
import config
import mysql

def administracion():
    os.system("cls")
    print("Estamos en administración : ")

def psw_a_pelo():
    pswd = """    Biofruta2023.                   VLC - E....0a 
        
        Pt nuevo - Lu....a- 
        
        Pt nw - En....a 
        
        484 - Enz...a 
        
        Mail. - T....a- 
        
        Vnc – Infopc00 
        
        
        PENDRIVE 
        
        Minipartición 
        
        Debían nube acer 
        192.168.1.97 
        Myvlcsys 
        Tete2510a 
        root 
        MiTucson19. 
        
        Dns  
        172.20.0.28 
        10.184.67.99


          """
    print(pswd)
    os.system("pause")
    config.menu()

    return "sw"

def psw_bd():
    print("pswd_BD")
    try:
        conexion2=mysql.connector.connect(host="myvlcsys.com", user="u591865418_usu_myvlcsys", passwd="oD7TRr&2tO@", database ="u591865418_bd_myvclsys_es")
        sql_select_Query = "select * from t_mis_cont"
        cursor = conexion2.cursor()
        cursor.execute(sql_select_Query)
        # get all records
        records = cursor.fetchall()
        print("Total number of rows in table: ", cursor.rowcount)

        print("\nPrinting each row")
        for row in records:
                print("Id = ", row[0], )
                print("Sitio = ", row[1])
                print("Usuario = ", row[2])
                print("Password = ", row[3])
                print("Categoria = ", row[4])
                print("Fecha Alta = ", row[5])
                print("Activo  = ", row[6], "\n")
                

    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
    
    
    os.system("pause")
    config.menu()

    return "sw"
    
