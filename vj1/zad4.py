import socket
ipAdress = "8.8.8.8"
hostName = socket.gethostbyaddr(ipAdress)
print("Host name for the ipAdress {} is {}".format(ipAdress,hostName))
