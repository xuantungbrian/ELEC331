#import socket module
from socket import *
import sys # In order to terminate the program
import webbrowser
import os
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
serverSocket.bind(('', 12000))
serverSocket.listen(1)
while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read().split()
        #Send one HTTP header line into socket
        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        connectionSocket.send('404 Not Found\r\n'.encode())
        #Close client socket
        connectionSocket.send("\r\n".encode())#not sure if this is right
        connectionSocket.close()
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data
#http://206.12.70.144:12000/HelloWorld.html
#home: http://10.0.0.103:12000/HelloWorld.html