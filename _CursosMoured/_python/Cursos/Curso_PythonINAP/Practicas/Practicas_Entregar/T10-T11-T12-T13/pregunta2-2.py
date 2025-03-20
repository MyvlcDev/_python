import re

def buscar_usuario(nombre_usuario, archivo):
    # Convertimos el nombre de usuario a minúsculas para que la búsqueda sea insensible a mayúsculas/minúsculas
    nombre_usuario = nombre_usuario.lower()

    # Expresión regular para buscar el nombre de usuario en el texto
    patron = re.compile(rf'^.*?Nombre de usuario:\s*{re.escape(nombre_usuario)}\s*.*?$',
                        re.IGNORECASE | re.MULTILINE)

    # Buscamos coincidencias en el archivo
    coincidencias = patron.findall(archivo)

    # Si se encontraron coincidencias, las devolvemos
    if coincidencias:
        return coincidencias
    else:
        return None

def main():
    # Leemos el contenido del archivo de texto
    with open('fichero.txt', 'r') as file:
        archivo = file.read()

    # Pedimos al usuario que ingrese el nombre de usuario a buscar
    nombre_usuario = input("Ingrese el nombre de usuario a buscar: ")

    # Buscamos el usuario en el archivo
    resultados = buscar_usuario(nombre_usuario, archivo)

    # Si se encontraron resultados, los imprimimos
    if resultados:
        print("Datos encontrados:")
        for resultado in resultados:
            print(resultado)
    else:
        print("No se encontraron datos para el usuario especificado.")

if __name__ == "__main__":
    main()
