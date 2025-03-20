import socket

 

def main():

    # Definición del socket del servidor

    host = "127.0.0.1"

    port = 5000

 

    # Instancia del objeto socket

    mySocket = socket.socket()

 

    # Enlace al socket definido para el servidor

    mySocket.bind((host, port))

 

    # Establece el número máximo de conexiones entrantes

    mySocket.listen(1)

    # Inicia la escucha

    conn, addr = mySocket.accept()

 

    #Imprime la dirección del cliente entrante

    print("Conexión desde: " + str(addr))

   

    # Bucle infinito para procesar la información entrante del cliente

    while True:

        # Decodifica la información entrante y la almacena en la variable 'data'

        data = conn.recv(1024).decode()

        if not data:

            break

        print("desde el usuario conectado: " + str(data))

 

        # La única operación que realiza es convertir a mayúsculas el texto que envia el cliente

        data = str(data).upper()

        print("enviando: " + str(data))

        # Envia de vuelta al cliente el texto modificado

        conn.send(data.encode())

 

    # Cierra la conexión

    conn.close()

 

if __name__ == '__main__':

    main()

