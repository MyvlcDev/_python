###
#####   DOCUMENTACION 
#####
##### https://blog.tiraquelibras.com/?p=1041
#####
###

import hashlib

def cifrar():
    clave = str(input("Introduce la contraseña a cifrar: ")).encode('utf-8')
    sha224 = hashlib.sha224(clave).hexdigest()
    print("Hash SHA224: %s" % str(sha224))



if __name__ == '__main__':
    cifrar()

def descifrar():
    try:
        resolverhash = str(input("Hash a resolver: "))
       ## type = input("Indica el tipo de encriptación: ")

        resolvedor = open("10-million-password-list-top-1000000.txt", 'r')
        for x in resolverhash.readlines():
            a = x.strip("\n").encode('utf-8')
            a = hashlib.sha224(a).hexdigest()
           
            if a == resolverhash:
                
                print("Contraseña: %s - Has resuelto: %s - Encriptado con: %s" %(str(x.rstrip()),str(a),str(type)))
                break

    except Exception as e:
        print("Error: {}".format(e))

if __name__ == '__main__':
    descifrar()