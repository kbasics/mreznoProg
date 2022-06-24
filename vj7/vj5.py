#Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
#Type "help", "copyright", "credits" or "license()" for more information.

import socket
import subprocess
import sys
from datetime import datetime
from vj_zad1 import print_machine_info
import multiprocessing
from multiprocessing import pool

t1 = datetime.now()
print_machine_info()
print("Vrijeme početka skeniranja je: ", t1)

def port_scanner(arg):
    remoteServerIP, PortNumber = arg
    tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_sock.settimeout(0.5)
    result = tcp_sock.connect_ex((remoteServerIP, PortNumber))
    if result == 0:
        return PortNumber, True
    else:
        return PortNumber, False
    tcp_sock.close()


def pool_handler(ports):
    broj_cpu = multiprocessing.cpu_count()

    pool = multiprocessing.Pool(processes=broj_cpu*2)

    for port, status in pool.map(port_scanner, [(remoteServerIP, port) for port in ports]):
        if status == True:  
            print("Port {}:  Otvoren".format(port))
        else:
            print("Port {}:  Zatvoren".format(port))
            
if __name__ == "__main__":
    
    remoteServer = input("Molim vas unesite adresu hosta koju zelite testirati: ")
    remoteServerIP = socket.gethostbyname(remoteServer)

   

  

    port1 = int(input("Unesite prvi port: "))
    port2 = int(input("Unesite drugi port: "))
  
   

    ports = range(port1, port2 + 1)
    pool_handler(ports)

    t2 = datetime.now()

    total = t2 - t1

    print("Skeniranje zavrseno za: ", total)
