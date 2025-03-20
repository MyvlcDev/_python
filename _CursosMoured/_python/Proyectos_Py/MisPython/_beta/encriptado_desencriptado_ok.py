import mysql.connector
from getpass import getpass

import bcrypt

import libreria_myvlcsys

""" text_encripatado =libreria_myvlcsys.encriptar("hola")

print ("Texto encriptado : " + text_encripatado)

texto_desencriptado =libreria_myvlcsys.desencriptar(text_encripatado)

print("Texto desencriptado 1: " + texto_desencriptado) """

txt = input("Ingrese un texto: " ) 
pwd = txt.encode('utf-8')
sal= bcrypt.gensalt()
encript = bcrypt.hashpw(pwd, sal)

print(encript)

##### validar contraseña pwd2 = chato

pwd2 = b'$2b$12$U4kNV/yvgTENsLjPiiMHau0yHejCGOstvj3NysA/KCjWsHAfJ7Mti'

txt2 = bytes(input("Ingrese un texto: "), 'utf-8')
if bcrypt.checkpw(txt2, pwd2):
    print("la contraseña es correcta")
else:
    print("La contraseña es incorrecta")