import socket

 
def main():
  
    host = "localhost"
    port = 8081

    mySocket = socket.socket()
    mySocket.bind((host, port))
    mySocket.listen(1)
    
    conn, addr = mySocket.accept()
    
    while True:

        data = conn.recv(1024).decode()

        if not data:

            break

        print("Mesaje recibido: " + data)
       
        mensaje= "Mensaje recibido"
        conn.send(mensaje.encode())
     
    conn.close()

 

if __name__ == '__main__':

    main()

