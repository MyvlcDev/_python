import socket

def main():

    host = 'localhost'
    port = 8081
    mySocket = socket.socket()
    mySocket.connect((host, port))
    message = input(" -> ")

 
    while message != 'q':

        mySocket.send(message.encode())
        data = mySocket.recv(1024).decode()
        print(data)
        message = input(" -> ")

       

    mySocket.close()

 

if __name__ == '__main__':

    main()