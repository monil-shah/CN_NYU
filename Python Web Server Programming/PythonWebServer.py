# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
serverPort=1339
#Fill in start
serverSocket.bind(('192.168.1.161',serverPort))
serverSocket.listen(5)
print('the web server is up on port:',serverPort)
#Fill in end
while True:
 #Establish the connection
     print('Ready to serve...')
     connectionSocket, addr = serverSocket.accept()
     try:
         message = connectionSocket.recv(1024)
         filename = message.split()[1]
         f = open(filename[1:])
         outputdata = f.read()
        
 #Send one HTTP header line into socket
 #Fill in start
         connectionSocket.send(b"HTTP/1.1 200 OK\r\n\r\n")
         #connectionSocket.send(outputdata.encode())
 #Fill in end
 #Send the content of the requested file to the client
         for i in range(0, len(outputdata)):
             connectionSocket.send(outputdata[i].encode())
             connectionSocket.close()
     except IOError:
 #Send response message for file not found
 #Fill in start
         connectionSocket.send(b"HTTP/1.1 404 Not Found\r\n\r\n")
         connectionSocket.send(b"<html><head></head><body>404 not found</body></html>")
       
 #Fill in end
 #Close client socket
 #Fill in start
     connectionSocket.close()
 #Fill in end 
serverSocket.close() 
