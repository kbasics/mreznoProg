#Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
#Type "help", "copyright", "credits" or "license()" for more information.

import socket
import subprocess
import sys
from datetime import datetime
from vj_zad1 import print_machine_info
from logging.handlers import TimedRotatingFileHandler
from multiprocessing import Process, Queue
import threading
import multiprocessing
from multiprocessing import pool

t1 = datetime.now()
print_machine_info()
print("Vrijeme početka skeniranja je: ", t1)

print_lock = threading.Lock()
ports = Queue(maxsize=0)


def threader():
    while True:
        
        tcp_scanner(ports)


def main():
    for x in range(port1, port2, ):
        thread = threading.Thread(target=threader)
        thread.daemon = True
        thread.start()

    for port in range(port1, port2):
        ports.put(port)

    ports.join

hostname = input("Upisi host name: ")
remoteServerIP = socket.gethostbyname(hostname)

port1 = int(input("Upisi početni port: "))
port2 = int(input("Upisi zavrsni port: "))
print("prvi port: {}, drugi port: {}".format(port1,port2))

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

def tcp_scanner(ports):
    broj_cpu = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=broj_cpu*2)
    
    for port, status in pool.map(port_scanner, [(remoteServerIP, port) for port in ports]):

        
        if status == True:
           
            print("Port {}:  Otvoreno".format(port))
        else:
            print("Port {}:  Zatvoren".format(port))



t2 = datetime.now()
total = t2 - t1


print("Skeniranje zavrseno za: ", total)
