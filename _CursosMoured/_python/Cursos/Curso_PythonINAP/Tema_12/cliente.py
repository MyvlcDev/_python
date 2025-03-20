import socket

 

def main():

    # Establece los datos del socket del servidor al que nos queremos conectar

    host = '127.0.0.1'

    port = 5000

 

    # Crea el objeto socket

    mySocket = socket.socket()

   

    # Establece conexión a los datos del socket del servidor

    mySocket.connect((host, port))

    # Solicita la entrada de texto al usuario

    message = input(" -> ")

 

    while message != 'q':

        # Codifica el mensaje y lo envia al servidor

        mySocket.send(message.encode())

        # Recibe la respuesta del servidor

        data = mySocket.recv(1024).decode()

        print('Recibido del servidor: ' + data)

        message = input(" -> ")

       

    # Cierra la conexión

    mySocket.close()

 

if __name__ == '__main__':

    main()