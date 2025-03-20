###
#####   DOCUMENTACION 
#####
##### https://blog.tiraquelibras.com/?p=1041
#####
###

import hashlib

def cifrar():
    clave = str(input("Introduce la contraseña a cifrar: ")).encode('utf-8')

    md5 = hashlib.md5(clave).hexdigest()
    print("Hash MD5: %s" % str(md5))

    sha1 = hashlib.sha1(clave).hexdigest()
    print("Hash SHA1: %s" % str(sha1))

    sha224 = hashlib.sha224(clave).hexdigest()
    print("Hash SHA224: %s" % str(sha224))

    sha256 = hashlib.sha256(clave).hexdigest()
    print("Hash SHA256: %s" % str(sha256))

    sha384 = hashlib.sha384(clave).hexdigest()
    print("Hash SHA384: %s" % str(sha384))

    sha512 = hashlib.sha512(clave).hexdigest()
    print("Hash SHA512: %s" % str(sha512))

if __name__ == '__main__':
    cifrar()

def descifrar():
    try:
        resolverhash = str(input("Hash a resolver: "))
        type = input("Indica el tipo de encriptación: ")

        resolvedor = open("10-million-password-list-top-1000000.txt", 'r')
        for x in resolvedor.readlines():
            a = x.strip("\n").encode('utf-8')
            if type == 'md5':
                a = hashlib.md5(a).hexdigest()
            elif type == 'sha1':
                a = hashlib.sha1(a).hexdigest()
            elif type == 'sha224':
                a = hashlib.sha224(a).hexdigest()
            elif type == 'sha256':
                a = hashlib.sha256(a).hexdigest()
            elif type == 'sha384':
                a = hashlib.sha384(a).hexdigest()
            elif type == 'sha512':
                a = hashlib.sha512(a).hexdigest()
            else:
                raise Exception('El tipo de encriptación %s no es válido.' %str(type))

            if a == resolverhash:
                print("Contraseña: %s - Has resuelto: %s - Encriptado con: %s" %(str(x.rstrip()),str(a),str(type)))
                break

    except Exception as e:
        print("Error: {}".format(e))

if __name__ == '__main__':
    try:
        resolverhash = str(input("Hash a resolver: "))
        type = input("Indica el tipo de encriptación: ")

        resolvedor = open("10-million-password-list-top-1000000.txt", 'r')
        for x in resolvedor.readlines():
            a = x.strip("\n").encode('utf-8')
            if type == 'md5':
                a = hashlib.md5(a).hexdigest()
            elif type == 'sha1':
                a = hashlib.sha1(a).hexdigest()
            elif type == 'sha224':
                a = hashlib.sha224(a).hexdigest()
            elif type == 'sha256':
                a = hashlib.sha256(a).hexdigest()
            elif type == 'sha384':
                a = hashlib.sha384(a).hexdigest()
            elif type == 'sha512':
                a = hashlib.sha512(a).hexdigest()
            else:
                raise Exception('El tipo de encriptación %s no es válido.' %str(type))

            if a == resolverhash:
                print("Contraseña: %s - Has resuelto: %s - Encriptado con: %s" %(str(x.rstrip()),str(a),str(type)))
                break

    except Exception as e:
        print("Error: {}".format(e))

if __name__ == '__main__':
    descifrar()
    descifrar()