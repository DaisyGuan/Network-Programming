#socketprogramming.py

#creating a socket

#Socket client example in python
#Address Family: AF_INET(this is IPv4)
#Type: SOCK_STREAM (this means connection oriented TCP protocol)
import socket #for sockets
import sys #for exit
try:
	#create an AF_INET, STREAM socket (TCP)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#error handling
except socket.error, msg:
	print 'Failed to creat socket. Error code: ' + str(msg[0]) + ' , Error message : ' + sys.exit();

print 'Socket Created'
#connect to server
host = 'www.google.com'
port = 80
#get ip address
try:
	remote_ip = socket.gethostbyname(host)

except socket. gaierror:
	#could not resolve
	print 'Hostname could not be resolved. Exiting'
	sys.exit()

print 'IP address of ' + host + ' is ' + remote_ip

#use port to connect
s.connect((remote_ip, port))

print 'Socket Connected to ' + host + ' on ip ' + remote_ip

#send some data to remote server
message = "GET / HTTP/1.1\r\n\r\n"

try :
	#Set the whole string
	s.sendall(message)
except socket.error:
	#send failed
	print 'Send failed'
	sys.exit()

print 'Message send successfully'

#Now receive data
reply = s.recv(4096)

print reply

s.close()

