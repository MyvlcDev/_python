import mysql.connector
import hashlib
from getpass import getpass

def desencriptar(texto_recibido):
   
   t1 = texto_recibido.strip("\n").encode('utf-8')
   texto_dec=  str(t1) ##estoy aqui
   
   ##print ("Texto descodificado1 :" + texto_dec  )

   return texto_dec



def desencriptar_2(texto_recibido):
   texto_codificado = str(texto_recibido)
   print ("Texto codificado dentro de funcion :" + texto_codificado)
   texto_a_descifrar=texto_codificado.encode('utf-8')
   texto_s224= hashlib.sha224(texto_a_descifrar).hexdigest()
   print ("Texto codificado dentro de funcion 224:" + texto_s224)
   texto_descifrado = str(texto_s224)

   return texto_descifrado

def encriptar(texto_teclado):
    texto_a_cifrar = texto_teclado.encode('utf-8')
    cifrado_sha224 =  hashlib.sha224(texto_a_cifrar).hexdigest()
    cifrado_text_fin = str(cifrado_sha224)
    
    ##print ("xxxxx "+cifrado_text_fin)


    return cifrado_text_fin



