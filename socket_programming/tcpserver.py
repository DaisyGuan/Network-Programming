#socket.py

#import socket module

from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket
#set port
port = 6789
#bind
serverSocket.bind(('',port))
serverSocket.listen(1)

while True:
	#establish the connection
	print 'Ready to serve...'
	connectionSocket, addr = serverSocket.accept()
	try:
		message = connectionSocket.recv(1024)
		filename = message.split()[1]
		f = open(filename[1:])
		outputdata = f.read()
		#send one http header line into socket
		connectionSocket.send('\nHTTP/1.x 200 OK\n') #sends a 200 OK header line
		#send the content of the requested file to the client 
		for i in range (0, len(outputdata)):
			connectionSocket.send(outputdata[i])
		connectionSocket.close()
	except IOError:
		#send response message for file not found
		connectionSocket.send('\n404 not found\n')
		
		#close clent socket
		connectionSocket.close()
		
serverSocket.close()		
