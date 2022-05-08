#tcp_server.py

import socket

server_socket = socket.socket()
host = socket.gethostname()
port = 9998

server_socket.bind((host,port))

print ('Waiting for connection...')
server_socket.listen(5)

while True:
	conn,addr = server_socket.accept()
	print ('Got Connection from', addr)
	conn.send('Server Saying Hi'.encode())
	conn.close()
    
#Pitanje: U serverskom dijelu vašeg programa, što znači drugi broj u
#zagradama kod ispisa „Got connection…“?
#Odgovor:klijentova IP adresa i TCP port
