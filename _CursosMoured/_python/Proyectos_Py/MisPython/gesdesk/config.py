import mysql
import hashlib
import getpass
import misFunciones


def cabecera():
        testo_cab_l_1="""
        
        ###################################################
        ###################################################
        
        #######     GESDESK MYVLCSYS BETA V.0.1     #######

        ###################################################
        ###################################################
        
        """
        print (testo_cab_l_1)
        return  ""

def val_password():
        pwd2 = '$2b$12$U4kNV/yvgTENsLjPiiMHau0yHejCGOstvj3NysA/KCjWsHAfJ7Mti'
        p=pwd2
        return p

def menu():
       
       print ("1- Admiinstrar")
       print ("2- Gestor de contraseñas")
       print ("3- Gestor de contraseñas BD")
       print ("4- Salir")
       op_menu_elegida= input("Selecciones alguna de las opciones anteriores: ")
       print("aqui" + op_menu_elegida) 

       if op_menu_elegida == "1":
                print("print" + op_menu_elegida)
                print(op_menu_elegida)
                misFunciones.administracion()
                print("opcion de menu1")
       elif op_menu_elegida == "2":
               print("opcion de menu 2")
               misFunciones.psw_a_pelo()
       elif op_menu_elegida == "3":
               print("opcion de menu 3")
               misFunciones.psw_bd()
       
