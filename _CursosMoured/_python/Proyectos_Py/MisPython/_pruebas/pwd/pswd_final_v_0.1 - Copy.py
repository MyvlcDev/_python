#
## 
###
####    SCRPTI DE CONTRASEÑAS EN USO V_0.1 - 14/01/2024
###
##
#
print("mis contraseñas")

import mislibrerias
import lib_contrasenas

print(mislibrerias.saludo)

## SOLICITO POR CONSOLA USUARIO Y CONTREASEÑA

print("Usuario:")
usuario = input()

print("contraseña")
contrasena = input()


def validar_us(usuario, contrasena): ## esto ya funciona correctamente

    print(f"Me alegro de conocerle, {usuario}")

    if usuario == "chato" and contrasena=="aaaa":
        print("usuario y contraseña correcto")

        gestion_contrasenas()
        menu()
        return("ok2")
    else:
        print("Erro no es la contraseña correcta!!!! ")


def menu():
        print("estoy dentro del menu del mismo archvio")
      



def gestion_contrasenas():

    print("estoy dentro de la gestion de contraseñas")


validar_us(usuario ,contrasena)